import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import uuid
import numpy
from htbuilder import div, big, h2, styles
from htbuilder.units import rem
from util.QRS_util import*
COLOR_RED = "#FF4B4B"
COLOR_BLUE = "#1C83E1"
COLOR_CYAN = "#00C0F2"
# read csv from a github repo
def display_dial(title, value, color):
        st.markdown(
            div(
                style=styles(
                    text_align="center",
                    color=color,
                    padding=(rem(0.8), 0, rem(3), 0),
                )
            )(
                h2(style=styles(font_size=rem(0.8), font_weight=600, padding=0))(title),
                big(style=styles(font_size=rem(3), font_weight=800, line_height=1))(
                    value
                ),
            ),
            unsafe_allow_html=True,
        )
st.set_page_config(
    page_title = 'Real-Time ECG Monitoring Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.header("Real-Time ECG Monitoring Dashboard")

# top-level filters 

# # creating a single-element container.
placeholder = st.empty()
import serial
import time
import re
import time
import plotly.graph_objects as go
# try:
ser = serial.Serial('COM5',9600)
lst=[]
r=[]
r_peaks=[]
rpeakslst=[]
# filename = uuid.uuid1().hex
# filename="static\\"+filename+".dat"
def test():
	t_tmpend = time.time() + 1/60 
	while time.time() < t_tmpend:
		b = str(ser.readline())
		print(b)
		tmp = ""
		for m in b:
			if m.isdigit():
				tmp = tmp + m
		if(tmp==''):
			tmp=float(0)
		else :
			tmp=float(tmp)
		lst.append(tmp)
		rpeakslst.append(tmp)
		print(len(rpeakslst))
		lst.pop(0)
def run():
	t_tmpend = time.time() + 5 
	while time.time() < t_tmpend:
		b = str(ser.readline())
		tmp = ""
		for m in b:
			if m.isdigit():
				tmp = tmp + m
		if(tmp==''):
			tmp=float(0)
		else :
			tmp=float(tmp)
		lst.append(tmp)
	t_end = time.time() + 60 
	while time.time() < t_end:
	    with placeholder.container():
	        test()
	        st.line_chart(lst)
	        # st.write(fig2)
run()
# filename = uuid.uuid1().hex
# filename="static\\"+filename+".dat"
# savefile(filename,rpeakslst)
r,index=EKG_QRS_detect(numpy.array(rpeakslst))
hzl=[]
for i in range(1,len(r)):
	dif=r[i]-r[i-1]
	dif=dif/(index)
	hz=300/dif	
	print(hz)
	hzl.append(hz)
print(hzl)  
print(len(hzl))   
a,b =st.columns(2) 
with a:
	display_dial(
	    "Average Heart rate", f"{int(sum(hzl)/len(hzl))}", COLOR_CYAN
	)
with b :
	display_dial(
				        "Practical Heart Rate", f"{len(r)}", COLOR_RED
			    )
st.header("Analysis of Practical and Calculated Data")
import matplotlib.pyplot as plt
plt1=plt.figure(figsize=(3,2))
plt.plot(hzl)
r_peaks_data=[]
for i in range(len(hzl)):
	r_peaks_data.append(len(r))
plt.plot(r_peaks_data)
st.pyplot(plt)
