__author__ = 'leoxuan'
# the distance of spaceship from tbe earth
# time 10.19 2015
theDay = raw_input('the day input like 2009.9.25,must be the later of frist day:')
Day = []
Day = theDay.split('.')
year = int(Day[0])
month = int(Day[1])
day = int(Day[-1])
year = year -2009
month =month-9
day = day -25
time = 24*(year*365+month*30+day)
if time <0:
    print 'the date is no ture.'
else:
    distance = 166.37
    distance = distance+time*38241
    Kilometer = distance*1.609344
    Au = distance/(92955877.6)
    Tilight =Kilometer*2000/29979458
    print('the mail will take %f'%distance)
    print('the kilometer will take %f'%Kilometer)
    print('the AU will take %f'%Au)
    print('the second it will:%f'%Tilight)
