from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os
import traceback


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure Flask-Mail for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('test2.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    try:
        order_data = request.get_json()
        
        name = order_data['name']
        food = order_data['food']
        quantity = order_data['quantity']
        default_email = 'default-customer-email@example.com'  # Hardcoded default email
        
        # Create the email content
        msg = Message('New Food Order',
                      recipients=['chaitanyasanikommu6@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {default_email}\nFood Item: {food}\nQuantity: {quantity}"
        
        mail.send(msg)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        # Print the error traceback to the console
        print(traceback.format_exc())
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
