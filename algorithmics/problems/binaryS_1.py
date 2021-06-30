# 1.1 Suppose you have a sorted list of 128 names, 
# and you’re searching through it using binary search. What’s the maximum number of steps it would take?

import math

def answerFmt(names_count, maxSteps):
    return f"The maximum number of steps to search for a name in a list of {names_count} items is : {maxSteps} steps."

names_count = 128
maxSteps = math.log2(names_count) #binary search's 0(log n)
print(answerFmt(names_count, maxSteps))

# 1.2 Suppose you double the size of the list. What’s the maximum number of steps now?

doubled_count = names_count * 2
doubled_maxSteps = math.log2(doubled_count)
print(answerFmt(doubled_count, doubled_maxSteps))

