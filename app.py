from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the form data (e.g., send an email, store in database)
        # Replace the code below with your own logic

        # Print the form data to the console
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Message: {message}')

        # Return a success message to the user
        return 'Thank you for contacting me! I will get back to you soon.'

    return render_template('contact.html')
