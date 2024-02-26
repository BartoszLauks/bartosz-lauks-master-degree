<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20240110134204 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Add computational_complexity table.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE computational_complexity (id INT AUTO_INCREMENT NOT NULL, algorithm VARCHAR(255) NOT NULL, language VARCHAR(255) NOT NULL, time_complexity DOUBLE PRECISION NOT NULL, memory_complexity INT NOT NULL, created_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', updated_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP TABLE computational_complexity');
    }
}
