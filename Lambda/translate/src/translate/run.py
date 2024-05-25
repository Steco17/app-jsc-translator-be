from flask import Flask, jsonify, render_template, request
from translate.library.db_languages import global_lang, local_lang
from translate.manage_globals.main import translate

app = Flask(__name__)

# Define valid API keys
VALID_API_KEYS = "jsc@20231104"


@app.before_request
def validate_api_key():
    """
    Before each request, this function validates the API key.
    """
    # Extract the API key from the request headers
    api_key = request.headers.get("Authorization")

    # Check if the API key is provided and matches the expected key
    if not api_key or api_key != f"Bearer {VALID_API_KEYS}":
        # If the API key is missing or incorrect, return a 401 Unauthorized response
        return jsonify({"error": "Unauthorized No key"}), 401


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/languages/global", methods=["GET"])
def intl_language():
    return global_lang


@app.route("/languages/local", methods=["GET", 'OPTIONS'])
def local_language():
    if request.method == 'OPTIONS':
        # Handle preflight request
        headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
            'Access-Control-Allow-Methods': 'OPTIONS, GET, POST, PUT, DELETE',  # Adjust allowed methods
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',  # Adjust allowed headers
            'Access-Control-Max-Age': '3600'  # Cache preflight response for 1 hour
        }
        return ('', 204, headers)
    elif request.method == 'GET':
        return local_lang
    else:
        return jsonify({'error': 'Method not allowed'}), 405
   

@app.route("/translate", methods=["POST", "GET"])
def intitiate_translation():
    lang_global = request.args.get("globalLang")
    lang_local = request.args.get("localLang")
    dataset = request.args.get("dataText")

    return translate(lang_global, lang_local, dataset)
