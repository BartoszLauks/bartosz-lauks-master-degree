<?php

namespace App\Command;

use App\Massage\BellmanFordImplementationTesting;
use App\Massage\BFSImplementationTesting;
use App\Massage\DFSImplementationTesting;
use App\Massage\DijkstraImplementationTesting;
use App\Massage\FleuryImplementationTesting;
use App\Massage\FloydWarshallImplementationTesting;
use App\Massage\JohnsonImplementationTesting;
use App\Massage\KruskalImplementationTesting;
use App\Massage\PrimImplementationTesting;
use App\Massage\TopologicalSortingImplementationTesting;
use App\Repository\TestRepository;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Style\SymfonyStyle;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\Messenger\MessageBusInterface;

#[AsCommand(
    name: 'app:AddWaitingImplementationToTesting',
    description: 'Add all waiting implementations to the queue',
)]
class AddWaitingImplementationToTestingCommand extends Command
{
    public function __construct(
        private readonly MessageBusInterface $messageBus,
        private readonly TestRepository $testRepository,
    ) {
        parent::__construct();
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $io = new SymfonyStyle($input, $output);

        $tests = $this->testRepository->findBy(['status' => 'WAITING']);

        foreach ($tests as $test) {
            match ($test->getAlgorithm()) {
                'BFS' => $this->messageBus->dispatch(new BFSImplementationTesting($test)),
                'DFS' => $this->messageBus->dispatch(new DFSImplementationTesting($test)),
                'Dijkstra' => $this->messageBus->dispatch(new DijkstraImplementationTesting($test)),
                'Kruskal' => $this->messageBus->dispatch(new KruskalImplementationTesting($test)),
                'Prim' => $this->messageBus->dispatch(new PrimImplementationTesting($test)),
                'TopologicalSorting' => $this->messageBus->dispatch(new TopologicalSortingImplementationTesting($test)),
                'BellmanFord' => $this->messageBus->dispatch(new BellmanFordImplementationTesting($test)),
                'FloydWarshall' => $this->messageBus->dispatch(new FloydWarshallImplementationTesting($test)),
                'Johnson' => $this->messageBus->dispatch(new JohnsonImplementationTesting($test)),
                'Fleury' => $this->messageBus->dispatch(new FleuryImplementationTesting($test)),
                default => throw new HttpException(404, 'This algorithm is not supported.')
            };
        }
        $io->success('Successfully added everyone waiting for testing to the queue. \o/');

        return Command::SUCCESS;
    }
}
