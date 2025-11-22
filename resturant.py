import streamlit as st
st.set_page_config(page_title="BUILD_A_BITE",layout="centered")
st.title("Build Your Own Bite")
st.caption("customize your perfect wrap with fresh veggies,sauses, and fillings")
veggies=st.multiselect(
    "select your veggies",
    ["Lettuce","Tomato","Onion","Corn","Cucumber","Capsicum"],
)
sauce = st.multiselect(
    "Choose your sauces ",
    ["Mayo", "Mint Chutney", "BBQ", "Cheese Sauce", "Peri Peri"],
)
wrap = st.selectbox(
    "Pick your base ",
    ["Whole Wheat Wrap", "Tortilla", "Plain Roti", "Bowl (no wrap)"],
)
stuffing = st.radio(
    "Choose your stuffing ",
    ["Paneer", "Chicken", "Tofu", "Veg Mix"],
)
if st.button("🍴 Create My Bite!"):
    if not veggies or not sauce or not wrap or not stuffing:
        st.warning("Yo, pick at least one from each category 😅")
    else:
        st.success("Here’s your custom bite 👇")
        st.write(f"Base: {wrap}")
        st.write(f"Stuffing: {stuffing}")
        st.write(f"Veggies: {', '.join(veggies)}")
        st.write(f"Sauces: {', '.join(sauce)}")