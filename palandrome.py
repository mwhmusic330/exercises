

####A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

###Find the largest palindrome made from the product of two 3-digit numbers.
range1 = range(100, 1000)
range2 = range(100, 1000)
combi_list = []
plist = []


for i in range1:
    for j in range2:
        combi_list.append(i * j)



def checkpal(a):
    s = str(a)
    return s == s[::-1]

def findpal(combi_list):
    for a in combi_list:
        if checkpal(a):
            plist.append(a)
findpal(combi_list)
print(max(plist))
