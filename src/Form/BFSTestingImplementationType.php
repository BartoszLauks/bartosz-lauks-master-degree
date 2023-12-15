<?php

namespace App\Form;

use App\Entity\Test;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Component\Form\Extension\Core\Type\FileType;
use Symfony\Component\Form\Extension\Core\Type\HiddenType;
use Symfony\Component\Form\Extension\Core\Type\SubmitType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class BFSTestingImplementationType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('Algorithm', TextType::class, [
                'data' => 'BFS',
                'attr' => ['readonly' => true]
//                'disabled' => true
            ])
//            ->add('Algorithm', ChoiceType::class, [
//                'choices' => array_combine(Test::ALGORITHM, Test::ALGORITHM)
//            ])
            ->add('Type')
            ->add('Language', TextType::class, [
                'data' => 'PYTHON',
                'attr' => ['readonly' => true]
//                'disabled' => true,
//                'empty_data' => 'John Doe'
            ])
//            ->add('Language', ChoiceType::class, [
//                'choices' => array_combine(TEST::LANGUAGE, TEST::LANGUAGE)
//            ])
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
