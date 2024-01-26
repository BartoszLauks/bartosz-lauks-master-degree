<?php

namespace App\Controller\Admin;

use App\Entity\ChatMessages;
use App\Entity\ComputationalComplexity;
use App\Entity\Gender;
use App\Entity\ResetPasswordRequest;
use App\Entity\Test;
use App\Entity\User;
use EasyCorp\Bundle\EasyAdminBundle\Config\Dashboard;
use EasyCorp\Bundle\EasyAdminBundle\Config\MenuItem;
use EasyCorp\Bundle\EasyAdminBundle\Controller\AbstractDashboardController;
use EasyCorp\Bundle\EasyAdminBundle\Router\AdminUrlGenerator;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class DashboardController extends AbstractDashboardController
{
    #[Route('/admin', name: 'app_admin')]
    public function index(): Response
    {
         $adminUrlGenerator = $this->container->get(AdminUrlGenerator::class);
         return $this->redirect($adminUrlGenerator->setController(TestCrudController::class)->generateUrl());
    }

    public function configureDashboard(): Dashboard
    {
        return Dashboard::new()
            ->setTitle('Bartosz-Lauks-master-degree')
            ->setFaviconPath('https://cdn-icons-png.flaticon.com/512/2103/2103633.png')
            ;
    }

    public function configureMenuItems(): iterable
    {
        yield MenuItem::linkToRoute('Home', 'fa-solid fa-house', 'app_home');
        yield MenuItem::linkToCrud('Test', 'fa-solid fa-file-lines', Test::class);
        yield MenuItem::linkToCrud('Computational Complexity', 'fa-solid fa-hourglass-half', ComputationalComplexity::class);
        yield MenuItem::linkToCrud('Users', 'fa fa-user', User::class);
        yield MenuItem::linkToCrud('Gender', 'fa-solid fa-venus-mars', Gender::class);
        yield MenuItem::linkToCrud('Reset Password', 'fa-solid fa-key', ResetPasswordRequest::class);
        yield MenuItem::linkToCrud('Chat Messages', 'fa-solid fa-message', ChatMessages::class);
    }
}
