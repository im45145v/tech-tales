
import streamlit as st 

st.title("------------------------------------------------")


import streamlit as st
import pandas as pd

# Create a dictionary to store user records and comments
user_records = {
    "user1": {
        "Name": "John Doe",
        "Email": "john@example.com",
        "Age": 30,
        "Comments": []
    },
    "user2": {
        "Name": "Jane Smith",
        "Email": "jane@example.com",
        "Age": 25,
        "Comments": []
    }
}

def add_comment(user_id, comment):
    if user_id in user_records:
        user_records[user_id]["Comments"].append(comment)
        return True
    else:
        return False

def main():
    st.title("User Records")

    # Get user ID from input
    search_id = st.text_input("Enter User ID to search")

    if st.button("Search"):
        if search_id in user_records:
            st.success("User ID found!")
            st.write("User ID:", search_id)
            st.write("Name:", user_records[search_id]["Name"])
            st.write("Email:", user_records[search_id]["Email"])
            st.write("Age:", user_records[search_id]["Age"])
            st.write("Comments:")
            comments = user_records[search_id]["Comments"]
            if comments:
                for comment in comments:
                    st.write("-", comment)
            else:
                st.write("No comments found.")
        else:
            st.error("User ID not found!")

    if st.button("Add Comment"):
        user_id = st.text_input("Enter User ID to add comment")
        comment = st.text_input("Enter Comment")

        if add_comment(user_id, comment):
            st.success("Comment added successfully!")
        else:
            st.error("User ID not found!")

if __name__ == "__main__":
    main()


st.title("--------------------------------")


import streamlit as st
import pandas as pd

# Create a dictionary to store user records and comments
user_records = {
    "user1": {
        "Name": "John Doe",
        "Email": "john@example.com",
        "Age": 30,
        "Comments": []
    },
    "user2": {
        "Name": "Jane Smith",
        "Email": "jane@example.com",
        "Age": 25,
        "Comments": []
    }
}

def add_comment(user_id, comment):
    if user_id in user_records:
        user_records[user_id]["Comments"].append(comment)
        return True
    else:
        return False

def main():
    st.title("User Records")

    # Get user ID from input
    search_id = st.text_input("Enter User ID to search" , key="search")

    if st.button("Search"  , key="search25"):
        if search_id in user_records:
            st.success("User ID found!")
            st.write("User ID:", search_id)
            st.write("Name:", user_records[search_id]["Name"])
            st.write("Email:", user_records[search_id]["Email"])
            st.write("Age:", user_records[search_id]["Age"])

            # Comment box for the searched user
            comment = st.text_area("Add Comment")

            if st.button("Add Comment", key="comment"):
                if add_comment(search_id, comment):
                    st.success("Comment added successfully!")
                else:
                    st.error("Failed to add comment!")
        else:
            st.error("User ID not found!")

    if st.button("Show Records"):
        st.write(user_records)

if __name__ == "__main__":
    main()



st.title("--------------------------------")

import streamlit as st
import os

# Create a folder to store user comments
if not os.path.exists("user_comments"):
    os.makedirs("user_comments")

def add_comment(user_id, comment):
    # Create a text file for the user if it doesn't exist
    file_path = f"user_comments/{user_id}.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass

    # Append the comment to the user's text file
    with open(file_path, "a") as file:
        file.write(f"{comment}\n")

def main():
    st.title("User Comments")

    # Get user ID from input
    user_id = st.text_input("Enter User ID")

    # Comment box for the user
    comment = st.text_input("Enter Comment")

    if st.button("Add Comment" , key="Add Comment21"):
        add_comment(user_id, comment)
        st.success("Comment added successfully!")

    if st.button("Show Comments"):
        file_path = f"user_comments/{user_id}.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                comments = file.read()
            st.write(f"Comments for User ID: {user_id}")
            st.write(comments)
        else:
            st.warning("No comments found for the user.")

if __name__ == "__main__":
    main()


st.title("--------------------------------")

import streamlit as st
import os

# Create a folder to store user comments
if not os.path.exists("user_comments"):
    os.makedirs("user_comments")

def add_comment(user_id, comment):
    # Check if the user exists
    if user_exists(user_id):
        # Create a text file for the user if it doesn't exist
        file_path = f"user_comments/{user_id}.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        # Append the comment to the user's text file
        with open(file_path, "a") as file:
            file.write(f"{comment}\n")
        return True
    else:
        return False

def user_exists(user_id):
    # Check if the user ID exists in the database
    # Replace this with your logic to check the user ID in the database
    user_records = ["user1", "user2","sri"]
    return user_id in user_records

def main():
    st.title("User Comments")

    # Get user ID from input
    user_id = st.text_input("Enter User ID" , key="user_id")

    # Comment box for the user
    comment = st.text_input("Enter Comment" , key="comment58")

    if st.button("Add Comment" , key="Create"):
        if add_comment(user_id, comment):
            st.success("Comment added successfully!")
        else:
            st.warning("User does not exist.")

    if st.button("Show Comments" , key="dingg"):
        if user_exists(user_id):
            file_path = f"user_comments/{user_id}.txt"
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    comments = file.read()
                st.write(f"Comments for User ID: {user_id}")
                st.write(comments)
            else:
                st.warning("No comments found for the user.")
        else:
            st.warning("User does not exist.")

if __name__ == "__main__":
    main()
