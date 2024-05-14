from kivy.uix.filechooser import string_types
from flask import Flask

app = Flask(__name__)

# criar a 1ª página do site
@app.route("/")
def homepage():
    return ("Esse é o meu primeiro site.")

@app.route("/denúncias")
def denúncias():
   return "<p>Registre sua denúncia aqui!</p> <p>Telefone: (81)9 9999-9999</p> <p> Email: qwertyuiop@gmail.com</p>"
# colocar o site no ar
if __name__ == '__main__':
 app.run(debug= True) 