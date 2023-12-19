<?php

declare(strict_types=1);

namespace App\MassageHandler;

use App\Entity\Test;
use App\Enum\OutputFlags;
use App\Massage\KruskalImplementationTesting;
use App\Repository\TestRepository;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
readonly class OrderKruskalImplementationTestingHandler
{
    public function __construct(
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem,
        private readonly ParameterBagInterface $parameterBag
    ) {
    }

    public function __invoke(KruskalImplementationTesting $algorithmToTest): void
    {
        $uuid = $algorithmToTest->getTest()->getUuid();
        $test = $this->testRepository->findOneBy([
            'uuid' => $uuid
        ]);

        if ($test->getStatus() !== Test::STATUS['VERIFIED'] && $test->getStatus() !== Test::STATUS['ERROR']) {
            $token = $test->getToken();
            $testPath = sprintf('%s%s',  $this->parameterBag->get('uploads_dir_Kruskal'), $test->getUuid());
            exec(sprintf('python %s/main.py %s > %s/output.txt', $testPath, $test->getToken(), $testPath));
            $mainTestPath = sprintf('%s%s', $testPath, '/output.txt');
            if ($this->filesystem->exists($mainTestPath)) {
                $fileContent = file_get_contents($mainTestPath);
                $errorFlag = sprintf('%s %s', $token, OutputFlags::ERROR->flag());
                if (is_int(strpos($fileContent, $errorFlag))) {
                    $test->setStatus(Test::STATUS['ERROR']);
                    $test->setResponse('An error was encountered.');
                } else {
                    exec(sprintf('python %s/computationalComplexityMain.py %s >> %s/output.txt', $testPath, $test->getToken(), $testPath));
                    if (is_int(strpos($fileContent, $errorFlag))) {
                        $test->setStatus(Test::STATUS['VERIFIED']);
                        $test->setResponse('An error was encountered.');
                    } else {
                        $fileContent = file_get_contents($mainTestPath);
                        $phrase = sprintf('%s %s', $token, OutputFlags::PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION->flag());
                        if (preg_match('/' . $phrase . '(\d+)/', $fileContent, $matches)) {
                            if ($matches[1]) {
                                $test->setResult(intval($matches[1]));
                            }
                        }
                        $test->setStatus(Test::STATUS['VERIFIED']);
                        $test->setResponse('Testing completed successfully.');
                    }
                }
            } else {
                $test->setStatus(Test::STATUS['ERROR']);
                $test->setResponse("Your implementation's main test result was not received. Contact your administrator.");
            }
            $this->testRepository->save($test);
        }


    }
}
