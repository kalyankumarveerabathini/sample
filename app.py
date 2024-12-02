import streamlit as st

import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())


# Page Configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":tada:",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Content: Home
if page == "Home":
    st.title("Welcome to My Portfolio!")
    st.image("https://th.bing.com/th/id/R.71fc55a0f2becd702cc4a893980dea57?rik=XOUhz40Jc9OcYg&riu=http%3a%2f%2fthewowstyle.com%2fwp-content%2fuploads%2f2015%2f01%2fnature-images-6.jpg&ehk=BQoi8QCZQtCfHkXWT0TIAxv1vTtTO1rY7ctKskX6Xfs%3d&risl=&pid=ImgRaw&r=0", caption="This is me!", width=250)
    st.write("""
        Hi! I'm [Your Name], a passionate developer with expertise in Python, web development, and data science.
        Explore this portfolio to learn more about my projects and skills.
    """)

# Content: About
elif page == "About":
    st.title("About Me")
    st.write("""
        I'm a Python developer with a strong interest in creating innovative web applications,
        data analysis projects, and machine learning models. My expertise includes:
        - **Programming Languages**: Python, JavaScript
        - **Frameworks**: Flask, Streamlit, Django
        - **Tools**: Git, SQL, Tableau
        """)
    st.image("https://via.placeholder.com/800x400.png?text=My+Skills", caption="My Skillset")

# Content: Projects
elif page == "Projects":
    st.title("Projects")
    st.subheader("1. Data Visualization Dashboard")
    st.write("Created an interactive data dashboard using Streamlit and Plotly.")
    st.image("https://via.placeholder.com/800x400.png?text=Data+Visualization+Demo")
    
    st.subheader("2. E-commerce Website")
    st.write("Developed an e-commerce platform with Django and integrated payment gateway.")
    st.image("https://via.placeholder.com/800x400.png?text=E-commerce+Project")

# Content: Contact
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out!")
    st.write("- **Email**: your.email@example.com")
    st.write("- **GitHub**: [github.com/yourprofile](https://github.com/yourprofile)")
    st.write("- **LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")

    # Contact form
    st.subheader("Send me a message")
    name = st.text_input("Name")
    message = st.text_area("Message")
    if st.button("Send"):
        st.success(f"Thank you, {name}! I'll get back to you soon.")
