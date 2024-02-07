import streamlit as st

# Layout for the form 
with st.form("myform", clear_on_submit=True):

    "### A form"

    # These exist within the form but won't wait for the submit button
    placeholder_for_selectbox = st.empty()
    placeholder_for_optional_text = st.empty()

    # Other components within the form will actually wait for the submit button
    radio_option = st.radio("Select number", [1, 2, 3], horizontal=True)
    submit_button = st.form_submit_button("Submit!")

# Create selectbox
with placeholder_for_selectbox:
    options = [f"Option #{i}" for i in range(3)] + ["Another option..."]
    selection = st.selectbox("Select option", options=options, index=None)

# Create text input for user entry
with placeholder_for_optional_text:
    if selection == "Another option...":
        otherOption = st.text_input("Enter your other option...")

# Code below is just to show the app behavior
with st.sidebar:

    "#### Notice that our `st.selectbox` doesn't really wait for `st.form_submit_button` to be clicked to update its value"
    st.warning(f"`st.selectbox` = *{selection}*")

    "#### But the other components within `st.form` do wait for `st.form_submit_button` to be clicked to update their value"
    st.info(f"`st.radio` = {radio_option}")

    "----"
    "#### It's better to condition the app flow to the form_submit_button... just in case"
    if submit_button:
        print(st.session_state)
        
        if selection != "Another option...":
            st.info(
                f":white_check_mark: The selected option is **{selection}** and the radio button is **{radio_option}**")
        else:
            st.info(
                f":white_check_mark: The written option is **{otherOption}** and the radio button is **{radio_option}** ")
    else:
        st.error("`st.form_submit_button` has not been clicked yet")