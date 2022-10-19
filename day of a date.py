def numberOfLeapYears(intsyear,intyear):
    c=-1
    for i in range(intsyear,intyear+1):
        if(i%4==0):
            c+=1
    return c
dayCode={
    0:"Sunday",
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday"
}
monthCode={
    1:0,
    2:3,
    3:3,
    4:6,
    5:1,
    6:4,
    7:6,
    8:2,
    9:5,
    10:0,
    11:3,
    12:5
}
centuryCode={
    0:0,
    1:6,
    2:4,
    3:2,
    4:0
}
date=int(input("Enter the date"))
month=int(input("Enter the month code"))
year=input("Enter the year")
lastTwoDigits=year[2:]
intLastTwoDigits=int(lastTwoDigits)
intyear=int(year)
#print("last two digits are"+str(lastTwoDigits))
syear=input("Enter the starting year of the century")
firstTwodigits=syear[0:2]
intFirstTwodigits=int(firstTwodigits)
#print("First two digits are "+str(firstTwodigits))
intsyear=int(syear)
leapYears=numberOfLeapYears(intsyear,intyear)
#print("Number of leap years are "+str(leapYears))
#print(daycode[5])
ccode=(intFirstTwodigits+1)%4
res=date+monthCode[month]+intLastTwoDigits+leapYears+centuryCode[ccode]
res=res%7
if((month==1 or month==2) and (intyear%4==0)):
    print(dayCode[res-1])
else:
    print(dayCode[res])