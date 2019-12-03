#Jessica Hiatt

print ("Please create a file and enter your course names (without spaces), credit hours, and the average time (in hours) you spend working on that course weekly. Enter it in the following format:")
print ("COURSE_NAME CREDIT_HOURS AVG_TIME")

print ("Enter the name of the file you just created")
fileName = input('File name> ')

data = open(fileName, 'r')

#print ("Error. Invalid file name.")

with data:
    courses = []
    credit_hours = []
    avg_hours = []
    lines = data.readlines()
    for i in lines:
        courses.append(i.split()[0])
        credit_hours.append(i.split()[1])
        avg_hours.append(i.split()[2])

def calculate_total_hours(avg_hours):
    total_hours = 0
    index1 = 0
    for item in avg_hours:
        total_hours += float(avg_hours[index1])
        index1 += 1

    return total_hours

total_hours = calculate_total_hours(avg_hours)
        
def calculate_time_spent(avg_hours):
    time_spent = []
##    total_hours = 0

##    index1 = 0
##    for item in avg_hours:
##        total_hours += float(avg_hours[index1])
##        index1 += 1

    index2 = 0
    for item in avg_hours:
        time_spent.append(float(avg_hours[index2]) / total_hours)
        index2 += 1
    
    return time_spent

def calculate_suggested_time_spent(credit_hours):
    suggested_time_spent = []
    total_credit_hours = 0

    index1 = 0
    for item in credit_hours:
        total_credit_hours += float(credit_hours[index1])
        index1 += 1
    
    index2 = 0
    for item in credit_hours:
        suggested_time_spent.append(float(credit_hours[index2]) / total_credit_hours)
        index2 += 1

    return suggested_time_spent

time_spent = calculate_time_spent(avg_hours)
suggested_time_spent = calculate_suggested_time_spent(credit_hours)

def calculate_time_adjustment(time_spent, suggested_time_spent):
    time_change = []
    
    index1 = 0
    for item in time_spent:
        if time_spent[index1] < suggested_time_spent[index1]:
           time_change.append((suggested_time_spent[index1] - time_spent[index1]))
           index1 += 1
        elif time_spent[index1] > suggested_time_spent[index1]:
           time_change.append((time_spent[index1] - suggested_time_spent[index1]))
           index1 += 1
        else:
           time_change.append(0)
           index1 += 1

    return time_change

def calculate_change_direction(time_spent, suggested_time_spent):
    change_direction =[]
    index1 = 0
    for item in time_spent:
        if time_spent[index1] < suggested_time_spent[index1]:
           change_direction.append('increase')
           index1 += 1
        elif time_spent[index1] > suggested_time_spent[index1]:
           change_direction.append('decrease')
           index1 += 1
        else:
           change_direction.append('perfect')
           index1 += 1

    return change_direction
 
time_change = calculate_time_adjustment(time_spent, suggested_time_spent)
change_direction = calculate_change_direction(time_spent, suggested_time_spent)
import math
print ("\nBased on the data provided, here are the statistics on how you spend your", total_hours, 'hours working.')
print ("The reccommended adjustments to the time you spend in each courses is provided.")

total_minutes = total_hours*60
index0 = 0
for percent in time_spent:
    print ('\nIn', courses[index0], 'the percent of total work time you spend is', "{:.2%}".format(time_spent[index0],4))
    print ('The suggested percent of time you spend on', courses[index0], 'is', "{:.2%}".format(suggested_time_spent[index0],4))
    if change_direction[index0] == ('perfect'):
        print ("You do not need to adjust the time you spend in", courses[index0])
        index0 += 1
    else:
        print ('You may need to', change_direction[index0], 'the percent of time you spend in', courses[index0], 'by', 'is', "{:.2%}".format(time_change[index0],4))
        print ('To make this reccomended adjustment, you need to', change_direction[index0], 'the time you spend by', math.floor((total_minutes*time_change[index0])/60), 'hours and', round((total_minutes*time_change[index0])%60), 'minutes.')
        index0 += 1
               
suggested_time_spent = calculate_suggested_time_spent(credit_hours)



