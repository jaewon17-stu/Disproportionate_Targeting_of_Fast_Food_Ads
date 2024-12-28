import streamlit as st

st.markdown("# Comment Section")
st.sidebar.markdown("Community")



# Initialize session state to store comments if not already initialized
if 'comments' not in st.session_state:
    st.session_state.comments = []


import streamlit as st

# Title with larger font
st.markdown('<h2 style="font-size: 24px;">What are your insights on this issue?</h2>', unsafe_allow_html=True)


# Create a text input for the user to enter their name (simulating multiple users)
username = st.text_input("Enter your name:")

# Create a form for users to submit their comments
with st.form(key='comment_form', clear_on_submit=True):
    # Create a text area for users to enter comments
    user_comment = st.text_area("Write your comment:", "")

    # Submit button inside the form
    submit_button = st.form_submit_button(label="Submit Comment")

    # If the form is submitted (Enter is pressed or button clicked)
    if submit_button and user_comment:
        if username:  # Make sure the user has entered their name
            # Add the comment along with the username to session state
            st.session_state.comments.append({"username": username, "comment": user_comment})
            
        else:
            st.write("Please enter your name before submitting.")
    elif submit_button:
        st.write("Please write a comment before submitting.")

# Display all previous comments
if st.session_state.comments:
    st.write("Previous comments:")
    for entry in st.session_state.comments:
        if isinstance(entry, dict):
            st.write(f"{entry['username']}: {entry['comment']}")
