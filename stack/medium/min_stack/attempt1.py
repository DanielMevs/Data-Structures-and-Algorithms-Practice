# Ask: design a stack class that supports push, pop, top, and 
# retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min if self.min else val)
        self.min = val
        
    # - Making min a variable makes it fail when we pop from the stack
    # and we don't take into account the new min after this operation
    # - To get over this, we need to make min a stack, too.
    # That way we will ensure that the new val is reflected in this new
    # min stack by popping it as well.
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min

# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()