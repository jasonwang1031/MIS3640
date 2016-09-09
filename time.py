import time
A = int(time.time())
B = A/24/60/60
C = int(B)
D = (B-C)
Hour = D * 24
Minutes = (Hour - int(Hour)) * 60
Seconds = (Minutes - int(Minutes))*60
print('Time: %2d days: %2d hours: %2d min: %2d seconds from Epoch' % (C,Hour, Minutes, Seconds))



