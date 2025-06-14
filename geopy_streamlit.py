import streamlit as st
from geopy.geocoders import Nominatim
st.title("Geocoding program")

type = st.radio(options=["Reverse Geo", "Forward Geo"],label="Type")

if type == "Reverse Geo":
    lat = st.text_input("Latitude: ")
    long = st.text_input("Longitude: ")
    if st.button("Get Address"):
        geo=Nominatim(user_agent="geoapi")
        st.text(geo.reverse(f"{lat}, {long}"))
        
elif type == "Forward Geo":
    address = st.text_input("Address: ")
    if st.button("Get Lat, Long"):
        geo=Nominatim(user_agent="geoapi")
        st.text(f"Lat: {geo.geocode(address).latitude}, Long: {geo.geocode(address).longitude}")