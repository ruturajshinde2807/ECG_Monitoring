import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import uuid
from htbuilder import div, big, h2, styles
from htbuilder.units import rem
from ecg import*
from QRS import*
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
ser = serial.Serial('COM6',9600)
lst=[]
hzl=[]
r=[]
r_peaks=[]
rpeakslst=[]
filename = uuid.uuid1().hex
filename="static\\"+filename+".dat"
def test():
	t_tmpend = time.time() + 1/60 
	while time.time() < t_tmpend:
		b = str(ser.readline())
		tmp = ""
		for m in b:
			if m.isdigit():
				tmp = tmp + m
		lst.append(float(tmp))
		rpeakslst.append(float(tmp))
		print(len(rpeakslst))
		lst.pop(0)
	return lst
def run():
	t_tmpend = time.time() + 5 
	while time.time() < t_tmpend:
		b = str(ser.readline())
		tmp = ""
		for m in b:
			if m.isdigit():
				tmp = tmp + m
		rpeakslst.append(float(tmp))
		lst.append(float(tmp))
	t_end = time.time() + 60 
	while time.time() < t_end:
	    with placeholder.container():
	        tt=test()
	        savefile(filename,lst)
	        r_peaks,index=QRS_test(filename)
	        dif=r_peaks[-1]-r_peaks[-2]
	        dif=dif/(5*index)
	        hz=1500/dif	
	        hzl.append(hz)        
	        polarity_color = COLOR_BLUE
	        subjectivity_color = COLOR_RED
	        line_color=COLOR_CYAN
	        a, b= st.columns(2)
	        with a:
	        	display_dial("Heart rate in BPM", f"{hz}", polarity_color)
	        with b:
	        	display_dial(
			        "Average Heart rate", f"{sum(hzl)/len(hzl)}", line_color
			    )
	        st.line_chart(tt)
	        # st.write(fig2)
run()
filename = uuid.uuid1().hex
filename="static\\"+filename+".dat"
savefile(filename,rpeakslst)
r,index=QRS_test(filename)
display_dial(
			        "Practical Heart Rate", f"{len(r)}", COLOR_RED
			    )

