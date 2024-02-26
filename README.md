# bartosz-lauks-master-degree

Projekt magisterski Bartosz Lauks 2024

Polecenia należy wykonąć w docelowym katalogu aplikacji

Aplikacja do uruchomienia wymaga Dockera

## LISTA ALGORYTMOW

- Przeszukiwanie w szerz (Breadth-First Search, BFS) +
- Przeszukiwanie w głąb (Depth-First Search, DFS) +
- Algorytm Dijkstry +
- Algorytm Bellmana-Forda +
- Algorytm Kruskala +
- Algorytm Prima +
- Algorytm Forda-Fulkersona +
- Algorytm Johnsona +
- Algorytm Fleury'ego +
- Algorytm Floyd-Warshalla +
- Algorytm Topologicznego Sortowania +

### Błąd przy budowaniu aplikacji
- Jeśli pojawi sie bład przy budowanu aplikacji wykonaj budowanie ponownie. Bład obrazu Docker

### Dostęp do konsoli admina RabbitMQ
- http://localhost:15672/

**Pierwszy start aplikacji**
```
$ make build_dev
$ make start_dev # http://localhost:8083
$ make install
```
**Wdrażanie backup z danymi testowymi bez plików wyników testów**
```
cat backup.sql | docker exec -i bartosz-lauks-master-degree-mysql-dev /usr/bin/mysql -u root bartosz-lauks-master-degree_dev
```

**Uruchomienia konsumenta wiadomości**
```
make start_queued_message_handling
```

**Lista użytkowników w tym backup i ich hasła**
- bartosz.lauks@interia.pl hasło : 123123 -> User
- cruzonek@gmail.com hasło : 123123 -> Super User

**Do działania systemu rejestracji i weryfikacji konta wymagane jest dodanie w plikiu .env MAILER_DSN**
```
MAILER_DSN=gmail://EMAIL@gmail.com:HASŁO@default
```

**Wyłączenie aplikacji**
```
$ make stop
```