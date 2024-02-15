import streamlit as st


def main():
    st.title("School Website Template")
    st.sidebar.title("Navigation")

    page = st.sidebar.radio("Go to", ["Home", "Courses", "Faculty", "Events", "Contact"])

    if page == "Home":
        st.header("Welcome to Our School")
        st.write("This is the home page of our school website. Feel free to explore!")

    elif page == "Courses":
        st.header("Courses Offered")
        courses = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry"]
        st.write("Check out the courses we offer:")
        for course in courses:
            st.write("- " + course)

    elif page == "Faculty":
        st.header("Faculty Members")
        faculty = {
            "John Doe": "Computer Science",
            "Jane Smith": "Mathematics",
            "Mike Johnson": "Physics",
            "Emily Brown": "Biology",
            "David Lee": "Chemistry"
        }
        st.write("Meet our faculty:")
        for name, department in faculty.items():
            st.write("- " + name + " (" + department + ")")

    elif page == "Events":
        st.header("Upcoming Events")
        events = [
            {"title": "Science Fair", "date": "February 20, 2024"},
            {"title": "Parent-Teacher Conference", "date": "March 5, 2024"},
            {"title": "Sports Day", "date": "April 10, 2024"}
        ]
        st.write("Don't miss out on these events:")
        for event in events:
            st.write("- " + event["title"] + " (" + event["date"] + ")")

    elif page == "Contact":
        st.header("Contact Us")
        st.write("You can reach us at:")
        st.write("- Phone: 123-456-7890")
        st.write("- Email: info@ourschool.com")
        st.write("- Address: 123 School St, City, Country")


if __name__ == "__main__":
    main()
