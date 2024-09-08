import os
import streamlit as st
from cookiecutter.main import cookiecutter


def generate_project(project_name, project_type):
    """
    Generate a project using cookiecutter
    """
    # Fetch the Cookiecutter repository URL from environment variable
    COOKIECUTTER_REPO = os.environ.get("COOKIECUTTER_REPO")

    if not COOKIECUTTER_REPO:
        raise ValueError("The COOKIECUTTER_REPO environment variable is not set.")

    # Validate inputs
    if not project_name:
        raise ValueError("Project name is required.")
    if project_type not in ["data_science", "machine_learning", "web_app"]:
        raise ValueError("Invalid project type.")

    # Generate the project using Cookiecutter
    extra_context = {"project_name": project_name, "project_type": project_type}
    cookiecutter(COOKIECUTTER_REPO, extra_context=extra_context)


if __name__ == "__main__":
    st.title("Cookiecutter and Streamlit Integration")
    st.write("This is a demo of how to integrate Streamlit and Cookiecutter")

    project_name = st.text_input("Project Name:")
    project_type = st.selectbox("Project Type:", ["data_science", "machine_learning", "web_app"])

    if st.button("Generate Project"):
        try:
            generate_project(project_name, project_type)
            st.success("Project Generated Successfully")
        except Exception as e:
            st.error(f"Error: {e}")