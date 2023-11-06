## LISTA ALGORYTMOW

- Przeszukiwanie w szerz (Breadth-First Search, BFS)
- Przeszukiwanie w głąb (Depth-First Search, DFS)
- Algorytm Dijkstry
- Algorytm Bellmana-Forda
- Algorytm Kruskala
- Algorytm Prima
- Algorytm Forda-Fulkersona
- *Algorytm A (A-star)**
- Algorytm Johnsona
- Algorytm Fleury'ego
- Algorytm Hierholzera
- Algorytm Edmondsa-Karpa
- Algorytm Floyd-Warshalla
- Algorytm Topologicznego Sortowania
- Algorytm Kosaraju

## TODO BFS
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