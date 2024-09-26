# bartosz-lauks-master-degree

## Design and implementation of a test platform intended for testing graph algorithms

Celem niniejszej pracy jest opracowanie i implementacja platformy testowej przeznaczonej do
testowania algorytmów grafowych. Aplikacja posiada szeroką gamę gotowych narzędzi do testowania implementacji algorytmów grafowych od testów jednostkowych, obciążeniowych do
testów złożoności obliczeniowych i na podstawie ich tworzy statystyki oraz wykresy. Posiada
także czytelne GUI obrazujące krok po kroku proces testowania, wskazując popełnione błędy w
przypadku niepoprawnego wyniku testu. Oprogramowanie jest zaprojektowane tak, aby mogło
uruchamiać się na dowolnej platformie bez znaczenia na system operacyjny.
Słowa kluczowe: PHP, Python, Algorytm, Graf, Docker, Symfony, MyS

## Projekt magisterski Bartosz Lauks 2024

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
$ make build_dev - jeśli pojawia się błąd przejdź na branch master-non-root
$ make start_dev # http://localhost:8083
$ make install
```
**Wdrażanie backup z danymi testowymi bez plików wyników testów**
```
cat backup.sql | docker exec -i bartosz-lauks-master-degree-mysql-dev /usr/bin/mysql -u root bartosz-lauks-master-degree_dev
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

======================================Author note v2 app==================================================

**feature, to change, ideas**

- Testing all algorithms of all types.
- Increasing the stack of programming languages ​​used to implement algorithms.
- Added data structure selection for algorithm testing. Consider default tests on all or almost all data structures. (Is it possible? Unlikely, requires several dedicated implementations)
- Adding a production analyzer of used resources (savings, unexpected, caught loops, etc.)
- Adding a code (static) analyzer (AST tree). (It gives better validation and saves resources.). ()
- Complexity analysis based on the code "Is it possible? Suspected undecidability"
- Improving the testing process. The steps themselves, but also the architecture (microservice).
- Ask the professor about functional requirements are. (Student use, license):
- Cont.

======================================V2 priv repo===============================================
