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
    client_headers = dict(request.headers)
    return global_lang, jsonify(client_headers)


@app.route("/languages/local", methods=["GET"])
def local_language():
    client_headers = dict(request.headers)
    return local_lang , jsonify(client_headers)
   

@app.route("/translate", methods=["POST", "GET"])
def intitiate_translation():

    lang_global = request.args.get("globalLang")
    lang_local = request.args.get("localLang")
    dataset = request.args.get("dataText")

    return translate(lang_global, lang_local, dataset)
