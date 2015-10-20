__author__ = 'leoxuan'
# translate the second to the hour
# time 10.19 2015
def timechanger(time):
    if time < 60:
         print 'the time is :%d second'%time
    elif 60<=time<3600:
         min = time/60
         sec = time%60
         print('the time is :%d minute %d second'%(min ,sec))
    elif  3600<=time<=86400:
        hour = time/3600
        time = time -hour*3600
        min = time/60
        sec = time%60
        print('the time is :%d hour %d minute %d second'%(hour,min ,sec))
    else:
        print('please put a right time')
while True:
    ten=raw_input("please input the second you want change:")
    if ten.isdigit():
        break
ten=int(ten)
timechanger(ten)

