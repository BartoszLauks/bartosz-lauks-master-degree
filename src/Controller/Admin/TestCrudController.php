<?php

namespace App\Controller\Admin;

use App\Entity\Test;
use EasyCorp\Bundle\EasyAdminBundle\Config\Action;
use EasyCorp\Bundle\EasyAdminBundle\Config\Actions;
use EasyCorp\Bundle\EasyAdminBundle\Config\Crud;
use EasyCorp\Bundle\EasyAdminBundle\Config\Filters;
use EasyCorp\Bundle\EasyAdminBundle\Controller\AbstractCrudController;
use EasyCorp\Bundle\EasyAdminBundle\Field\ChoiceField;
use EasyCorp\Bundle\EasyAdminBundle\Field\DateTimeField;
use EasyCorp\Bundle\EasyAdminBundle\Field\IdField;
use EasyCorp\Bundle\EasyAdminBundle\Field\IntegerField;
use EasyCorp\Bundle\EasyAdminBundle\Field\TextEditorField;
use EasyCorp\Bundle\EasyAdminBundle\Field\TextField;
use EasyCorp\Bundle\EasyAdminBundle\Filter\BooleanFilter;
use EasyCorp\Bundle\EasyAdminBundle\Filter\ChoiceFilter;
use EasyCorp\Bundle\EasyAdminBundle\Filter\DateTimeFilter;
use EasyCorp\Bundle\EasyAdminBundle\Filter\NumericFilter;
use EasyCorp\Bundle\EasyAdminBundle\Filter\TextFilter;

class TestCrudController extends AbstractCrudController
{
    public static function getEntityFqcn(): string
    {
        return Test::class;
    }

    public function configureFields(string $pageName): iterable
    {
        return [
            IdField::new('id')->hideOnForm(),
            TextField::new('algorithm')->hideOnForm(),
            TextField::new('type')->hideOnForm(),
            ChoiceField::new('status')
                ->allowMultipleChoices(false)
                ->setChoices([
                    'WAITING' => 'WAITING',
                    'CHECKED' => 'CHECKED',
                    'VERIFIED' => 'VERIFIED',
                    'ERROR' => 'ERROR'
                ]),
            IntegerField::new('result'),
            TextEditorField::new('response'),
            TextField::new('language')->hideOnForm(),
            TextField::new('uuid')->hideOnForm(),
            TextField::new('token')->hideOnForm()->setMaxLength(5),
            DateTimeField::new('updatedAt')->hideOnForm(),
            DateTimeField::new('createdAt')->hideOnForm(),
        ];
    }

    public function configureActions(Actions $actions): Actions
    {
        return $actions
            ->add(Crud::PAGE_INDEX, Action::DETAIL)
            ->remove(Crud::PAGE_INDEX, Action::NEW)
            ;
    }

    public function configureFilters(Filters $filters): Filters
    {
        return $filters
            ->add(NumericFilter::new('id'))
            ->add(TextFilter::new('algorithm'))
            ->add(TextFilter::new('type'))
            ->add(ChoiceFilter::new('status')
                ->setChoices([
                    'WAITING' => 'WAITING',
                    'CHECKED' => 'CHECKED',
                    'VERIFIED' => 'VERIFIED',
                    'ERROR' => 'ERROR'
                ]))
            ->add(NumericFilter::new('result'))
            ->add(TextFilter::new('response'))
            ->add(TextFilter::new('language'))
            ->add(DateTimeFilter::new('updatedAt'))
            ->add(DateTimeFilter::new('createdAt'))
            ;
    }
}
