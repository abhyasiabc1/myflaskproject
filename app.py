from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    name = ""
    if request.method == 'POST':
        # Safely capture form variables sent by clients
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Log data to terminal for testing (substitute with DB/email hooks later)
        print(f"Lead Received: {name} | {email} | Message: {message}")
        success = True
        
    return render_template('contact.html', success=success, name=name)

if __name__ == '__main__':
    app.run(debug=True)