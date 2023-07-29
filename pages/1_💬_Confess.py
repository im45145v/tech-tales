import streamlit as st
import requests
from mongodb_connection import MongoConnect
from twilio.rest import Client as cl
import pymongo

account_sid = st.secrets["account_sid"]
auth_token = st.secrets["auth_token"]
twilio_phone_number = st.secrets["twilio_phone_number"]
client1 = cl(account_sid, auth_token)

# The MongoDB connection
client= st.experimental_connection('mongo', type=MongoConnect, host=st.secrets['mclient'])

db = "Tech_Tales"
collection = "comments"

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

    # Comment box for the user
    comment = st.text_input("Enter Comment" , key="itachi")

    if st.button("Add Comment" , key="naruto"):
        if check_user_exists(username):
            add_comment(username, comment)
            st.success("Comment added successfully!")
        else:
            insert_user(username, comment)
            st.warning("User does not exist.")

    if st.button("Show Comments" , key="minato"):
        if check_user_exists(username):
            retrieve_comments(username)
        else:
            st.warning("No comments found for the user.")

def add_comment(username, comment):
    client.update_one(db, collection,
        {"username": username},
        {"$addToSet": {"comments": comment}}
    )

    # Get the updated document using find_one
    user_document = client.find_one(db, collection, {"username": username})
    if user_document:
        numbers = user_document.get("number", [])  # Changed "numbers" to "number"
        for number in numbers:
            # Customize the SMS content as needed
            sms_body = f"Hello Watcher, {username} got a new comment: {comment}"
            send_sms(number, sms_body)

def add_number(username, number):
    client.update_one(db, collection,
        {"username": username},
        {"$addToSet": {"number": number}}
    )

def insert_user(username, comment):
    user_data = {
        "username": username,
        "comments": [comment],
        "number": []
    }
    client.insert_one(db, collection, user_data)


def send_sms(to_number, body):
    try:
        message = client1.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=f"+{to_number}"
        )
        print(f"SMS sent successfully to {to_number}. Message SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Failed to send SMS to {to_number}. Error: {str(e)}")


def retrieve_comments(username):
    user_data = client.find_one(db, collection, {"username": username})
    # st.write(user_data)
    comments = user_data.get("comments", [])
    for each_comment in comments:
        st.write(each_comment)

def check_user_exists(username):
    user_data = client.find_one(db, collection, {"username": username})
    # st.write(user_data)
    if user_data:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
