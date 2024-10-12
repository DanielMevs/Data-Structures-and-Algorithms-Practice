from typing import List


class NestedInteger:
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather
        """
        """than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it"""
        """ holds a single integer.
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds """
        """a nested list.
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nestedList):
        for n in nestedList:
            if n.isInteger():
                self.stack.append(n.getInteger())
            else:
                self.dfs(n.getList())
