import streamlit as st
import requests
from mongodb_connection import MongoConnect
from twilio.rest import Client as cl

account_sid = st.secrets["account_sid"]
auth_token = st.secrets["auth_token"]
twilio_phone_number = st.secrets["twilio_phone_number"]
client1 = cl(account_sid, auth_token)

# The MongoDB connection
client= st.experimental_connection('mongo', type=MongoConnect, host=st.secrets['mclient'])

db ="Tech_Tales"
collection ="comments"

def main():
    st.title("User Records")

    # Get user ID from input
    search_id = st.text_input("Enter User ID to search",key="bingo_book")
    username = search_id

    if st.button("Search"):
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_records = dict(response.json())
            url_image = user_records["avatar_url"]
            circular_image_style = """<style>
                    .circle-img {object-fit: cover;border-radius: 50%;}
                    .circle-img img {object-fit: cover;border-radius: 50%;width: 150px;height: 150px;}
                    </style> """
            st.markdown(circular_image_style, unsafe_allow_html=True)
            st.markdown(f'<div class="circle-img"><img src="{url_image}"></div>', unsafe_allow_html=True)
            st.write("User ID:", username)
            st.write("Name:", user_records["name"])
            st.write("Email:", user_records["email"])
            st.write("Bio:", user_records["bio"])
        else:
            st.error("User ID not found!")
    # Text input box with an important message in red color
    number = st.text_input("Enter your phone number with country code (ex: 91xxxxxxxxxx)",key="madara", help="Important: This field cannot be  blank", type="default")

    # Button to save the input to the file
    if st.button("Save Input", key="hashirama"):
        if not number or number == "Please enter your phone number":
            st.warning("Please enter a valid phone number")
        else:
            add_number(username, number)
            st.success("You'll be reminded to this phone number once a new comment is added")

def add_number(username, number):
    client.update_one(db, collection, 
        {"username": username},
        {"$push": {"number": number}}
    )
if __name__ == "__main__":
    main()
