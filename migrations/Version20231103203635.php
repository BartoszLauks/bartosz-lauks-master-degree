<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20231103203635 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Create test table to testing algorithms.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE test (id INT AUTO_INCREMENT NOT NULL, user_id INT NOT NULL, algorithm VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL, result INT NOT NULL, response LONGTEXT NOT NULL, language VARCHAR(255) DEFAULT NULL, uuid BINARY(16) NOT NULL COMMENT \'(DC2Type:uuid)\', INDEX IDX_D87F7E0CA76ED395 (user_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE test ADD CONSTRAINT FK_D87F7E0CA76ED395 FOREIGN KEY (user_id) REFERENCES user (id)');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE test DROP FOREIGN KEY FK_D87F7E0CA76ED395');
        $this->addSql('DROP TABLE test');
    }
}
