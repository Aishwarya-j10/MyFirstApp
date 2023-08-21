from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact', methods = ["GET", "POST"])
def contact():
    if request.method == 'POST' :
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        print(f'Name: {name}, Email:{email}, Message: {message}')

        with open('message.txt', 'a') as file:
            file.write(f"Name : {name}, Email : {email}, Subject : {subject}, Message : {message}\n")

        return render_template('contact.html', message_sent = True)
    return render_template('contact.html', message_Sent = False)


if __name__ == '__main__' :
    app.run(debug = True)
