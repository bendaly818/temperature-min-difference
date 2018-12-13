import re

#change this to read other files
filepath = "./weather.dat"

#formats a string using a regular expression returning a list of valid integers
#i am ignoring the monthly average, which has floating point numbers, but if they for some reason crop up in the data I handle them by rounding them to the nearest integer
#if floating point numbers were needed, the pattern match still holds for floating points and can just be changed to return a
#list of floating point numbers instead and then the answer would then be in floating point notation 
def as_integer(a):
    return [int(float(s)) for s in re.findall(r'\d+(?:\.\d+)?', a)]

#takes a list of integers and finds the minimum value(s) from the list along with their indexes
def find_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a) if smallest == element]

#computes the minimum temperature difference for a set of weather data
#prints out the minimum temperature difference along with the corresponding day(s) which have this difference
def get_minimum_temperature_difference(filepath):
    #reading the file and formatting the data into a suitable format to work with --> [[line1],[line2],...]
    with open(filepath, "r") as w:
        weather_data = w.readlines()
        #getting rid of any whitespace
        weather_data = [line.rstrip().split() for line in weather_data]
        #and new lines
        weather_data = [line for line in weather_data if line]
  
    days = []
    differences = []

    for line in weather_data:
        #ignore any lines which have bad data i.e letters as dates/temperatures and ignore the column headers and the monthly average column
        if not line[0].isalpha() and not line[1].isalpha() and not line[2].isalpha():
            day = line[0]
            max_temp = as_integer(line[1])[0]
            min_temp = as_integer(line[2])[0]
            #making sure there is no minimum more than a maximum, if so, ignore it
            if max_temp < min_temp:
                continue
            else:
                days.append(day)
                differences.append(max_temp-min_temp)
        else:
            continue
                   
    #minimum value of temperature difference
    minimum_difference = find_min(differences)
    
    days_with_minimum_difference = []

    #list of days with minimum difference
    for index in minimum_difference[1]:
        days_with_minimum_difference.append(days[index])

    #checking if there are more than one day with the minimum difference, if so list them all, else just list the day which the minimum belongs to
    if len(days_with_minimum_difference) > 1:
        days = ", ".join(str(day) for day in days_with_minimum_difference)
        print("The minimum difference in temperature for the month is {} degrees on the days {}".format(minimum_difference[0], days))
    else:
        print("The minimum difference in temperature for the month is {} degrees on day {}".format(minimum_difference[0], days_with_minimum_difference[0]))
            
get_minimum_temperature_difference(filepath)


    



