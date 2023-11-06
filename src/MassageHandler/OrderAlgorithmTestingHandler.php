<?php

declare(strict_types=1);

namespace App\MassageHandler;

use App\Massage\AlgorithmToTest;
use App\Repository\TestRepository;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
readonly class OrderAlgorithmTestingHandler
{
    public function __construct(
        private readonly TestRepository $testRepository
    ) {
    }

    public function __invoke(AlgorithmToTest $algorithmToTest): void
    {
        $uuid = $algorithmToTest->getTest()->getUuid();
        $test = $this->testRepository->findOneBy([
            'uuid' => $uuid
        ]);
        $test->setStatus('CHECKED');
        $test->setResponse("Test");
        $this->testRepository->save($test);

        $test->setStatus('VERIFIED');
        $this->testRepository->save($test);
    }
}
