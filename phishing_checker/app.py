from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    email_text = request.json['emailText']
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    result = 'Phishing' if prediction == 'phishing' else 'Legitimate'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
