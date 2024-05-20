import math


def take_value(parameter):
    value = str()
    for c in str(parameter):
        if c.isdigit() or c=='.':
            value = value + c
    return float(value)

def speed(RPM,radius):
    '''function to calculate the speed of the treadmill'''
    speed = 2 * math.pi * take_value(radius)/100 * take_value(RPM)/60
    return speed #m/s

def distance(RPM,radius,time):
    '''function to calculate the distance walked/ran'''
    distance = speed(RPM,radius) * take_value(time)*60*60
    return round(distance) #m

def calories_burnt(RPM,radius,time,weight,grade):
    '''function to calculate the burned calories'''
    #grade = 0 #It is considered as gradient(inclination) of the treadmill is zero
    speeds = speed(RPM,radius)
    if speeds <= 1.67 :#checking the situation(waalking or running)
        #when walking
        burned_calories = (0.1*speeds + 1.8*speeds*grade + 3.5)* take_value(weight)* take_value(time)/200*60
    else:
        #when running
        burned_calories = (0.2*speeds + 0.9*speeds*grade + 3.5)* take_value(weight)* take_value(time)/200*60
    return round(burned_calories) #cal

def steps(height,RPM,radius,time):
    '''function to calculate number of steps taken'''
    num_steps = distance(RPM,radius,time)/1000 * 3280.84/( take_value(height)/12 * 0.413)
    return round(num_steps)