""" Final Project
    Download Files Test
    Elijah Reyes """

import wget, time

print('                       This test will run once...')
print('Choose one of the options to download:')
print('(1) A 100MB file')
print('(2) A 1GB file')
print('(3) A 10GB file')

try:
    # python 2
    choice = str(raw_input('Enter your choice: '))
except:
    # python 3
    choice = str(input('Enter your choice: '))

# 3 links for testing.
link1 = 'http://speed.hetzner.de/100MB.bin'
link2 = 'http://speed.hetzner.de/1GB.bin'
link3 = 'http://speed.hetzner.de/10GB.bin'

startTime = time.time()
if choice == '1':
    wget.download(link1)
elif choice == '2':
    wget.download(link2)
elif choice == '3':
    wget.download(link3)
else:
    print('there is no option {}'.format(choice))
    quit()

endTime = time.time() - startTime
endTime = round((endTime * 1000000), 3)
print('Download took {} microseconds'.format(str(endTime)))
