<?php

namespace App\Controller;

use App\Entity\Test;
use App\Form\DijkstraTestingImplementationType;
use App\Massage\DijkstraImplementationTesting;
use App\Repository\TestRepository;
use App\Service\RandomStringGenerator;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\HttpFoundation\File\UploadedFile;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Uid\Uuid;

#[Route('/dijkstra', name: 'app_dijkstra_algorithm_')]
class DijkstraController extends AbstractController
{
    public function __construct(
        private readonly ParameterBagInterface $parameterBag,
        private readonly MessageBusInterface $messageBus,
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem,
        private readonly RandomStringGenerator $stringGenerator
    ) {
    }

    #[Route('/', name: 'index')]
    public function index(): Response
    {
        return $this->render('dijkstra/index.html.twig');
    }

    #[Route('/create', name: 'create')]
    public function createTest(Request $request): Response
    {
        $test = new Test();

        $form = $this->createForm(DijkstraTestingImplementationType::class, $test);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $testCount = $this->testRepository->getCountUserTestsOlderThen($this->getUser(), $test->getAlgorithm(), new \DateTime('-1 hour'));

            if ($testCount[0] >= $_ENV['IMPLEMENTATION_PER_HOUR'] && !$this->isGranted('ROLE_ADMIN')) {
                $this->addFlash('danger', "You've send too many implementations. Please wait a moment to be able to add additional ones.");

                return $this->render('dijkstra/create.html.twig', [
                    'form' => $form
                ]);
            }

            $test->setUuid(Uuid::v7());
            $test->setUser($this->getUser());
            $test->setToken($this->stringGenerator->getToken(Test::TOKEN_LENGTH));

            /** @var UploadedFile $file */
            $file = ($request->files->get('dijkstra_testing_implementation')['File']);
            if ($file) {
                if ($file->getClientMimeType() !== Test::MINE_TYPES[$test->getLanguage()]) {
                    throw new HttpException(Response::HTTP_NOT_FOUND, 'Expansion of the uploaded file is not supported.');
                }

                $file->move($this->parameterBag->get('uploads_dir_Dijkstra').$test->getUuid(), 'userDijkstra.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_Dijkstra').'main.py',
                    $this->parameterBag->get('uploads_dir_Dijkstra').$test->getUuid().'/main.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_Dijkstra').'computationalComplexityMain.py',
                    $this->parameterBag->get('uploads_dir_Dijkstra').$test->getUuid().'/computationalComplexityMain.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_Dijkstra').'chart.py',
                    $this->parameterBag->get('uploads_dir_Dijkstra').$test->getUuid().'/chart.py');
            }
            $this->testRepository->save($test);

            $this->messageBus->dispatch(new DijkstraImplementationTesting($test));
            $this->addFlash('success', 'Your algorithm implementation has been added to the overview. This may take a while.');

            return $this->redirectToRoute('app_home');
        }

        return $this->render('dijkstra/create.html.twig', [
            'form' => $form
        ]);
    }
}
