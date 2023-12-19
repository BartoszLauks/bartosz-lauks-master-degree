<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20231218173913 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Create Gender table. Add related table User with Gender.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE gender (id INT AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, created_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', updated_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE test ADD created_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', ADD updated_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\'');
        $this->addSql('ALTER TABLE user ADD gender_id INT DEFAULT NULL');
        $this->addSql('ALTER TABLE user ADD CONSTRAINT FK_8D93D649708A0E0 FOREIGN KEY (gender_id) REFERENCES gender (id)');
        $this->addSql('CREATE INDEX IDX_8D93D649708A0E0 ON user (gender_id)');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE user DROP FOREIGN KEY FK_8D93D649708A0E0');
        $this->addSql('DROP TABLE gender');
        $this->addSql('ALTER TABLE test DROP created_at, DROP updated_at');
        $this->addSql('DROP INDEX IDX_8D93D649708A0E0 ON user');
        $this->addSql('ALTER TABLE user DROP gender_id');
    }
}
