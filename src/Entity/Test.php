<?php

namespace App\Entity;

use App\Repository\TestRepository;
use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Uid\Uuid;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Constraints\NotBlank;

#[ORM\Entity(repositoryClass: TestRepository::class)]
class Test
{
    const ALGORITHM = ['BFS', 'DFS', 'Dijkstra'];
    const STATUS = ['WAITING', 'CHECKED', 'VERIFIED', 'ERROR'];

    const LANGUAGE = ['PYTHON', 'C++', 'JAVA'];

    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\ManyToOne(inversedBy: 'tests')]
    #[ORM\JoinColumn(nullable: false)]
    private ?User $user = null;

    #[Assert\NotBlank()]
    #[Assert\Choice(choices: self::ALGORITHM, message: 'Choose a valid algorithm.')]
    #[ORM\Column(length: 255)]
    private ?string $algorithm = null;

    #[ORM\Column(length: 255)]
    private ?string $type = null;

    #[Assert\Choice(choices: self::STATUS, message: 'Unknown status')]
    #[ORM\Column(length: 255)]
    private string $status = 'WAITING';

    #[ORM\Column]
    private int $result = 0;

    #[ORM\Column(type: Types::TEXT)]
    private ?string $response = '';

    #[Assert\Choice(choices: self::LANGUAGE, message: 'Not supported language.')]
    #[ORM\Column(length: 255, nullable: true)]
    private ?string $language = null;

    #[Assert\Uuid]
    #[ORM\Column(type: 'uuid')]
    private Uuid $uuid;


    public function getId(): ?int
    {
        return $this->id;
    }

    public function getUser(): ?User
    {
        return $this->user;
    }

    public function setUser(?User $user): static
    {
        $this->user = $user;

        return $this;
    }

    public function getAlgorithm(): ?string
    {
        return $this->algorithm;
    }

    public function setAlgorithm(string $algorithm): static
    {
        $this->algorithm = $algorithm;

        return $this;
    }

    public function getType(): ?string
    {
        return $this->type;
    }

    public function setType(string $type): static
    {
        $this->type = $type;

        return $this;
    }

    public function getStatus(): ?string
    {
        return $this->status;
    }

    public function setStatus(string $status): static
    {
        $this->status = $status;

        return $this;
    }

    public function getResult(): ?int
    {
        return $this->result;
    }

    public function setResult(int $result): static
    {
        $this->result = $result;

        return $this;
    }

    public function getResponse(): ?string
    {
        return $this->response;
    }

    public function setResponse(string $response): static
    {
        $this->response = $response;

        return $this;
    }

    public function getLanguage(): ?string
    {
        return $this->language;
    }

    public function setLanguage(?string $language): static
    {
        $this->language = $language;

        return $this;
    }

    public function getUuid(): ?Uuid
    {
        return $this->uuid;
    }

    public function setUuid(Uuid $uuid): static
    {
        $this->uuid = $uuid;

        return $this;
    }

}
