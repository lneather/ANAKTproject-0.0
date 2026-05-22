import streamlit as st

st.title("🎈 ANAKT PROJECT")
st.write(
    "Welcome to ANAKT Garden Official Website!"
)
action = st.menu_button("MENU", options=["Warehouse", "Sponsorship", "Our Products"])
if action == "Warehouse":
    st.write("Loading A list of our warehouse all over the galaxy...")
elif action == "Sponsorship":
    st.write("Loading A list of our sponsor...")
elif action == "Our Products":
    st.write("Searching a top-quality product for you...")
