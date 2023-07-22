import streamlit as st 
import requests
import pymongo

from datetime import datetime

# Assuming you have a MongoDB connection and a collection object
# Set up the MongoDB connection and collection
client = pymongo.MongoClient("mongodb+srv://21311a6611:Waffle@cluster0.ub5pbd6.mongodb.net/")
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


    # Comment box for the user
    comment = st.text_input("Enter Comment" , key="itachi")

    if st.button("Add Comment" , key="naruto"):
        if check_user_exists(username):
            add_comment(username,comment)
            st.success("Comment added successfully!")
        else:
            insert_user(username,comment)
            st.warning("User does not exist.")

    if st.button("Show Comments" , key="minato"):
        if check_user_exists(username):
            retrieve_comments(username)
        else:
            st.warning("No comments found for the user.")
            
        
            
        #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        


    # Text input box with an important message in red color
    number = st.text_input("Enter your phone number",key="madara", help="Important: This field cannot be  blank", type="default")
    # Button to save the input to the file
    if st.button("Save Input", key="hashirama"):
        if not number or number == "Please enter your phone number":
            st.warning("Please enter a valid phone number")
        else:
            add_number(username,number)

            st.success("you'll be reminded to this phone number once a new comment is added")

    


def add_comment(username, comment):
    collection.update_one(
        {"username": username},
        {"$push": {"comments": comment}}
    )
    #numbers = collection.find({"username": username}).get("numbers",[])
    #if numbers:
        #for number in numbers:
           # number

  
    


def add_number(username, number):
    collection.update_one(
        {"username": username},
        {"$push": {"number": number}}
    )


def insert_user(username, comment):
    user_data = {
        "username": username,
        "comments": [comment],
        "number": []
    }
    collection.insert_one(user_data)



def retrieve_comments(username):
    user_data = collection.find_one({"username": username})
    comments = user_data.get("comments", [])
    for each_comment in comments:
        st.write(each_comment)


def check_user_exists(username):
    user_data = collection.find_one({"username": username})
    if user_data:
        return True
    else:
        return False


    
if __name__ == "__main__":
    main()






