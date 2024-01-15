<?php

namespace App\Entity;

use App\Repository\ComputationalComplexityRepository;
use DateTimeImmutable;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\HasLifecycleCallbacks()]
#[ORM\Entity(repositoryClass: ComputationalComplexityRepository::class)]
class ComputationalComplexity
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255)]
    #[Assert\NotBlank()]
    #[Assert\Choice(choices: Test::ALGORITHM, message: 'Choose a valid algorithm.')]
    private ?string $algorithm = null;

    #[ORM\Column(length: 255)]
    #[Assert\NotBlank()]
    #[Assert\Choice(choices: Test::LANGUAGE, message: 'Not supported language.')]
    private ?string $language = null;

    #[ORM\Column]
    #[Assert\NotBlank()]
    private ?float $timeComplexity = null;

    #[ORM\Column]
    #[Assert\NotBlank()]
    private ?int $memoryComplexity = null;

    #[ORM\Column]
    private ?\DateTimeImmutable $createdAt = null;

    #[ORM\Column]
    private ?\DateTimeImmutable $updatedAt = null;



    public function getId(): ?int
    {
        return $this->id;
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

    public function getLanguage(): ?string
    {
        return $this->language;
    }

    public function setLanguage(string $language): static
    {
        $this->language = $language;

        return $this;
    }

    public function getTimeComplexity(): ?float
    {
        return $this->timeComplexity;
    }

    public function setTimeComplexity(float $timeComplexity): static
    {
        $this->timeComplexity = $timeComplexity;

        return $this;
    }

    public function getMemoryComplexity(): ?int
    {
        return $this->memoryComplexity;
    }

    public function setMemoryComplexity(int $memoryComplexity): static
    {
        $this->memoryComplexity = $memoryComplexity;

        return $this;
    }

    public function getCreatedAt(): ?\DateTimeImmutable
    {
        return $this->createdAt;
    }

    public function setCreatedAt(\DateTimeImmutable $createdAt): static
    {
        $this->createdAt = $createdAt;

        return $this;
    }

    public function getUpdatedAt(): ?\DateTimeImmutable
    {
        return $this->updatedAt;
    }

    public function setUpdatedAt(\DateTimeImmutable $updatedAt): static
    {
        $this->updatedAt = $updatedAt;

        return $this;
    }

    #[ORM\PrePersist()]
    public function initializationDataTime(): static
    {
        $this->createdAt = new DateTimeImmutable('now');
        $this->updatedAt = new DateTimeImmutable('now');

        return $this;
    }

    #[ORM\PreUpdate]
    public function updateTimestamp(): static
    {
        $this->updatedAt = new DateTimeImmutable('now');

        return $this;
    }
}
