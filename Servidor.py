from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def receber_login():
    dados = request.get_json()
    login = dados.get('login')
    senha = dados.get('senha')

    return jsonify({'login': login, 'senha': senha})

if __name__ == '__main__':
    app.run(debug=True)

