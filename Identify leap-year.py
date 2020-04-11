"""
decide if it is a leap-year
A practice by a rookie
                  Shuzhe Li
"""
temp = int(input('year = '))
if temp % 4:
    print('%d is a commom-year', temp)
else:
    print('%d is a leap-year', temp)