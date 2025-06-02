import google.generativeai as genai
from flask import Flask, render_template, request, redirect, url_for
import csv
import os

# Configurando a API Key
genai.configure(api_key="AIzaSyDGfvHzrdtUIfCp_c_vgl7aJFqRtu7CT68")

# Inicializando o modelo Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicializando o Flask
app = Flask(__name__)

#  Página inicial
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobre():
    return render_template('sobre.html')


#  Rota do Chat com IA
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    resposta = None
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        try:
            response = model.generate_content(mensagem)
            resposta = response.text
        except Exception as e:
            resposta = f"Ocorreu um erro: {e}"
    return render_template('chat.html', resposta=resposta)

#  Página do Glossário
@app.route('/glossario')
def glossario():
    glossario = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                glossario.append(row)
    return render_template('glossario.html', glossario=glossario)

#  Página para adicionar novo termo
@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

#  Rota para salvar novo termo
@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']
    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])
    return redirect(url_for('glossario'))

# Rota para apagar termo
@app.route('/apagar/<termo>')
def apagar_termo(termo):
    termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[0] != termo:
                    termos.append(row)
        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(termos)
    return redirect(url_for('glossario'))

#  Rodando o app
if __name__ == '__main__':
    app.run(debug=True)

