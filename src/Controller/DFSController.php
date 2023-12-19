<?php

namespace App\Controller;

use App\Entity\Test;
use App\Enum\OutputFlags;
use App\Form\DFSTestingImplementationType;
use App\Massage\AlgorithmToTest;
use App\Massage\DFSImplementationTesting;
use App\MassageHandler\OrderDFSImplementationTestingHandler;
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

#[Route('/dfs', name: 'app_dfs_algorithm_')]
class DFSController extends AbstractController
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
        return $this->render('dfs/index.html.twig', [
            'controller_name' => 'DFSController',
        ]);
    }

    #[Route('/create', name: 'create')]
    public function createTest(Request $request): Response
    {
        $test = new Test();

        $form = $this->createForm(DFSTestingImplementationType::class, $test);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $test->setUuid(Uuid::v7());
            $test->setUser($this->getUser());
            $test->setToken($this->stringGenerator->getToken(Test::TOKEN_LENGTH));

            /** @var UploadedFile $file */
            $file = ($request->files->get('dfs_testing_implementation')['File']);
            if ($file) {
                if ($file->getClientMimeType() !== Test::MINE_TYPES[$test->getLanguage()]) {
                    throw new HttpException(Response::HTTP_NOT_FOUND, 'Expansion of the uploaded file is not supported.');
                }

                $file->move($this->parameterBag->get('uploads_dir_DFS').$test->getUuid(), 'userDFS.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_DFS').'main.py', $this->parameterBag->get('uploads_dir_DFS').$test->getUuid().'/main.py');
                $this->filesystem->copy($this->parameterBag->get('algorithms_dir_DFS').'computationalComplexityMain.py', $this->parameterBag->get('uploads_dir_DFS').$test->getUuid().'/computationalComplexityMain.py');
            }
            $this->testRepository->save($test);

            $this->messageBus->dispatch(new DFSImplementationTesting($test));
            $this->addFlash('success', 'Your algorithm implementation has been added to the overview. This may take a while.');

            return $this->redirectToRoute('app_home');
        }

        return $this->render('dfs/create.html.twig', [
           'form' => $form
        ]);
    }

    #[Route('/test')]
    public function test()
    {
        $test = $this->testRepository->find(35);

        if ($test->getStatus() !== 'VERIFIED' && $test->getStatus() !== 'ERROR') {
            $token = $test->getToken();
            $testPath = sprintf('%s%s',  $this->parameterBag->get('uploads_dir_DFS'), $test->getUuid());
            exec(sprintf('python %s/main.py %s > %s/output.txt', $testPath, $test->getToken(), $testPath));
            $mainTestPath = sprintf('%s%s', $testPath, '/output.txt');
            if ($this->filesystem->exists($mainTestPath)) {
                $fileContent = file_get_contents($mainTestPath);
                $errorFlag = sprintf('%s %s', $token, OutputFlags::ERROR->flag());
                if (is_int(strpos($fileContent, $errorFlag))) {
                    $test->setStatus(OutputFlags::ERROR->flag());
                    $test->setResponse('An error was encountered.');
                } else {
                    exec(sprintf('python %s/computationalComplexityMain.py %s >> %s/output.txt', $testPath, $test->getToken(), $testPath));
                    if (is_int(strpos($fileContent, $errorFlag))) {
                        $test->setStatus(OutputFlags::ERROR->flag());
                        $test->setResponse('An error was encountered.');
                    } else {
                        $fileContent = file_get_contents($mainTestPath);
                        $phrase = sprintf('%s %s', $token, OutputFlags::PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION->flag());
                        if (preg_match('/' . $phrase . '(\d+)/', $fileContent, $matches)) {
                            if ($matches[1]) {
                                $test->setResult(intval($matches[1]));
                            }
                        }
                        $test->setStatus(Test::STATUS['']);
                        $test->setResponse('Testing completed successfully.');
                    }
                }
            } else {
                $test->setStatus(OutputFlags::ERROR->flag());
                $test->setResponse("Your implementation's main test result was not received. Contact your administrator.");
            }
            $this->testRepository->save($test);
        }

        dd("Miss");
    }
}
