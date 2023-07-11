strs = ["flower","flow","flight"]
truthy = [word[0] == strs[0][0] for word in strs]
# [x for b in a for x in b] # Works fine
print(truthy)