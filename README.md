# Text Annotation Application Prototype

This is a Streamlit-based web application for annotating text files. The application allows users to upload a text file, view it in a paginated format, annotate specific text fragments, and download the annotations as a JSON file.

## Features

- **Text File Upload**: Upload a `.txt` file to begin annotating.
- **Pagination**: View the uploaded text in a paginated format for easy navigation.
- **Text Annotation**: Annotate specific portions of the text with custom labels.
- **Annotation Preview**: See a preview of the annotated text with highlighted annotations.
- **Save Annotations**: Download the annotations as a JSON file.

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/) - Install via pip

### Installation

#### 1. Set Up a Virtual Environment (Optional but Recommended)

If you don't already have a virtual environment set up, follow these steps to create and activate one. This will ensure that all dependencies are installed in an isolated environment.

1. **Create a Virtual Environment**:
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     ```
   - On Windows:
     ```bash
     python -m venv venv
     ```

2. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

   You should now see `(venv)` in your terminal prompt, indicating that the virtual environment is active.

3. **Install Dependencies**:
   After activating the virtual environment, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
    ```

#### 2. If You Already Have the Project

1. Navigate to your project directory:
    ```bash
    cd path-to-your-project
    ```

2. Ensure all dependencies are installed:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Update the repository to the latest version:
    ```bash
    git pull origin main
    ```

### Running the Application

To run the application, use the following command:

```bash
streamlit run app.py
