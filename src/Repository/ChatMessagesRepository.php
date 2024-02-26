<?php

namespace App\Repository;

use App\Entity\ChatMessages;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<ChatMessages>
 *
 * @method ChatMessages|null find($id, $lockMode = null, $lockVersion = null)
 * @method ChatMessages|null findOneBy(array $criteria, array $orderBy = null)
 * @method ChatMessages[]    findAll()
 * @method ChatMessages[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class ChatMessagesRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, ChatMessages::class);
    }

    public function save(ChatMessages $chatMessages, bool $flush = true): void
    {
        $this->_em->persist($chatMessages);
        if ($flush) {
            $this->_em->flush();
        }

    }

    public function flush() : void
    {
        $this->_em->flush();
    }

    public function remove(ChatMessages $chatMessages, bool $flush = true): void
    {
        $this->_em->remove($chatMessages);
        if ($flush) {
            $this->_em->flush();
        }
    }
}
