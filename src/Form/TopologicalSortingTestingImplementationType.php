<?php

namespace App\Form;

use App\Entity\Test;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\FileType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class TopologicalSortingTestingImplementationType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('Algorithm', TextType::class, [
                'data' => 'TopologicalSorting',
                'attr' => ['readonly' => true]
            ])
            ->add('Type')
            ->add('Language', TextType::class, [
                'data' => 'PYTHON',
                'attr' => ['readonly' => true]
            ])
            ->add('File',FileType::class, [
                'mapped' => false,
            ])
            ->add('Test',SubmitType::class)
        ;
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Test::class,
        ]);
    }
}
