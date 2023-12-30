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

### Testowanie
- Graf pusty:

Sprawdź, jak algorytm BFS zachowuje się w przypadku całkowicie pustego grafu (bez wierzchołków i krawędzi).

- Graf z jednym wierzchołkiem:

Utwórz graf z jednym wierzchołkiem i przetestuj algorytm BFS, zaczynając od tego jedynego wierzchołka. Upewnij się, że algorytm działa poprawnie i zwraca ten sam wierzchołek jako wynik.

- Brak ścieżki między wierzchołkami:

Utwórz graf, w którym nie istnieje ścieżka między wierzchołkami, które próbujesz odwiedzić. Sprawdź, czy algorytm BFS zwraca wartość None w takim przypadku.

- Wierzchołek końcowy jest wierzchołkiem początkowym:

Sprawdź, jak algorytm BFS reaguje, gdy wierzchołek początkowy i wierzchołek końcowy są tym samym wierzchołkiem. Czy algorytm obsługuje ten przypadek poprawnie?

- Graf niespójny:

Utwórz graf niespójny, który składa się z dwóch lub więcej składowych. Przetestuj algorytm BFS na takim grafie i upewnij się, że działa poprawnie, odwiedzając tylko wierzchołki w jednej składowej, zaczynając od odpowiedniego wierzchołka początkowego.

## Wstępna dokumentacja
### Błąd przy budowaniu aplikacji
- Jeśli pojawi sie bład przy budowanu aplikacji wykonaj budowanie ponownie. Bład obrazu Docker

## Broker Wiadomości
### Włączenie konsumenta wiadomości
- php bin/console messenger:consume async
- php bin/console messenger:consume async -vv // with details what's happening

- ### Dostęp do konsoli admina RabbitMQ
- http://localhost:15672/
- Username: guest Password: guest 
