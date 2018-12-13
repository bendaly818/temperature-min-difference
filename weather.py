import re

#change this to read other files
filepath = "./weather.dat"

#formats a string using a regular expression returning a list of valid integers (as we are ignoring the monthly average, which has floating point numbers, I assumed that I didn't need to handle floating point numbers)
#if floating point numbers were needed, this can just be changed to return a list of floating point numbers instead.
def get_integers(a):
    return [int(s) for s in re.findall(r'\d+(?:\.\d+)?', a)]

#takes a list of integers and finds the minimum value(s) from the list along with their indexes
def find_min(a):
    smallest = min(a)
    return smallest, [index for index, element in enumerate(a) if smallest == element]

#computes the minimum temperature difference for a set of weather data
#prints out the minimum temperature difference along with the corresponding day(s) which have this difference
def get_minimum_temperature_difference(filepath):
    #reading the file and formatting the data into a suitable format to work with --> [[row1],[row2],...]
    with open(filepath, "r") as w:
        weather_data = w.readlines()
        #getting rid of any whitespace or new lines
        weather_data = [i.rstrip().split() for i in weather_data]
        
    days = []
    differences = []

    for row in weather_data:
        #ignore any empty data
        if len(row) != 0:
            #ignore any rows which have bad data i.e letters as dates/temperatures and ignore the column headers and the monthly average column
            if not row[0].isalpha() and not row[1].isalpha() and not row[2].isalpha():
                day = row[0]
                max_temp = get_integers(row[1])[0]
                min_temp = get_integers(row[2])[0]
                #making sure there is no bad data for min/max temperature, if so, alert the user ()
                if max_temp < min_temp:
                    print("There is a minimum temperature that was more than a maximum temperature on day {}, it was ignored\n".format(day))
                    continue
                else:
                    days.append(day)
                    differences.append(max_temp-min_temp)
                

                
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
    



