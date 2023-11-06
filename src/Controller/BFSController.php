<?php

namespace App\Controller;

use App\Entity\Test;
use App\Form\BFSTestingImplementationType;
use App\Massage\AlgorithmToTest;
use App\Repository\TestRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Uid\Uuid;

#[Route('/bfs', name: 'app_bfs_algorithm_')]
class BFSController extends AbstractController
{
    public function __construct(
        private readonly ParameterBagInterface $parameterBag,
        private readonly MessageBusInterface $messageBus,
        private readonly TestRepository $testRepository
    ) {
    }

    #[Route('/', name: 'index')]
    public function index(): Response
    {
        return $this->render('bfs/index.html.twig');
    }

    #[Route('/create', name: 'create')]
    public function createTest(Request $request): Response
    {
        $test = new Test();

        $form = $this->createForm(BFSTestingImplementationType::class, $test);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $test->setUuid(Uuid::v7());
            $test->setUser($this->getUser());
            $file = ($request->files->get('bfs_testing_implementation')['File']);
            if ($file) {
                $file->move($this->parameterBag->get('uploads_dir_BFS').$test->getUuid(), $file->getClientOriginalName());
            }

            $this->testRepository->save($test);

            $this->messageBus->dispatch(new AlgorithmToTest($test));
            return $this->redirectToRoute('app_home');
        }

        return $this->render('bfs/create.html.twig', [
            'form' => $form
        ]);
    }

    #[Route('/test')]
    public function test()
    {
        dd($this->testRepository->find(1)->getUuid()->jsonSerialize());
    }
}
