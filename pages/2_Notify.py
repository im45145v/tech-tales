import streamlit as st
import requests
import pymongo
from twilio.rest import Client as cl

account_sid = st.secrets["account_sid"]
auth_token = st.secrets["auth_token"]
twilio_phone_number = st.secrets["twilio_phone_number"]
client1 = cl(account_sid, auth_token)
client = pymongo.MongoClient(st.secrets["mclient"])
db = client["Tech_Tales"]
collection = db["comments"]

def main():
    st.title("User Records")

    # Get user ID from input
    search_id = st.text_input("Enter User ID to search",key="bingo_book")
    username = search_id

    if st.button("Search"):
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_records= dict(response.json())
            st.success("User ID found!")
            st.write("User ID:", username)
            st.write("Name:", user_records["name"])
            st.write("Email:", user_records["email"])
            st.write("Bio:", user_records["bio"])
        else:
            st.error("User ID not found!")
        
    number = st.text_input("Enter your phone number with country code (ex: 91xxxxxxxxxx)",key="madara", help="Important: This field cannot be  blank", type="default")

    # Button to save the input to the file
    if st.button("Save Input", key="hashirama"):
        if not number or number == "Please enter your phone number":
            st.warning("Please enter a valid phone number")
        else:
            add_number(username, number)
            st.success("You'll be reminded to this phone number once a new comment is added")
def add_number(username, number):
    collection.update_one(
        {"username": username},
        {"$push": {"number": number}}
    )
if __name__ == "__main__":
    main()
