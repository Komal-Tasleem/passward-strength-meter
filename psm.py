import streamlit as st

st.title("🔐 Password Strength Meter")

# User Input for Password
password = st.text_input("Enter your password:", type="password")

# Button for Checking Password Strength
if st.button("Check Strength"):
    # Initialize score and feedback
    score = 0
    suggestions = []

    # Check password criteria
    if password:
        if len(password) >= 8:
            score += 1
        else:
            suggestions.append("Use at least 8 characters.")

        if any(char.isupper() for char in password):
            score += 1
        else:
            suggestions.append("Include at least one uppercase letter.")

        if any(char.islower() for char in password):
            score += 1
        else:
            suggestions.append("Include at least one lowercase letter.")

        if any(char.isdigit() for char in password):
            score += 1
        else:
            suggestions.append("Include at least one digit (0-9).")

        if any(char in "!@#$%^&*" for char in password):
            score += 1
        else:
            suggestions.append("Include at least one special character (!@#$%^&*).")

        # Determine Strength Level
        if score == 5:
            strength = "🟢 Strong"
            color = "green"
        elif 3 <= score < 5:
            strength = "🟡 Moderate"
            color = "orange"
        else:
            strength = "🔴 Weak"
            color = "red"

        # Display Strength Score
        st.markdown(f"### **Password Strength: <span style='color:{color};'>{strength}</span>**", unsafe_allow_html=True)
        st.write(f"**Score: {score}/5**")

        # Show Suggestions
        if score < 5:
            st.subheader("❌ Suggestions to Improve:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

        # Success Message
        if score == 5:
            st.success("✅ Great job! Your password meets all security requirements.")
    else:
        st.warning("⚠️ Please enter a password first!")


