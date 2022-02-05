import streamlit as st
from PIL import Image
img = Image.open("calculator-image.jpg")
st.image(img, width=600)
st.title("Currency Converter")
st.header("This app is designed to convert naira to US dollars, pounds and euros.")
amount = st.number_input("Enter your amount in naira")
desiredCurrency = st.radio("Select the currency you want to convert naira to: ", ("dollars", "pounds", "euros"))
if (desiredCurrency == "dollars"):
    try:
        convertedCurrency = amount / 416.20
    except:
        st.text('Please select your desired currency')
elif (desiredCurrency == "pounds"):
    try:
        convertedCurrency = amount / 563.44
    except:
        st.text('Please select your desired currency')
else:
    try:
        convertedCurrency = amount / 476.51
    except:
         st.text('Please select your desired currency')
            
if(st.button("Convert your naira")):
    st.text('Your naira equivalent in {} is {}.' .format(desiredCurrency, convertedCurrency))
    st.success("You have successfully converted your naira")
        
        