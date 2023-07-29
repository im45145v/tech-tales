import streamlit as st


def main():
    st.markdown("""
    <div style='text-align: center;'>
        <h1>Tech-Tales</h1>
    </div>
    """, unsafe_allow_html=True)

    url = "https://i.ibb.co/FYgXtTZ/3d-rendering-emotions.jpg"

    # Center the image using CSS 'text-align' property
    st.markdown(f'<div style="text-align: center;"><img src="{url}" width="200"></div>', unsafe_allow_html=True)

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
