from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0',
     'Responsavel': 'Guilherme',
     'Status': 'Concluido',

    },
    {'id': '1',
     'Responsavel': 'Leticia',
     'Status': 'Pendente',
    }
]


# Devolve um desenvolvedor pelo ID, também altera e deleta.
@app.route('/dev/<int:id>/', methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvimento de ID {} não existe'.format(id)
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, Procure o Adminstrador da API'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        return jsonify (response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'Mensagem': 'Registro excluido'})

# Lista de todos os desenvolvedores e permite registrar um novo desenvolvedor

@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedoires():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug = True)
