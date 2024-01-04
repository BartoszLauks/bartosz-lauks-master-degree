<?php

namespace App\Controller;

use App\Repository\TestRepository;
use App\Repository\UserRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/search', name: 'app_')]
class SearchController extends AbstractController
{
    public function __construct(
      private readonly UserRepository $userRepository
    ) {}

    #[Route('', name: 'search')]
    public function index(Request $request): Response
    {
        $offset = max(0, $request->query->getInt('offset', 0));

        $text = $request->query->get("search-text");
        $paginator = $this->userRepository->searchUser($text, $offset);
        return $this->render('search/index.html.twig', [
            'users' => $paginator,
            'previous' => $offset - TestRepository::PAGINATOR_PER_PAGE,
            'next' => min(count($paginator), $offset + TestRepository::PAGINATOR_PER_PAGE),
        ]);
    }
}
