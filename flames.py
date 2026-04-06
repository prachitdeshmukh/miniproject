import streamlit as st

def calculate_flames(name1, name2):
    s1 = list(name1)
    s2 = list(name2)
    i = 0
    while i < len(s1):
        if s1[i] in s2:
            s2.remove(s1[i])
            s1.pop(i)
        else:
            i += 1

    n = len(s1) + len(s2)
    s = 'FLAMES'
    
    while len(s) > 1:
        i = n % len(s) - 1
        if i < 0:
            s = s[:len(s)-1]
        else:
            s = s[i+1:] + s[:i]
    return s

st.set_page_config(page_title="FLAMES Game", page_icon="🔥", layout="centered")
st.markdown("<h3 style='text-align: center; color: #FF5733;'>💖 FLAMES Relationship Game 💖</h3>", 
            unsafe_allow_html=True)

with st.form(key="flames_form"):
    st.markdown("### Enter the Names")
    name1 = st.text_input("Enter the first name:", placeholder="Name 1")
    name2 = st.text_input("Enter the second name:", placeholder="Name 2")
    submit_button = st.form_submit_button("Get Results 💌")

if submit_button:
    if name1 and name2:
        result = calculate_flames(name1, name2)
        relationships = {
            "F": "Friends 👫",
            "L": "Love ❤️",
            "A": "Affection 🤗",
            "M": "Marriage 💍",
            "E": "Enemies 😠",
            "S": "Siblings 👨‍👩‍👧‍👦",
        }
        relationship = relationships.get(result, "Unknown")

        st.markdown("<hr style='border: 1px solid #FF5733;'>", unsafe_allow_html=True)
        st.markdown(
            f"<h3 style='text-align: center; color: #28B463;'>The relationship is:</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h2 style='text-align: center; color: #FF5733;'>{relationship}</h2>",
            unsafe_allow_html=True,
        )
        st.balloons()
    else:
        st.error("Please enter both names to proceed.")
st.markdown("<hr style='border: 1px solid #2E86C1;'>", unsafe_allow_html=True)
