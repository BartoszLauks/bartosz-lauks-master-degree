<?php

namespace App\Repository;

use App\Entity\ComputationalComplexity;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<ComputationalComplexity>
 *
 * @method ComputationalComplexity|null find($id, $lockMode = null, $lockVersion = null)
 * @method ComputationalComplexity|null findOneBy(array $criteria, array $orderBy = null)
 * @method ComputationalComplexity[]    findAll()
 * @method ComputationalComplexity[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class ComputationalComplexityRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, ComputationalComplexity::class);
    }

    public function save(ComputationalComplexity $computationalComplexity, bool $flush = true): void
    {
        $this->_em->persist($computationalComplexity);
        if ($flush) {
            $this->_em->flush();
        }

    }

    public function flush() : void
    {
        $this->_em->flush();
    }
}
