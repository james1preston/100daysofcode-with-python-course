#!/anaconda3/bin/python3

from time import sleep

loopcount = 1
loopmax = 4
# Smaller numbers for testing
workmins = 2
#workmins = 20
breakmins = 1
#breakmins = 5

print("Get to work.")
while loopcount < loopmax:
	sleep( workmins * 2 )		#sleep is in seconds
	#sleep( workmins * 60 )		#sleep is in seconds
	print("Take a 5 minute break.")
	sleep( breakmins * 2 )
	#sleep( breakmins * 60 )
	print("Get back to work.")
	loopcount += 1
sleep( workmins * 2 )
#sleep( workmins * 60 )
print("Take a 15 minute break.")
