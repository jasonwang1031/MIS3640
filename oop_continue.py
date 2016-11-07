class Time:
    '''
    represents the time of day.
    attributes: hour, minute, second
    '''
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))
    def time_to_int(self):
            minutes = self.hour * 60 + self.minute
            seconds = minutes * 60 + self.second
            return seconds 
    #def is_after(self,other):


start = Time()
start.hour = 9
start.minute = 45
start.second = 0
start.print_time()
print(start.time_to_int())
