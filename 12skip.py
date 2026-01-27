###### Defining a range by the first and last item of a list.
###### After we create a chronological list based on the range given from the input list
###### We then use len to get the number of entries in our difference list.

def howManyMissing(inputlist):
    chronlist = list(range(inputlist[0], (inputlist[-1] + 1)))
    difflist = list(set(chronlist) - set(inputlist))
    print(len(difflist))


howManyMissing([1, 3])
output = 1

howManyMissing([7, 10, 11, 12])
output = 2

howManyMissing([1, 3, 5, 7, 9, 11])
output = 5

howManyMissing([5, 6, 7, 8])
output = 0
