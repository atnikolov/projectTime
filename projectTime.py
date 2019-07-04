import math

hoursTotalProject = float( input( "How many hours needed for the project: " ) )
daysProjectTotal = int( input( "How many days for the project: " ) )
peopleWorking = int( input( "How many people will work on the project: " ) )

hoursPerDay = 8

overTime = 2 * peopleWorking * daysProjectTotal
workingHours = math.floor( (hoursPerDay * peopleWorking) * daysProjectTotal + overTime ) * 0.9
workingDays = math.floor( (workingHours / 8) * 0.9 )

resultDays = daysProjectTotal - workingDays
resultHours = math.fabs( hoursTotalProject - workingHours )

if hoursTotalProject > workingHours:
    print( "Not good! You need {:.2f} hours extra to finish the project!".format( resultHours ) )
elif hoursTotalProject < workingHours:
    print( "Good job! You have {:.2f} hours extra for the project!".format( resultHours ) )
else:
    print( "Good! You should be done with the project just on time!" )
