from kivy.uix.filechooser import string_types
from flask import Flask, render_template

app = Flask(__name__)

# criar a 1ª página do site
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/denúncias")
def denúncias():
   return  render_template("denuncias.html")

@app.route("/registro")
def registro():
   return render_template("registro.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
   return render_template("usuários.html", nome_usuario=nome_usuario)
# colocar o site no ar
if __name__ == '__main__':
 app.run(debug= True) 

 # servidor do heroku