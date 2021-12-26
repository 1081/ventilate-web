import streamlit as st
import numpy as np
import pandas as pd
import time


st.subheader("Dew point contol")

# if st.button("test"):
#     t = st.title("Fenster schließen")

# outside = st.container()
# inside = st.container()

# with outside:
#     st.subheader("Outside")
#     st.metric("Temperature", "70 °C")
#     st.metric("Humidity", "86%")
#     st.metric("Water", "33 g")

# with inside:
#     st.subheader("Inside")
#     st.metric("Temperature", "70 °C", "1.2 °C")
#     st.metric("Humidity", "86%", "4%")
#     st.metric("Water", "21 g", "1 g")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Outside")
    st.metric("Temperature", "70 °C")
    st.metric("Humidity", "86%")
    st.metric("Water", "33 g")

with col2:
    st.subheader("Inside")
    st.title("70 °C")
    st.markdown("### Inside")
    st.markdown("# 70 °C")
    st.subheader("Inside")
    st.metric("Temperature", "70 °C", "1.2 °C")
    st.metric("Humidity", "86%", "4%")
    st.metric("Water", "21 g", "1 g")

# col1.outside
# col2.inside


# h1.subheader("Inside")
# col1.metric("Temperature", "70 °C", "1.2 °C")
# col2.metric("Humidity", "86%", "4%")
# col3.metric("Water", "21 g", "1 g")

# st.subheader("Outside")
# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °C")
# col2.metric("Humidity", "86%")
# col3.metric("Water", "33 g")


# st.title("Open window!")

# st.write("Auto updates every 60 seconds.")


# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)


# with st.spinner("Wait for it..."):
#     time.sleep(5)
#     st.success("Done!")
