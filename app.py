from flask import Flask, render_template, request, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# --- Page Routes ---
# These routes tell Flask which HTML file to send to the browser
# when a user visits a specific URL.

@app.route('/')
def home():
    """Serves the homepage."""
    return render_template('home.html')

@app.route('/mental_ai')
def mental_ai():
    """Serves the Mental Health AI page."""
    return render_template('mental_ai.html')

@app.route('/toolkit')
def toolkit():
    """Serves the Toolkit page."""
    return render_template('toolkit.html')

@app.route('/directory')
def directory():
    """Serves the Directory page."""
    return render_template('directory.html')

@app.route('/help_finder')
def help_finder():
    """Serves the Help Finder page."""
    return render_template('help_finder.html')

@app.route('/contact')
def contact():
    """Serves the Contact page."""
    return render_template('contact.html')

# --- API / Form Handling Route ---

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """
    Handles the submission of the contact form.
    In a real application, you would add code here to:
    1. Sanitize and validate the input.
    2. Send an email notification.
    3. Save the message to a database.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        inquiry_type = request.form.get('inquiry-type')
        message = request.form.get('message')

        # For now, we'll just print the data to the console (the "terminal")
        # to show that the backend has received it.
        print("--- CONTACT FORM SUBMISSION ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Inquiry Type: {inquiry_type}")
        print(f"Message: {message}")
        print("-----------------------------")

        # Return a success message to the frontend
        return jsonify({"status": "success", "message": "Thank you for your message! We will get back to you soon."})

# This is the standard entry point for a Python script.
if __name__ == '__main__':
    # Runs the Flask development server.
    # debug=True allows the server to automatically reload when you save changes.
    app.run(debug=True)
