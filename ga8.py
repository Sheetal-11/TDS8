import streamlit as st

def find_largest(a,b,c):
    """
    This function takes three values as input and returns the largest value among them.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the Largest Number")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    largest_num = find_largest(a,b,c)
    st.write(f"The largest number is: {largest_num}")
