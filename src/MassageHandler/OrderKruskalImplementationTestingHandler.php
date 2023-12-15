<?php

declare(strict_types=1);

namespace App\MassageHandler;

use App\Massage\DFSImplementationTesting;
use App\Massage\DijkstraImplementationTesting;
use App\Massage\KruskalImplementationTesting;
use App\Repository\TestRepository;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
readonly class OrderKruskalImplementationTestingHandler
{
    public function __construct(
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem
    ) {
    }

    public function __invoke(KruskalImplementationTesting $algorithmToTest): void
    {
        $uuid = $algorithmToTest->getTest()->getUuid();
        $test = $this->testRepository->findOneBy([
            'uuid' => $uuid
        ]);

        if ($test->getStatus() != 'WAITING') {
            $test->setStatus('CHECKED');
            $this->testRepository->save($test);

            //$this->filesystem->copy('//app/algorithms/BFS/main.py', '/public/'. $test->getUuid());

            $test->setStatus('VERIFIED');
            $this->testRepository->save($test);
        }


    }
}
