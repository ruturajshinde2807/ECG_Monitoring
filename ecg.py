import serial
import time
import re
import time
import struct
def savefile(filename,lis):
	with open(filename, 'w+') as f:
	     
	    # write elements of list
	    for items in lis:
	        f.write('%s\n' %items)
	     
	 
	# close the file
	f.close()