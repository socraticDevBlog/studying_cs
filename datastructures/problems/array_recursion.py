# Write a recursive function for generating all permutations of an input string. Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops—it just needs to also be recursive.

# https://www.interviewcake.com/question/python/recursive-string-permutations

def test():
    given = "abc"
    assert execute(given).sort() == ["bca", "bac", "cba", "cab", "acb", "abc"].sort()

def execute(val):
    letters = list(val)
    result = []

    for _ in letters:
        permutate(result, letters, 0)

    return result
    
def permutate(result, letters, idx):
    if idx + 1 >= len(letters):
        return result

    letters[idx + 1], letters[idx] = letters[idx], letters[idx + 1]
    result.append(listToString(letters))
    permutate(result, letters, idx + 1)

def listToString(list):
    str = ""
    for x in list:
        str += x

    return str

