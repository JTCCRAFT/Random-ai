from flask import Flask, render_template, request
# This line imports the 'model' you already set up in main.py
from main import model 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_text = request.form.get('user_input')
    if user_text:
        # Uses the model imported from main.py
        response = model.generate_content(user_text)
        return render_template('index.html', user_text=user_text, ai_response=response.text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
