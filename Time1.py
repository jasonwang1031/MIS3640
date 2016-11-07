class Time:
    '''
    represents the time of day.
    attributes: hour, minute, second
    '''
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    
    def time_to_int(self):
            minutes = self.hour * 60 + self.minute
            seconds = minutes * 60 + self.second
            return seconds 
    
    
    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()
    
    def is_as_expected(self,duration,arrival):
        return self.time_to_int() + duration.time_to_int() == arrival.time_to_int()
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __add__ (self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __str__ (self):
        return '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)

def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)

start = Time(9,45,0)
#start.hour = 9
#start.minute = 45
#start.second = 0

start.print_time()
print(start.time_to_int())

end = start.increment(2000)
end.print_time()
print(end.is_after(start))

traffic = Time(0,30,0)
#traffic = Time()
#traffic.hour = 0
#traffic.minute = 30
#traffic.second = 0

expect = Time(10,15,0)
#expect = Time()
#expect.hour = 10
#expect.minute = 15
#expect.second = 0
traffic.print_time()
expect.print_time()
print(start.is_as_expected(traffic,expect))

breakfast = Time(8,0,0)
print(breakfast.time_to_int())
lunch = Time(12,0,0)
print (breakfast+lunch)


