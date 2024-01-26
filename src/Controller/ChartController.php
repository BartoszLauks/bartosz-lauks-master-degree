<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\ResponseHeaderBag;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\Routing\Annotation\Route;

class ChartController extends AbstractController
{
    public function __construct(
        private readonly ParameterBagInterface $parameterBag
    ) {}

    #[Route('/chart/{algorithm}/{uuid}', name: 'app_chart')]
    public function index(string $algorithm, string $uuid): Response
    {
        $file = $this->getChartFile($algorithm, $uuid);
        $response = new Response();
        $disposition = $response->headers->makeDisposition(ResponseHeaderBag::DISPOSITION_INLINE, 'chart.png');
        $response->headers->set('Content-Disposition', $disposition);
        $response->headers->set('Content-Type', 'image/png');
        try {
            $image = file_get_contents($file);
        } catch (\Exception $exception) {
            $response->setStatusCode(404);

            return $response;
        }
        $response->setContent($image);

        return $response;
    }

    private function getChartFile(string $algorithm, string $uuid): string
    {
        $path = match ($algorithm) {
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

        return sprintf('%s%s%s', $path, $uuid, '/chart.png');
    }
}
