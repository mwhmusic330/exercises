||``` py 
monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
def dayOfYear(datestr):
    month, day, year = [int(i) for i in datestr.split("/")]
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        monthlist[1] = 29
    else:
        monthlist[1] = 28
    # UNLESS divisible 400
    datesum = sum(monthlist[:(month)-1])+day
    print(datesum)

def main():
    dayOfYear("12/13/2020")
  ###  output = 348

    dayOfYear("11/16/2020")
    ###output = 321

    dayOfYear("1/9/2019")
    ###output = 9

    dayOfYear("3/1/2004")
    ###output = 61

    dayOfYear("12/31/2000")
    ###output = 366 # leap year

    dayOfYear("12/31/2019")
    ###output = 365 #non leap year 

if __name__ == "__main__":
    main()
```||
