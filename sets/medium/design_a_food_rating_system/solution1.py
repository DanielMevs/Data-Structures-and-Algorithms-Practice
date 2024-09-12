from typing import List
from sortedcontainers import SortedSet
from collections import defaultdict


class FoodRatings:

    def __init__(
            self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_food = defaultdict(SortedSet)  # cuisine -> (rating, fd)
        self.cuisines = {}  # food -> cuisine
        self.ratings = {}  # food -> rating

        for i in range(len(foods)):
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[food]
        rating = self.ratings[food]

        self.cuisines_food[cuisine].remove((-rating, food))
        self.cuisines_food[cuisine].add((-newRating, food))

        self.ratings[food] = newRating
        
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_food[cuisine][0][1]


