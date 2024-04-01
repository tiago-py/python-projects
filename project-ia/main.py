from flask import Flask, render_template, redirect, request
import google.generativeai as genai

app = Flask(__name__)
model = genai.GenerativeModel('gemini-pro')
genai.configure(api_key="AIzaSyBA3QkVQEMaEChwoUBbXi9NJCjwfKj0UZc")
responseUsr = ''

@app.route("/")
def index():
    return render_template('index.html', response=responseUsr)

@app.route("/chat", methods=["POST"])
def chatAI():
    global responseUsr
    if request.method == "POST":
        chat = model.start_chat()
        user_input = request.form['message']
        response = chat.send_message(user_input)
        responseUsr = response.text 
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
