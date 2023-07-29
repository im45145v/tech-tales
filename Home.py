import streamlit as st 
import requests
import pymongo
from twilio.rest import Client as cl

#account_sid = st.secrets["account_sid"]
#auth_token = st.secrets["auth_token"]
#twilio_phone_number = st.secrets["twilio_phone_number"]
#client1 = cl(account_sid, auth_token)
#client = pymongo.MongoClient(st.secrets["mclient"])
#db = client["Tech_Tales"]
#collection = db["comments"]
def main():
    st.markdown("""
    <div style='text-align: center;'>
        <h1>Tech-Tales</h1>
    </div>
    """, unsafe_allow_html=True)
    url="https://i.ibb.co/FYgXtTZ/3d-rendering-emotions.jpg"
    st.image(url)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
        <h4> Ever wondered about the person behind the code?</h4>
        <h5>With TechTales, you can now access personal information such as names, emails, and bio of GitHub users, shared willingly by them in the spirit of openness and connection.</h5>
        <br>
        <h5>TechTales enables anonymous commenting on GitHub profiles, allowing you to share your thoughts, feedback, and encouragement without revealing your identity. And here's the kicker - you can even opt-in to associate your phone number with a GitHub user, and receive real-time SMS notifications whenever someone leaves a comment on their profile</h5>
    </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
