<?php

declare(strict_types=1);

namespace App\Service;

const CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
class RandomStringGenerator
{
    public function getToken(int $length) : string
    {
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
           $index = rand(0, strlen(CHARACTERS) - 1);
           $randomString .= CHARACTERS[$index];
        }

        return $randomString;
    }
}
