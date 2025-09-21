# Last updated: 22/9/2025, 12:16:52 am
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # First have an entry for every shop with every movie (double hash table [shop][movie])
        # Every movie have a heap with a (price, shop) comparator as movies heap
        # Once movie rented move mark it in rented_movies hash table [movie][shop] = 1
        # Once rented movie droped off delete the mark from rented_movies hash_table [movie][shop] = 0
        # Also, have the rented movies heap (price, shop, movie)

        self.shops = defaultdict(dict)
        self.movies = defaultdict(list)
        self.is_rented = defaultdict(lambda: defaultdict(int))
        self.rented_movies = []

        for shop, movie, price in entries:
            self.shops[shop][movie] = price
            heapq.heappush(self.movies[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        k = 5
        found = []
        ret = []
        prev = None
        while k and self.movies[movie]:
            price, shop = heapq.heappop(self.movies[movie])
            if shop == prev or self.is_rented[movie][shop]:
                continue
            prev = shop
            found.append((price, shop))
            ret.append(shop)
            k -= 1
        
        while found:
            heapq.heappush(self.movies[movie], found.pop())
        
        return ret

    def rent(self, shop: int, movie: int) -> None:
        self.is_rented[movie][shop] = 1
        heapq.heappush(self.rented_movies, (self.shops[shop][movie], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.is_rented[movie][shop] = 0
        heapq.heappush(self.movies[movie], (self.shops[shop][movie], shop))

    def report(self) -> List[List[int]]:
        k = 5
        found = []
        ret = []
        prev_movie = None
        prev_shop = None
        while k and self.rented_movies:
            price, shop, movie = heapq.heappop(self.rented_movies)
            if (prev_movie == movie and prev_shop == shop) or self.is_rented[movie][shop] == 0:
                continue
            prev_movie = movie
            prev_shop = shop
            found.append((price, shop, movie))
            ret.append([shop, movie])
            k -= 1
        
        while found:
            heapq.heappush(self.rented_movies, found.pop())
        
        return ret

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()