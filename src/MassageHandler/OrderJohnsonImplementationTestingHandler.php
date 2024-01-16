<?php

declare(strict_types=1);

namespace App\MassageHandler;

use App\Entity\ComputationalComplexity;
use App\Entity\Test;
use App\Enum\OutputFlags;
use App\Massage\JohnsonImplementationTesting;
use App\Repository\ComputationalComplexityRepository;
use App\Repository\TestRepository;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBagInterface;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
readonly class OrderJohnsonImplementationTestingHandler
{
    public function __construct(
        private readonly TestRepository $testRepository,
        private readonly Filesystem $filesystem,
        private readonly ParameterBagInterface $parameterBag,
        private readonly ComputationalComplexityRepository $complexityRepository
    ) {
    }

    public function __invoke(JohnsonImplementationTesting $algorithmToTest): void
    {
        $uuid = $algorithmToTest->getTest()->getUuid();
        $test = $this->testRepository->findOneBy([
            'uuid' => $uuid
        ]);

        if ($this->isTestDone($test)) {
            $testPath = sprintf('%s%s', $this->parameterBag->get('uploads_dir_Johnson'), $test->getUuid());

            $complexity = $this->getComputationalComplexity($test);

            if ($this->runMainTest($testPath, $test, $complexity)) {
                if ($this->runComplexityTest($testPath, $test, $complexity)) {
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
    private function runMainTest(string $testPath, Test $test, ComputationalComplexity $complexity): bool
    {
        exec(sprintf('python %s/main.py %s %s > %s/output.txt',
            $testPath, $test->getToken(), $complexity->getTimeComplexity(), $testPath));
        $mainTestPath = $this->getOutputTestPath($testPath);

        if ($this->checkOutputTestFileExist($testPath, $test)) {
            $fileContent = file_get_contents($mainTestPath);
            if ($this->checkForErrorFlag($test, $fileContent)) {
                return false;
            }
        }

        return true;
    }

    private function runComplexityTest(string $testPath, Test $test, ComputationalComplexity $complexity): bool
    {
        exec(sprintf('python %s/computationalComplexityMain.py %s %s %s >> %s/output.txt',
            $testPath, $test->getToken(), $complexity->getTimeComplexity(), $complexity->getMemoryComplexity(), $testPath));
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

    private function getComputationalComplexity(Test $test) : ComputationalComplexity
    {
        $complexity = $this->complexityRepository->findOneBy([
            'algorithm' => $test->getAlgorithm(),
            'language' => $test->getLanguage()
        ]);

        if (!$complexity) {
            $complexityPath = sprintf('%s%s', $this->parameterBag->get('algorithms_dir_Johnson'), 'computationalComplexity');

            $complexity = new ComputationalComplexity();
            $complexity->setAlgorithm($test->getAlgorithm());
            $complexity->setLanguage($test->getLanguage());
            $complexity->setMemoryComplexity(intval(exec(sprintf('python %s/memoryComplexity.py', $complexityPath))));

            $times = [];
            for ($i = 0; $i <= 10; $i++) {
                $times[] = floatval(exec(sprintf('python %s/timeComplexity.py', $complexityPath)));
            }

            $complexity->setTimeComplexity(round(array_sum($times) / count($times)));

            $this->complexityRepository->save($complexity);
        }

        return $complexity;
    }
}
