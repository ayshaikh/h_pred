import streamlit as st
import joblib
import numpy as np


model = joblib.load('house_price_model.pkl')

st.title('House Price Prediction')

area = st.number_input('Area (in sq ft)', min_value=0, step=1)
bedrooms = st.number_input('Bedrooms', min_value=1, step=1)
bathrooms = st.number_input('Bathrooms', min_value=1, step=1)
stories = st.number_input('Stories', min_value=1, step=1)
mainroad = st.selectbox('Is the house on the main road?', ('yes', 'no'))
guestroom = st.selectbox('Does the house have a guestroom?', ('yes', 'no'))
basement = st.selectbox('Does the house have a basement?', ('yes', 'no'))
hotwaterheating = st.selectbox('Does the house have hot water heating?', ('yes', 'no'))
airconditioning = st.selectbox('Does the house have air conditioning?', ('yes', 'no'))
parking = st.selectbox('Is there parking?', ('yes', 'no'))
prefarea = st.selectbox('Is the house in a preferable area?', ('yes', 'no'))
furnishingstatus = st.selectbox('Furnishing status', ('semi-furnished', 'unfurnished'))

mainroad = 1 if mainroad == 'yes' else 0
guestroom = 1 if guestroom == 'yes' else 0
basement = 1 if basement == 'yes' else 0
hotwaterheating = 1 if hotwaterheating == 'yes' else 0
airconditioning = 1 if airconditioning == 'yes' else 0
parking = 1 if parking == 'yes' else 0
prefarea = 1 if prefarea == 'yes' else 0
furnishingstatus_semi = 1 if furnishingstatus == 'semi-furnished' else 0
furnishingstatus_unfurnished = 1 if furnishingstatus == 'unfurnished' else 0

features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                      hotwaterheating, airconditioning, parking, prefarea, furnishingstatus_semi, furnishingstatus_unfurnished]])

predicted_price = model.predict(features)

st.write(f'Predicted House Price: {predicted_price[0]:,.2f}')
