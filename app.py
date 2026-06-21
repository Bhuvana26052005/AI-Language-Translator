from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# 1. This displays your empty HTML page when you first visit the website
@app.route('/')
def home():
    return render_template('index.html', original='', translation='', lang='es')

# 2. This runs when the user clicks the "Translate" button on your HTML page
@app.route('/translate', methods=['POST'])
def translate():
    # Grab the data that the user typed into the HTML boxes
    text_to_translate = request.form['user_text']
    chosen_language = request.form['target_language']
    
    # If the user left it completely empty
    if not text_to_translate.strip():
        return render_template('index.html', original='', translation='Please enter some text!', lang=chosen_language)
    
    try:
        # Call the Google Translation engine in the background
        output = GoogleTranslator(source='auto', target=chosen_language).translate(text_to_translate)
    except Exception as e:
        output = f"An error occurred: {e}"
        
    # Send the final results back to fill up the text fields inside the HTML website
    return render_template('index.html', original=text_to_translate, translation=output, lang=chosen_language)

if __name__ == '__main__':
    app.run(debug=True)