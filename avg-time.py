""" Final Project
    Execute 100 Hello World Threads - Calculate Average
    Elijah Reyes
    CSCI 604 """

try:

	with open( 'execution-time.txt', 'r') as exFile:
		# get only the numerical values and convert them to a float
		executionTimes = [ float( line.rstrip() ) for line in exFile.readlines() if 'Top of the file.' != line.rstrip() ]

except Exception as exception:
	print(exception)
	quit()

# calculate the average execution time
avgTime = round( sum( executionTimes ) / len( executionTimes ), 6 )

# print the result
print( 'Average execution time: {} seconds.'.format( str( avgTime ) ) )

