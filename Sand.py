import matplotlib.pyplot as plt


def average(data):
    '''
    A simple averaging function for a list.
    :param data: The list of numbers.
    :return: The average of the list of numbers.
    '''
    return sum(data)/len(data)

def seven_day_average(data):
    '''
    Calculates the moving average of calendar data.
    :param data: Calendar data stored in a list.
    :return: A list containing the weekly moving average.
    '''
    # We fill the list with 6 days of 'null' values
    moving_average = [float('nan') for i in range(6)]
    for i in range(len(data)-6):
        week = average(data[i:i+7])
        moving_average.append(week)
    return moving_average

# Daily ratings
September = [1, 3, 2, 3, 2, 4, 1, 1, 2, 1, 3, 2, 3, 2, 2, 3, 3, 4, 3, 2, 3, 2, 3, 2, 2, 2]
October =   [3, 4, 3, 3, 2, 1, 3, 2, 3, 2, 3, 2, 2, 2, 3, 3, 2, 3, 3, 2, 2, 2]
November =  []

# Start on October 3rd, and again, we have
check_boxes = [float('nan') for i in range(30)]+[6, 7, 16, 13, 14, 11, 2, 16, 7, 11, 14, 8, 8, 6, 6, 6, 10, 11, 8]

all_days = September + October + November

# Graphing the information
plt.plot(all_days, 'b', label='Daily Rating')
plt.plot(seven_day_average(all_days), 'r', label='Weekly Average')
plt.plot(check_boxes, 'g', label='Checks')

plt.ylabel('Rating')
plt.xlabel('Day')

plt.yticks([1,2,3,4,5])

plt.grid(True)
plt.legend()

plt.savefig("DevonRating")
plt.show()