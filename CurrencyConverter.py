import streamlit as st
from PIL import Image
img = Image.open("currency.jpg")
st.image(img, width=700)
st.title("Naira Converter")
st.header("A simple currency converter that converts naira only to US dollars, pounds and euros")
st.subheader("Exchange rates as of 10th February, 2022")
st.subheader("1 USD = 416.87 naira")
st.subheader("1 GBP = 568.10 naira")
st.subheader("1 EUR = 478.59 naira")
amount = st.number_input("Enter your amount in naira")
desiredCurrency = st.radio("Select the currency that you want to convert naira to: ", ("dollars", "pounds", "euros"))
currencySymbols = ["$", "£", "€"] 
if (desiredCurrency == "dollars"):
    try:
        convertedCurrency = amount / 416.87
        currencySymbol = currencySymbols[0]
    except:
        st.text('Please select your desired currency')
elif (desiredCurrency == "pounds"):
    try:
        convertedCurrency = amount / 568.19
        currencySymbol = currencySymbols[1]
    except:
        st.text('Please select your desired currency')
else:
    try:
        convertedCurrency = amount / 478.59
        currencySymbol = currencySymbols[2]
    except:
         st.text('Please select your desired currency')
convertedCurrency =  round(convertedCurrency, 2)             
if(st.button("Convert your naira")):
    st.text('The naira equivalent of ₦{} is {}{}.' .format(amount, currencySymbol, convertedCurrency))
    st.success("You have successfully converted your naira!")
        
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)        
        