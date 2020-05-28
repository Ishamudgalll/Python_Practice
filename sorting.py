badList = [12, 5, 13, 8, 9, 65]

length = len(badList) - 1
unsorted = True

while unsorted:
    for element in range(length):
            unsorted = False
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print (badList)
            else:
                unsorted = True

