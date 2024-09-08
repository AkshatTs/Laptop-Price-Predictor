import streamlit as st
import pickle
import numpy as np
import pandas as pd

#import the model
pipe = pickle.load(open('pipe.pkl','rb'))
laptop_data = pickle.load(open('laptop_data.pkl','rb'))

st.title("Laptop Price Predictor")

#brand
company = st.selectbox('Brand',laptop_data['Company'].unique())

#type of laptop
type = st.selectbox('Type',laptop_data['TypeName'].unique())

#Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#Weight
weight = st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

#IPS
ips = st.selectbox('IPS',['No','Yes'])

#screen size
#screen_size = st.number_input('Screen Size')
screen_size = st.number_input("Enter screen size (in inches)", min_value=0.1, value=0.1)


#Resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2568x1600','2568x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',laptop_data['Cpu brand'].unique())

#hdd
hdd = st.selectbox('HDD(in GB)',[0,8,128,256,512,1024,2048])

#ssd
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

#gpu
gpu = st.selectbox('GPU',laptop_data['Gpu brand'].unique())

#os
os = st.selectbox('OS',laptop_data['os'].unique())

X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

if touchscreen == 'Yes':
        touchscreen = 1
else:
        touchscreen = 0
    
if ips == 'Yes':
        ips = 1
else:
        ips = 0

query_dict = {
    'Company': [company],
    'TypeName': [type],
    'Ram': [ram],
    'Weight': [weight],
    'Touchscreen': [touchscreen],
    'Ips': [ips],
    'ppi': [ppi],
    'Cpu brand': [cpu],
    'HDD': [hdd],
    'SSD': [ssd],
    'Gpu brand': [gpu],
    'os': [os]
}

query = pd.DataFrame(query_dict)

if st.button('Predict Price'):
    #query
    #query = query.reshape(1,12)
    predicted_price = pipe.predict(query)
    st.title(f"The predicted price of the laptop is {int(np.exp(predicted_price[0]))}")
