# You want to know how much money you could have made yesterday buying and selling Apple stock (no shorting!)
# index 0 represent market opening at 9:30 AM. So index 15 is 9:45.
# you can only do one transaction per minute
def getProfit(arr):
    lowestIdx = arr.index(min(arr))

    startFromIdx = lowestIdx + 1
    slicedArr = arr[startFromIdx:]
    idxHighest = slicedArr.index(max(slicedArr))
    
    highestIdx = startFromIdx + idxHighest
    return arr[highestIdx] - arr[lowestIdx]


def test_answer():
    apple_stock = [50,45,28,99,97]
    assert getProfit(apple_stock) == 71