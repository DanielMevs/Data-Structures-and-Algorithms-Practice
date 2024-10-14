import timeit


class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList

    def hasNext(self):
        return bool(len(self.stack))

    def hasNextAlternative(self):
        return len(self.stack) > 0


# Sample nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Create an instance of NestedIterator
iterator = NestedIterator(nested_list)

# Time the performance of hasNext
time_hasNext = timeit.timeit(lambda: iterator.hasNext(), number=1000000)

# Time the performance of hasNextAlternative
time_hasNextAlternative = timeit.timeit(lambda: iterator.hasNextAlternative(), number=1000000)

print(f"hasNext: {time_hasNext} seconds")
print(f"hasNextAlternative: {time_hasNextAlternative} seconds")
