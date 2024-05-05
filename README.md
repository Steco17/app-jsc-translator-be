## Overview

Flask Translator App is a simple Flask application that translates text into a custom language using a JSON file with translation rules.

## Prerequisites

<table><tbody><tr><td><code><strong>TOOL &nbsp;&nbsp;</strong></code></td><td><code><strong>VERSION &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</strong></code></td></tr><tr><td><code>Python&nbsp;</code></td><td><code>3.12.2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</code></td></tr><tr><td><code>Docker</code></td><td>&nbsp;</td></tr><tr><td><code>Poetry</code></td><td><code>1.7.1</code></td></tr><tr><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>

## Installation

1.  **Clone the repository:**

```
   git clone https://https://github.com/Steco17/linear_JSC_translator.git
```

## Running the Flask Application

**Set the** `**FLASK_APP**` **environment variable:**

On macOS/Linux:

On Windows (cmd):

**Run the Flask application:**

**Open your web browser and visit** `**http://localhost:5000**` **to access the Flask application.**

## Building and Running Docker Image

**Build the Docker image:**

**Run the Docker container:**

**Open your web browser and visit** `**http://localhost:5000**` **to access the Flask application.**

## Posting a Translation Using Postman

To post a translation to the Flask application using Postman, follow these steps:

**Open Postman:** Launch the Postman application on your computer.

**Set Request Type:** Select the HTTP request type as `POST`.

**Set Request URL:** Enter the URL where your Flask application is hosted, followed by `/translate`. For example: `http://localhost:5000/translate`.

**Set Headers:**

- Add a header with key `Content-Type` and value `application/json`.
- If your application requires authentication, include a header with key `Authorization` and value `Bearer <your_access_token>`.

**Set Request Body:** Select the raw JSON option and enter the translation text in the following format:

**Send Request:** Click on the "Send" button to send the POST request.

**View Response:** The translated text will be returned in the response body.

**Note:** Make sure to replace `http://localhost:5000/translate` with the actual URL of your Flask application.

### Example Request

**Request Type:** POST

**Request URL:** http://localhost:5000/translate

**Headers:**

- Content-Type: application/json
- Authorization: Bearer

**Request Body:**

### Example Response

```
{
    "input_text": "night",
    "translated_text": "Nintu’ɨ"
```
