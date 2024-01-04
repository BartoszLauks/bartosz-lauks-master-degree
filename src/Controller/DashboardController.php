<?php

namespace App\Controller;

use App\Entity\Test;
use App\Entity\User;
use App\Repository\TestRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

#[Route('/dashboard', name: 'app_dashboard_')]
class DashboardController extends AbstractController
{
    public function __construct(
      private readonly TestRepository $testRepository,
      private readonly ParameterBagInterface $parameterBag,
        private readonly Filesystem $filesystem
    ) {}

    #[Route('/tests', name: 'tests')]
    public function myTests(Request $request): Response
    {
        $offset = max(0, $request->query->getInt('offset', 0));

        $paginator = $this->testRepository->getUserTestsPaginator($this->getUser(), $offset);

        return $this->render('dashboard/index.html.twig', [
            'tests' => $paginator,
            'previous' => $offset - TestRepository::PAGINATOR_PER_PAGE,
            'next' => min(count($paginator), $offset + TestRepository::PAGINATOR_PER_PAGE),
        ]);
    }

    #[Route('/tests/user/{uuid}', name: 'user_tests')]
    public function userTests(Request $request, User $user): Response
    {
        $offset = max(0, $request->query->getInt('offset', 0));

        $paginator = $this->testRepository->getUserTestsPaginator($user, $offset);

        return $this->render('dashboard/index.html.twig', [
            'tests' => $paginator,
            'previous' => $offset - TestRepository::PAGINATOR_PER_PAGE,
            'next' => min(count($paginator), $offset + TestRepository::PAGINATOR_PER_PAGE),
        ]);
    }

    #[IsGranted('ROLE_ADMIN')]
    #[Route('/all_tests', name: 'all_tests')]
    public function all(Request $request): Response
    {
        $offset = max(0, $request->query->getInt('offset', 0));

        $paginator = $this->testRepository->getAllTestsPaginator($this->getUser(), $offset);

        return $this->render('dashboard/index.html.twig', [
            'tests' => $paginator,
            'previous' => $offset - TestRepository::PAGINATOR_PER_PAGE,
            'next' => min(count($paginator), $offset + TestRepository::PAGINATOR_PER_PAGE),
        ]);
    }

    #[Route('/test/{uuid}', name: 'test')]
    public function test(Test $test): Response
    {
        $output = $this->getOutputTestingFile($test);
        if ($test->getStatus() === 'VERIFIED') {
            $percent = $this->testRepository->getPercentageOfTestsLowerResult($test->getResult(), $test->getAlgorithm());
        }

        return $this->render('dashboard/details.html.twig', [
            'test' => $test,
            'output' => $output,
            'percent' => $percent ?? null
        ]);
    }

    private function getOutputTestingFile(Test $test) : string
    {
       $path = match ($test->getAlgorithm()) {
           'BFS' => $this->parameterBag->get('uploads_dir_BFS'),
           'DFS' => $this->parameterBag->get('uploads_dir_DFS'),
           'Dijkstra' => $this->parameterBag->get('uploads_dir_Dijkstra'),
           'Kruskal' => $this->parameterBag->get('uploads_dir_Kruskal'),
           'Prim' => $this->parameterBag->get('uploads_dir_Prim'),
           'TopologicalSorting' => $this->parameterBag->get('uploads_dir_TopologicalSorting'),
           'BellmanFord' => $this->parameterBag->get('uploads_dir_BellmanFord'),
           'FloydWarshall' => $this->parameterBag->get('uploads_dir_FloydWarshall'),
           'Johnson' => $this->parameterBag->get('uploads_dir_Johnson'),
           'Fleury' => $this->parameterBag->get('uploads_dir_Fleury'),
           default => throw new HttpException(404, 'This algorithm is not supported.')
        };

       $path = sprintf('%s%s%s', $path, $test->getUuid(), '/output.txt');

       if (!$this->filesystem->exists($path)) {
           return 'File not exist';
       }

       $output = file_get_contents($path);
       $output = str_replace($test->getToken(), '', $output);
       return nl2br($output);
    }
}
