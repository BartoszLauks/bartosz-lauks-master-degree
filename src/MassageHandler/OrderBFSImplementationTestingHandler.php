<?php

declare(strict_types=1);

namespace App\MassageHandler;

use App\Entity\Test;
use App\Enum\OutputFlags;
use App\Massage\BFSImplementationTesting;
use App\Repository\TestRepository;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
readonly class OrderBFSImplementationTestingHandler
{
    public function __construct(
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem,
        private readonly ParameterBagInterface $parameterBag
    ) {
    }

    public function __invoke(BFSImplementationTesting $algorithmToTest): void
    {
        $uuid = $algorithmToTest->getTest()->getUuid();
        $test = $this->testRepository->findOneBy([
            'uuid' => $uuid
        ]);

        if ($this->isTestDone($test)) {
            $testPath = sprintf('%s%s', $this->parameterBag->get('uploads_dir_BFS'), $test->getUuid());

            if ($this->runMainTest($testPath, $test)) {
                if ($this->runComplexityTest($testPath, $test)) {
                    $test->setStatus(Test::STATUS['VERIFIED']);
                    $test->setResponse('Testing completed successfully.');
                }
            }

            $this->testRepository->save($test);
        }
    }

    private function getOutputTestPath(string $testPath): string
    {
        return sprintf('%s%s', $testPath, '/output.txt');
    }

    private function checkOutputTestFileExist(string $testPath, Test $test): bool
    {
        if ($this->filesystem->exists($this->getOutputTestPath($testPath))) {
            return true;
        }

        $test->setStatus(Test::STATUS['ERROR']);
        $test->setResponse("Your implementation's main test result was not received. Contact with administrator.");

        return false;
    }

    private function checkForErrorFlag(Test $test, string $fileContent): bool
    {
        $errorFlag = sprintf('%s %s', $test->getToken(), OutputFlags::ERROR->flag());
        if (is_int(strpos($fileContent, $errorFlag))) {
            $test->setStatus(Test::STATUS['ERROR']);
            $test->setResponse('An error was encountered.');
            return true;
        }

        return false;
    }

    private function checkStartComplexityTestFlagExisting(Test $test, string $fileContent): bool
    {
        $startComplexityTestFlag = sprintf('%s %s',
            $test->getToken(), OutputFlags::START_COMPUTATIONAL_COMPLEXITY_TEST->flag());
        if (!is_int(strpos($fileContent, $startComplexityTestFlag))) {
            $test->setStatus(Test::STATUS['ERROR']);
            $test->setResponse('An error was encountered when starting the computational complexity test.');
            return true;
        }

        return false;
    }

    private function checkMemoryUsageExisting(Test $test, string $fileContent): bool
    {
        $phrase = sprintf('%s %s', $test->getToken(), OutputFlags::PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION->flag());
        if (preg_match('/' . $phrase . '(\d+)/', $fileContent, $matches)) {
            if ($matches[1]) {
                $test->setResult(intval($matches[1]));
            }
        } else {
            $test->setStatus(Test::STATUS['ERROR']);
            $test->setResponse('No memory usage results from the complexity test were found.');
            return true;
        }

        return false;
    }

    private function isTestDone(Test $test): bool
    {
        return $test->getStatus() !== Test::STATUS['VERIFIED'] && $test->getStatus() !== Test::STATUS['ERROR'];
    }
    private function runMainTest(string $testPath, Test $test): bool
    {
        exec(sprintf('python %s/main.py %s > %s/output.txt', $testPath, $test->getToken(), $testPath));
        $mainTestPath = $this->getOutputTestPath($testPath);

        if ($this->checkOutputTestFileExist($testPath, $test)) {
            $fileContent = file_get_contents($mainTestPath);
            if ($this->checkForErrorFlag($test, $fileContent)) {
                return false;
            }
        }

        return true;
    }

    private function runComplexityTest(string $testPath, Test $test): bool
    {
        exec(sprintf('python %s/computationalComplexityMain.py %s >> %s/output.txt',
            $testPath, $test->getToken(), $testPath));
        $mainTestPath = $this->getOutputTestPath($testPath);

        if ($this->checkOutputTestFileExist($testPath, $test)) {
            $fileContent = file_get_contents($mainTestPath);
            if ($this->checkForErrorFlag($test, $fileContent)) {
                return false;
            }
            if ($this->checkStartComplexityTestFlagExisting($test, $fileContent)) {
                return false;
            }
            if ($this->checkMemoryUsageExisting($test, $fileContent)) {
                return false;
            }
        }

        return true;
    }
//    public function __invoke(BFSImplementationTesting $algorithmToTest): void
//    {
//        $uuid = $algorithmToTest->getTest()->getUuid();
//        $test = $this->testRepository->findOneBy([
//            'uuid' => $uuid
//        ]);
//
//        if ($test->getStatus() !== Test::STATUS['VERIFIED'] && $test->getStatus() !== Test::STATUS['ERROR']) {
//            $token = $test->getToken();
//            $testPath = sprintf('%s%s',  $this->parameterBag->get('uploads_dir_BFS'), $test->getUuid());
//            exec(sprintf('python %s/main.py %s > %s/output.txt', $testPath, $test->getToken(), $testPath));
//            $mainTestPath = sprintf('%s%s', $testPath, '/output.txt');
//            if ($this->filesystem->exists($mainTestPath)) {
//                $fileContent = file_get_contents($mainTestPath);
//                $errorFlag = sprintf('%s %s', $token, OutputFlags::ERROR->flag());
//                if (is_int(strpos($fileContent, $errorFlag))) {
//                    $test->setStatus(Test::STATUS['ERROR']);
//                    $test->setResponse('An error was encountered.');
//                } else {
//                    exec(sprintf('python %s/computationalComplexityMain.py %s >> %s/output.txt',
//                        $testPath, $test->getToken(), $testPath));
//                    $fileContent = file_get_contents($mainTestPath);
//                    if (is_int(strpos($fileContent, $errorFlag))) {
//                        $test->setStatus(Test::STATUS['ERROR']);
//                        $test->setResponse('An error was encountered.');
//                    } else {
//                        $startComplexityTestFlag = sprintf('%s %s',
//                            $token, OutputFlags::START_COMPUTATIONAL_COMPLEXITY_TEST->flag());
//                        if (!is_int(strpos($fileContent, $startComplexityTestFlag))) {
//                            $test->setStatus(Test::STATUS['ERROR']);
//                            $test->setResponse('An error was encountered when starting the computational complexity test.');
//                        } else {
//                            $phrase = sprintf('%s %s', $token, OutputFlags::PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION->flag());
//                            if (preg_match('/' . $phrase . '(\d+)/', $fileContent, $matches)) {
//                                if ($matches[1]) {
//                                    $test->setResult(intval($matches[1]));
//                                }
//                            }
//                            $test->setStatus(Test::STATUS['VERIFIED']);
//                            $test->setResponse('Testing completed successfully.');
//                        }
//                    }
//                }
//            } else {
//                $test->setStatus(Test::STATUS['ERROR']);
//                $test->setResponse("Your implementation's main test result was not received. Contact with administrator.");
//            }
//            $this->testRepository->save($test);
//        }
//    }
}
