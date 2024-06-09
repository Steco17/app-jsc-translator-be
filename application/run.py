from glob import escape
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import awsgi
from application.manage_globals.main import translate
from application.library.db_languages import global_lang, local_lang

app = Flask(__name__)
CORS(app)

# Define valid API keys
VALID_API_KEYS =  'jsc@20231104'

@app.before_request
def validate_api_key():
    """
    Before each request, this function validates the API key.
    """
    # Extract the API key from the request headers
    api_key = request.headers.get('Authorization')
    api_key = request.headers.add("Access-Control-Allow-Origin", "*")

    # Check if the API key is provided and matches the expected key
    if not api_key or api_key != f'Bearer {VALID_API_KEYS}':
        # If the API key is missing or incorrect, return a 401 Unauthorized response
        return jsonify({'error': 'Unauthorized No key'}), 401

@app.route('/')
def index():
    return render_template('index.html')

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

@app.route('/languages/global', methods=['GET', 'OPTIONS'])
def intl_language():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight request successful'}), 200
    
    return global_lang

@app.route('/languages/local', methods=['GET', 'OPTIONS'])
def local_language():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight request successful'}), 200
    
    return local_lang

@app.route('/translate', methods=['POST', 'GET', 'OPTIONS'])
def intitiate_translation():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight request successful'}), 200
    
    lang_global = escape(request.args.get('globalLang'))
    lang_local = escape(request.args.get('localLang'))
    dataset = escape(request.args.get('dataText'))
    
    return translate(lang_global, lang_local, dataset)