<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20240106232431 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Add uuid to table.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('ALTER TABLE chat_messages ADD uuid BINARY(16) NOT NULL COMMENT \'(DC2Type:uuid)\'');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE chat_messages DROP uuid');
    }
}
