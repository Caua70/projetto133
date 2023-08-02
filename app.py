# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Cauã" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route('/pagina_pai')
def pag_pai():

    nome = "Alexandre" 
    idade = "40"

    return render_template("pai.html", nome = nome, idade = idade)



# defina a rota para a página da mãe
@app.route('/pagina_mae')
def pag_mae():

    nome = "AnaPaula" 
    idade = "42"

    return render_template("mae.html", nome = nome, idade = idade)



# defina a rota para a página do amigo
@app.route('/pagina_amigo')
def pag_amg():

    nome = "Victor" 
    idade = "14"

    return render_template("amigo.html", nome = nome, idade = idade)


# adicione outras rotas, se você quiser


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
   
