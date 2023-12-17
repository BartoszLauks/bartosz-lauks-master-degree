<?php

declare(strict_types=1);

namespace App\Massage;

use App\Entity\Test;

readonly class JohnsonImplementationTesting
{
    public function __construct(
        private Test $test
    ) {
    }

    public function getTest() : Test
    {
        return $this->test;
    }
}
