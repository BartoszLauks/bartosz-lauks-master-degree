<?php

namespace App\Repository;

use App\Entity\Test;
use App\Entity\User;
use DateTime;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\ORM\Tools\Pagination\Paginator;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Test>
 *
 * @method Test|null find($id, $lockMode = null, $lockVersion = null)
 * @method Test|null findOneBy(array $criteria, array $orderBy = null)
 * @method Test[]    findAll()
 * @method Test[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class TestRepository extends ServiceEntityRepository
{
    public const PAGINATOR_PER_PAGE = 10;

    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Test::class);
    }

    public function save(Test $test, bool $flush = true): void
    {
        $this->_em->persist($test);
        if ($flush) {
            $this->_em->flush();
        }

    }

    public function flush() : void
    {
        $this->_em->flush();
    }

    public function getUserTestsPaginator(User $user, int $offset): Paginator
    {
        $query = $this->createQueryBuilder('t')
            ->where('t.user = :user')
            ->setParameter('user', $user)
            ->orderBy('t.createdAt', 'DESC')
            ->setMaxResults(self::PAGINATOR_PER_PAGE)
            ->setFirstResult($offset)
            ->getQuery()
            ;

        return new Paginator($query);
    }

    public function getAllTestsPaginator(User $user, int $offset): Paginator
    {
        $query = $this->createQueryBuilder('t')
            ->orderBy('t.createdAt', 'DESC')
            ->setMaxResults(self::PAGINATOR_PER_PAGE)
            ->setFirstResult($offset)
            ->getQuery()
        ;

        return new Paginator($query);
    }

    public function getCountUserTestsOlderThen(User $user, string $algorithm, DateTime $time)
    {
        $query = $this->createQueryBuilder('t')
            ->select('count(t.id)')
            ->where('t.algorithm LIKE :algorithm')
            ->andWhere('t.createdAt >= :time')
            ->setParameter('algorithm', $algorithm)
            ->setParameter('time', $time)
            ->getQuery()
            ->getSingleColumnResult()
            ;
        return $query;
    }

    public function getPercentageOfTestsLowerResult(int $result, string $algorithm)
    {
        $conn = $this->getEntityManager()->getConnection();

        $sql = "select ROUND((count(*) / (select count(*) from test where status like 'VERIFIED' and algorithm like :algorithm )) * 100) as 'percent'
    from test t
where status like 'VERIFIED' and algorithm like :algorithm and result <= :result";

        $resultSet = $conn->executeQuery($sql, [
            'algorithm' => $algorithm,
            'result' => $result
        ]);

        return $resultSet->fetchOne();
    }
}
