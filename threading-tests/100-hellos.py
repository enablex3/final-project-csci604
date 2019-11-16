""" Final Project
    Execute 100 Hello World Threads
    Elijah Reyes
    CSCI 604 """

import time, threading

# execution time file will be in current working directory
try:

	with open( 'execution-time.txt', 'w') as exFile:
		exFile.write( 'Top of the file.\n' )

except Exception as exception:
	print(exception)
	quit()

# method to print 'Hello, world'
def helloWorld():

	startTime = time.time()
	print('Hello world')

	recordTime(startTime)

# method to append to the file
def recordTime(startTime):

	try:

		with open( 'execution-time.txt', 'a') as exFile:
			# round by 10 decimal places
			executionTime = str( round( ( time.time() - startTime ), 10) )
			exFile.write(executionTime + '\n')

	except:
		
		# the file may open, so simply retry
		recordTime(startTime)

# 100 threads
threads = 10000

for t in range( 0, threads ):
	threading.Thread( target = helloWorld ).start()
