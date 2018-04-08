#!/anaconda3/bin/python3

from datetime import datetime

# Function definition is here
def updateTime( myTimeFull ):
	myTimeHours = ( myTimeFull.hour * 60 * 60 )
	myTimeMins = ( myTimeFull.minute * 60 )
	myTime = ( myTimeHours + myTimeMins + myTimeFull.second )
	return myTime;

# Smaller numbers for testing
workMins = 2
#workMins = 20
breakMins = 1
#breakMins = 5
workBlocks = 4
breakBlocks = ( workBlocks - 1 )
workWaitSecs = ( workMins * 2 )
#workWaitSecs = ( workMins * 60 )
breakWaitSecs = ( breakMins * 2 )
#breakWaitSecs = ( breakMins * 60 )
allWorkWaitSecs = ( workWaitSecs * workBlocks )
allBreakWaitSecs = ( breakWaitSecs * breakBlocks )

startTime = datetime.today()
startTimeInSecs = updateTime( startTime )
currTrackTime = startTimeInSecs
finishTime = ( startTimeInSecs + allWorkWaitSecs + allBreakWaitSecs )

print('Get to work.')
testTime = 0
while ( currTrackTime < finishTime ):
	while ( testTime < ( currTrackTime + workWaitSecs ) ):
		workTimeFull = datetime.today()
		testTime = updateTime( workTimeFull )
	currTrackTime = ( currTrackTime + workWaitSecs )
	if currTrackTime >= finishTime:
		continue
	print('Take a break.')
	while testTime < ( currTrackTime + breakWaitSecs ):
		testTimeFull = datetime.today()
		testTime = updateTime( testTimeFull )
	currTrackTime = ( currTrackTime + breakWaitSecs )
	print('Get back to work.')
print("Take a 15 minute break.")
