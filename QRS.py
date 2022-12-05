import os
import sys
from util.QRS_util import*

'''
QRS detection demo 
@author: Kemeng Chen: kemengchen@email.arizona.edu
'''

def QRS_test(file_name):
	'''
	QRS detection on file_name
	assuming 360 Hz sampling rate, may not work with very low sampling rate signal
	args:
		file_name: file containing ecg data in one column
	'''
	fs=360
	file_path=os.path.join(os.getcwd(), '', file_name)
	if not os.path.isfile(file_path):
		raise AssertionError(file_path, 'not exists')
	ecg=read_ecg(file_path)
	R_peaks, S_pint, Q_point,ecg,index=EKG_QRS_detect(ecg, fs, True, True)
	return R_peaks,index[-1]
