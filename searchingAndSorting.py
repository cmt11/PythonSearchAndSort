def seqSearchLast(myList, target):
    for i in range(len(myList)-1, -1, -1):
        if myList[i] == target:
            return i
    return None


def trinarySearch(myList, target):
    low = 0
    high = len(myList)-1
    while low <= high:
        oneThird = low + (high - low)/3
        twoThirds = high - (high - low)/3
        if myList[oneThird] == target:
            return oneThird
        if myList[twoThirds] == target:
            return twoThirds
        if target < myList[oneThird]:
            high = oneThird - 1
        else:
            if target > myList[oneThird] and target < myList[twoThirds]:
                low = oneThird + 1
                high = twoThirds - 1
            else:
                low = twoThirds + 1
    return None


def backwardsBubbleSort(myList):
    for i in range(len(myList)-1, 0, -1):
        for i in range(len(myList)-1, 0, -1):
            if myList[i] < myList[i-1]:
                myList[i], myList[i-1] = myList[i-1], myList[i]
    return myList


def backwardsSelectionSort(myList):
    i = len(myList)-1
    while i >= 0:
        maxIndex = i
        j = i
        while j >= 0:
            if myList[maxIndex] < myList[j]:
                maxIndex = j
            j-=1
        myList[i], myList[maxIndex] = myList[maxIndex], myList[i]
        i-=1
    return myList
