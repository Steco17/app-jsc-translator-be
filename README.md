## Overview

Flask Translator App is a simple Flask application that translates text into a custom language using a JSON file with translation rules.

## Prerequisites

Make sure you have the following software installed on your system:

- Python 3.x
- Docker

## Installation

1. **Clone the repository:**

```bash
   git clone https://https://github.com/Steco17/linear_JSC_translator.git
   ```


2. **Navigate to the project directory:**

   ```bash
   cd linear_JSC_translator
   ```

## Setting up Python Virtual Environment

1. **Create a Python virtual environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows (cmd):

     ```bash
     venv\Scripts\activate.bat
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask Application

1. **Set the `FLASK_APP` environment variable:**

   - On macOS/Linux:

     ```bash
     export FLASK_APP=app.py
     ```

   - On Windows (cmd):

     ```bash
     set FLASK_APP=app.py
     ```

2. **Run the Flask application:**

   ```bash
   python app/app.py 
   ```

3. **Open your web browser and visit `http://localhost:5000` to access the Flask application.**

## Building and Running Docker Image

1. **Build the Docker image:**

   ```bash
   docker build -t jsc-translator .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 jsc-translator
   ```

3. **Open your web browser and visit `http://localhost:5000` to access the Flask application.**

## Posting a Translation Using Postman

To post a translation to the Flask application using Postman, follow these steps:

1. **Open Postman:** Launch the Postman application on your computer.

2. **Set Request Type:** Select the HTTP request type as `POST`.

3. **Set Request URL:** Enter the URL where your Flask application is hosted, followed by `/translate`. For example: `http://localhost:5000/translate`.

4. **Set Headers:**
   - Add a header with key `Content-Type` and value `application/json`.
   - If your application requires authentication, include a header with key `Authorization` and value `Bearer <your_access_token>`.

5. **Set Request Body:** Select the raw JSON option and enter the translation text in the following format:
   
   ```json
   {
    "text": "night"
    }
   ```

6. **Send Request:** Click on the "Send" button to send the POST request.

7. **View Response:** The translated text will be returned in the response body.

**Note:** Make sure to replace `http://localhost:5000/translate` with the actual URL of your Flask application.

### Example Request

- **Request Type:** POST
- **Request URL:** http://localhost:5000/translate
- **Headers:**
  - Content-Type: application/json
  - Authorization: Bearer <your_access_token> 
- **Request Body:**
  
  ```json
  {
      "text": "night"
  }
  ```

### Example Response

```json
{
    "input_text": "night",
    "translated_text": "Nintu’ɨ"
}
```

## Continuous Integration (CI)

This project includes a CI/CD workflow that runs automated tests and builds Docker images on every push to the `main` branch and on every pull request targeting the `main` branch. Here's how to use it:

1. **Navigate to the `.github/workflows` directory:**

   ```bash
   cd .github/workflows
   ```

2. **Open the `ci.yml` file in a text editor:**

   ```bash
   code ci.yml
   ```

3. **Make any necessary adjustments to the CI workflow, such as test commands or Docker build options.**

4. **Commit and push your changes to trigger the CI workflow:**

   ```bash
   git add ci.yml
   git commit -m "Update CI workflow"
   git push origin main
   ```

5. **Monitor the CI workflow's progress on the "Actions" tab of your GitHub repository.**

## Contributing

Only for JSC

## License

This project is licensed under the JSC License.

This README section provides instructions for accessing and modifying the CI/CD workflow, making adjustments as necessary, and triggering the workflow to run automated tests and build Docker images. Adjust the paths and commands as needed to match your project's directory structure and workflow configuration.