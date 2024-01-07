from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not any([use_letters, use_numbers, use_symbols]):
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    use_letters = 'use_letters' in request.form
    use_numbers = 'use_numbers' in request.form
    use_symbols = 'use_symbols' in request.form
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
