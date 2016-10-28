class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(t):

    print ('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def is_after(t1,t2):
    return (t1.hour, t2.minute,t1.second)>(t2.hour,t2.minute,t2.second)


t1 = Time()
t1.hour = 5
t1.minute = 10
t1.second = 5

t2 = Time()
t2.hour = 10
t2.minute = 5
t2.second = 5

print(is_after(t1,t2))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -=60
        sum.minute += 1
    if sum.minute > 60:
        sum.minute -=60
        sum.hour += 1

    return sum

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

 def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def subtract_time(t1,t2):
    seconds = abs(time_to_int(t1)-time_to_int(t2))
    return int_to_time(seconds)

def mul_time(t1,num):
    seconds = time_to_int(t1)
    new_time = seconds * num
    return int_to_time(new_time)

def average_pace(t1,distance):
    seconds = time_to_int(t1)
    speed = seconds/distance
    return int_to_time(speed)


start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)
