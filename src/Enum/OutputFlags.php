<?php

namespace App\Enum;

enum OutputFlags
{
    case FINISH_MAIN_TEST;
    case ERROR_USER_IMPLEMENTATION;
    case ERROR_ALGORITHM_RESULT;
    case BRUTE_FORCE_TEST_UNIT;
    case START_MAIN_TEST;
    case ERROR_TIME_OUT;
    case ERROR_IMPORT;
    case START_COMPUTATIONAL_COMPLEXITY_TEST;
    case PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION;
    case FINISH_COMPUTATIONAL_COMPLEXITY_TEST;
    case ERROR_MEMORY_LIMIT_EXCEEDED;
    case ERROR;
    case FINISH;

    public function flag(): string
    {
        return match ($this)
        {
            OutputFlags::FINISH_MAIN_TEST => 'FINISH MAIN TEST',
            OutputFlags::ERROR_USER_IMPLEMENTATION => 'ERROR USER IMPLEMENTATION',
            OutputFlags::ERROR_ALGORITHM_RESULT => 'ERROR ALGORITHM RESULT',
            OutputFlags::BRUTE_FORCE_TEST_UNIT => 'BRUTE FORCE TEST UNIT',
            OutputFlags::START_MAIN_TEST => 'START MAIN TEST',
            OutputFlags::ERROR_TIME_OUT => 'ERROR TIME OUT',
            OutputFlags::ERROR_IMPORT => 'ERROR IMPORT',
            OutputFlags::START_COMPUTATIONAL_COMPLEXITY_TEST => 'START COMPUTATIONAL COMPLEXITY TEST',
            OutputFlags::PEEK_MEMORY_USAGE_BY_YOUR_IMPLEMENTATION => 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION: ',
            OutputFlags::FINISH_COMPUTATIONAL_COMPLEXITY_TEST => 'FINISH COMPUTATIONAL COMPLEXITY TEST',
            OutputFlags::ERROR_MEMORY_LIMIT_EXCEEDED => 'ERROR MEMORY LIMIT EXCEEDED',
            OutputFlags::ERROR => 'ERROR',
            OutputFlags::FINISH => 'FINISH'
        };
    }
}
