def calendar_1(date, month, year) :
    m = (year // 100) % 4   #~      Eg.year = 1970 so m = 3
    odd = (m * 5) % 7       #~      odd =  3*5 % 7 = 1
    remain = year % 100     #~      remain = 70
    leap = remain // 4      #~      leap = 17
    ordinary = remain - leap#~      ordinary = 70 - 17 = 53
    odd = (odd + (leap*2 + ordinary)) % 7 #~    odd = 4
    
    month = month.lower()
    
    odd = odd - 1;
    
    if(month == "january"):
        odd = (date+odd) % 7
    elif(month == "february"):
        odd = (31 + date + odd) % 7
    elif(month == "march"):
        odd = (31+28 + date + odd) % 7
    elif(month == "april"):
        odd = (31+28+31 + date + odd) % 7
    elif(month == "may"):
        odd = (31+28+31+30 + date + odd) % 7
    elif(month == "june"):
        odd = (31+28+31+30+31 + date + odd) % 7
    elif(month == "july"):
        odd = (31+28+31+30+31+30 + date + odd) % 7
    elif(month == "august"):
        odd = (31+28+31+30+31+30+31 + date + odd) % 7
    elif(month == "september"):
        odd = (31+28+31+30+31+30+31+31 + date + odd) % 7
    elif(month == "october"):
        odd = (31+28+31+30+31+30+31+31+30 + date + odd) % 7
    elif(month == "november"):
        odd = (31+28+31+30+31+30+31+31+30+31 + date + odd) % 7
    elif(month == "december"):
        odd = (31+28+31+30+31+30+31+31+30+31+30 + date + odd) % 7

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    return days[odd]

    
date = int(input("Enter date: "))
month = input("Enter month: ")
year = int(input("Enter year: "))

print(f'The Day on {date} {month} {year} was / is {calendar_1(date, month, year)}')