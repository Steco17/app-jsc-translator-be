from flask import request, jsonify
from nltk import word_tokenize
from nltk.translate import AlignedSent, IBMModel1
from nltk.corpus import comtrans
import pandas as pd
import re
import os
import csv
import json

# Init path for the requested language
def init_translation_path(input_language, output_language):
    # Specify the path to the directory where the CSV file is located
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(current_dir)
    lib_folder = 'library'
    # file_name = "mandouka_abo_nord.csv"
    file_name = input_language + "_" + output_language + ".csv"
    file_path = os.path.join(parent_dir, lib_folder, file_name)
    
    return file_path

def clean_sentences(sentences):
    # cleaned_sentences = word_tokenize(sentences)
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        # sentence = re.sub(r"[^a-zA-Z0-9]+", " ", sentence)
        cleaned_sentences.append(sentence.strip())
    return cleaned_sentences

def train_translation_model(cleaned_input_sentences, cleaned_output_sentences):
    # These are just tests, update these with actual training models
    # aligned_sentences = [ibm1.translation_table[word]['das'] if word in ibm1.translation_table else word for word in cleaned_input_sentences]
    aligned_sentences = [AlignedSent(source.split(), target.split()) for source, target in zip(cleaned_input_sentences, cleaned_output_sentences)]
    ibm_model = IBMModel1(aligned_sentences, 10)
    
    return ibm_model 

# Function to load translation rules from a JSON file
def load_translation_rules(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        
        return df
    except FileNotFoundError:
        print(f"Translation rules file not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in translation rules file: {file_path}")
        return None


# Function to translate text based on loaded translation rules
def translate_function(input_text, trained_model):
    # Split input text into words and process each word
    cleaned_text = clean_sentences(input_text.split())
    source_words = cleaned_text
    
    translated_words = []
    for source_word in source_words:
        max_prob = 0.0
        translated_word = None
        for target_word in trained_model.translation_table[source_word]:
            prob = trained_model.translation_table[source_word][target_word]
            
            if prob > max_prob:
                max_prob = prob
                translated_word = target_word
            
                # print(source_word)
                
        if translated_word is not None:
            translated_words.append(translated_word)
        else:
            # Append the original word if translation is not found
            translated_words.append(source_word)
                
    translated_text = ' '.join(translated_words)
    
    # Return JSON response with non-ASCII characters directly
    return translated_text


# Translation core process
def translate(input_language, output_language, text_to_be_translated):
    
    path_to_file = init_translation_path(input_language, output_language)
    
    df = load_translation_rules(path_to_file)
    source_sentences = df[input_language].tolist()
    outcome_sentences = df[output_language].tolist()
        
    cleaned_input_sentences = clean_sentences(source_sentences)
    cleaned_output_sentences = clean_sentences(outcome_sentences)
        
    # Train the model
    trained_model = train_translation_model(cleaned_input_sentences, cleaned_output_sentences)
    
    # Get JSON data from request body
    # data = request.form.to_dict()
    # data = request.form['input_text']
    data = text_to_be_translated
    
    translated_sentence = translate_function(data, trained_model)
    
    return translated_sentence