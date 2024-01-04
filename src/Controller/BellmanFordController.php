<?php

namespace App\Controller;

use App\Entity\Test;
use App\Form\BellmanFordTestingImplementationType;
use App\Massage\BellmanFordImplementationTesting;
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

#[Route('/bellman_ford', name: 'app_bellman_ford_algorithm_')]
class BellmanFordController extends AbstractController
{
    public function __construct(
        private readonly ParameterBagInterface $parameterBag,
        private readonly MessageBusInterface $messageBus,
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem,
        private readonly RandomStringGenerator $stringGenerator
    ) {
    }

    #[Route('', name: 'index')]
    public function index(): Response
    {
        return $this->render('bellman_ford/index.html.twig');
    }

    #[Route('/create', name: 'create')]
    public function createTest(Request $request): Response
    {
        $test = new Test();

        $form = $this->createForm(BellmanFordTestingImplementationType::class, $test);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $test->setUuid(Uuid::v7());
            $test->setUser($this->getUser());
            $test->setToken($this->stringGenerator->getToken(Test::TOKEN_LENGTH));

            /** @var UploadedFile $file */
            $file = ($request->files->get('bellman_ford_testing_implementation')['File']);
            if ($file) {
                if ($file->getClientMimeType() !== Test::MINE_TYPES[$test->getLanguage()]) {
                    throw new HttpException(Response::HTTP_NOT_FOUND, 'Expansion of the uploaded file is not supported.');
                }

                $file->move($this->parameterBag->get('uploads_dir_BellmanFord').$test->getUuid(), 'userBellmanFord.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_BellmanFord').'main.py', $this->parameterBag->get('uploads_dir_BellmanFord').$test->getUuid().'/main.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_BellmanFord').'computationalComplexityMain.py', $this->parameterBag->get('uploads_dir_BellmanFord').$test->getUuid().'/computationalComplexityMain.py');
            }
            $this->testRepository->save($test);

            $this->messageBus->dispatch(new BellmanFordImplementationTesting($test));
            $this->addFlash('success', 'Your algorithm implementation has been added to the overview. This may take a while.');

            return $this->redirectToRoute('app_home');
        }

        return $this->render('bellman_ford/create.html.twig', [
            'form' => $form
        ]);
    }
}
