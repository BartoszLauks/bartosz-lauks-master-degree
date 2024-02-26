<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20240106212641 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Add table hat_messages and two relation with this table to test and user.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE chat_messages (id INT AUTO_INCREMENT NOT NULL, user_id INT NOT NULL, test_id INT NOT NULL, body LONGTEXT NOT NULL, created_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', updated_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', INDEX IDX_EF20C9A6A76ED395 (user_id), INDEX IDX_EF20C9A61E5D0459 (test_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE chat_messages ADD CONSTRAINT FK_EF20C9A6A76ED395 FOREIGN KEY (user_id) REFERENCES user (id)');
        $this->addSql('ALTER TABLE chat_messages ADD CONSTRAINT FK_EF20C9A61E5D0459 FOREIGN KEY (test_id) REFERENCES test (id)');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE chat_messages DROP FOREIGN KEY FK_EF20C9A6A76ED395');
        $this->addSql('ALTER TABLE chat_messages DROP FOREIGN KEY FK_EF20C9A61E5D0459');
        $this->addSql('DROP TABLE chat_messages');
    }
}
