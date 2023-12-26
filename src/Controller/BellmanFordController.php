<?php

namespace App\Controller;

use App\Entity\Test;
use App\Form\BellmanFordTestingImplementationType;
use App\Massage\BellmanFordImplementationTesting;
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

    #[Route('/test')]
    public function test()
    {
        $test = $this->testRepository->find(28);

        if ($test->getStatus() !== 'VERIFIED' && $test->getStatus() !== 'ERROR') {
            $token = $test->getToken();
            $testPath = sprintf('%s%s',  $this->parameterBag->get('uploads_dir_BellmanFord'), $test->getUuid());
            exec(sprintf('python %s/main.py %s > %s/output.txt', $testPath, $test->getToken(), $testPath));
            $mainTestPath = sprintf('%s%s', $testPath, '/output.txt');
            if ($this->filesystem->exists($mainTestPath)) {
                $fileContent = file_get_contents($mainTestPath);
                $errorFlag = sprintf('%s %s', $token, 'ERROR');
                if (is_int(strpos($fileContent, $errorFlag))) {
                    $test->setStatus('ERROR');
                    $test->setResponse('An error was encountered.');
                } else {
                    exec(sprintf('python %s/computationalComplexityMain.py %s >> %s/output.txt', $testPath, $test->getToken(), $testPath));
                    if (is_int(strpos($fileContent, $errorFlag))) {
                        $test->setStatus('ERROR');
                        $test->setResponse('An error was encountered.');
                    } else {
                        $test->setStatus('VERIFIED');
                        $test->setResponse('Testing completed successfully.');
                    }

                }
            } else {
                $test->setStatus('ERROR');
                $test->setResponse("Your implementation's main test result was not received. Contact your administrator.");
            }
            $this->testRepository->save($test);
            dd("done");
        }

        dd("Miss");
    }
}
