# the trend population of America after 1991.the number is just to do exercise,it not the really population
# time 10.20 2015
def brith(second):
    brithNumber = second /7
    return brithNumber
def death(second):
    deathNumber = second /13
    return  deathNumber
def immigrant(second):
    immigrantNumber = second /35
    return immigrantNumber
def timeTosec(year):
    year = year -1991
    seco = year*365*86400
    return seco
population = 307357870
ye = input('input the year after 1991:')
ti = timeTosec(ye)
population +=brith(ti)+death(ti)+immigrant(ti)
print 'the year of %d America population is %f'%(ye,population)


