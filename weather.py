import re

#finds all integers in a string and formats them using a regular expression returning a list of valid integers
def get_integers(a):
    return [int(float(s)) for s in re.findall(r'\d+(?:\.\d+)?', a)]

#takes a list of integers and finds the minimum value(s) from the list along with their indexes
def locate_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a) 
                      if smallest == element]

def get_minimum_temperature_difference(filepath):
    with open(filepath, "r") as w:
        weather_data = w.readlines()
        weather_data = [i.rstrip().split() for i in weather_data]
        
    days = []
    differences = []

    for item in weather_data:
        #ignore any empty data
        if len(item) != 0:
            #ignore any rows which have bad data i.e letters as dates/temperatures and ignore the column headers and the monthly average column
            if not item[0].isalpha() and not item[1].isalpha() and not item[2].isalpha():
                day = item[0]
                max_temp = get_integers(item[1])[0]
                min_temp = get_integers(item[2])[0]
                #making sure there is no bad data for min/max temperature
                if max_temp < min_temp:
                    print("There is a minimum temperature that was more than a maximum temperature on day {}, it was ignored.".format(day))
                    continue
                else:
                    days.append(day)
                    differences.append(max_temp-min_temp)
    
    minimum_difference = locate_min(differences)

    days_with_minimum_difference = []

    for index in minimum_difference[1]:
        days_with_minimum_difference.append(days[index])
        
    if len(days_with_minimum_difference) > 1:
        days = ", ".join(str(day) for day in days_with_minimum_difference)
        print("The minimum difference in temperature for the month is " + str(minimum_difference[0]) + " degrees on the days " + days)
    else:
        day = days_with_minimum_difference[0]
        print("The minimum difference in temperature for the month is " + str(minimum_difference[0]) + " degrees on day " + day)
            

    



