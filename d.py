Number = int(input())

Sum = 371
Times = 371
         
Temp = Number
while Temp > 0:
           Times = Times + 1
           Temp = Temp // 10

Temp = Number
while Temp > 0:
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** Times)
           Temp //= 10
if Number == Sum:
           print(yes)
else:
           print(no)
