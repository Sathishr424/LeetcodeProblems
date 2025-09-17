# Last updated: 17/9/2025, 4:31:36 pm
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = cuisines
        self.foods_index = {}
        self.cuisines_heap = defaultdict(list)
        self.ratings = ratings
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.foods_index[food] = i
            heapq.heappush(self.cuisines_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        index = self.foods_index[food]
        cuisine = self.cuisines[index]

        self.ratings[index] = newRating
        heapq.heappush(self.cuisines_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines_heap[cuisine]:
            index = self.foods_index[self.cuisines_heap[cuisine][0][1]]
            if self.ratings[index] != -self.cuisines_heap[cuisine][0][0]:
                heapq.heappop(self.cuisines_heap[cuisine])
            else:
                return self.cuisines_heap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)