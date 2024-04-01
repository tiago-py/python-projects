from flask import Flask, render_template, redirect, request
import google.generativeai as genai
from PIL import Image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
model = genai.GenerativeModel('gemini-pro-vision')
genai.configure(api_key="SUA_CHAVE_API")
responseUsr = ''

@app.route("/")
def index():
    return render_template('index.html', response=responseUsr)

@app.route("/chat", methods=["POST"])
def chatAI():
    global responseUsr 
    imagem = request.files['imagem']
    imagem.save(f"{app.config['UPLOAD_FOLDER']}/{imagem.filename}")


    img = Image.open(imagem)
   
    response = model.generate_content(["por favor me descreva o conteudo dessa imagem.", img])
    responseUsr = response.text 
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
