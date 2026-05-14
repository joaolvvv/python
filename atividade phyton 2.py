from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def explicar_decorator():
    return """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Explicando Decorators</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }
                h1 { color: #0056b3; }
                h2 { color: #007BFF; }
                code { background-color: #f4f4f4; padding: 2px 5px; border-radius: 4px; }
            </style>
        </head>
        <body>
            <h1>O que é um decorator em Python?</h1>
            <p>Um <strong>decorator</strong> (decorador) é uma função em Python que permite modificar ou estender o comportamento de outra função ou método sem alterá-la diretamente. Ele basicamente "abraça" outra função para adicionar funcionalidades extras.</p>
            
            <h2>Para que ele serve?</h2>
            <p>Serve para evitar a repetição de código e separar lógicas secundárias da lógica principal de uma função. É muito usado para validação de login, medição de tempo de execução de um código, registro de logs e roteamento de URLs em frameworks web.</p>
            
            <h2>Como ele é utilizado no Flask?</h2>
            <p>No Flask, o decorator mais comum é o <code>@app.route()</code>. Ele é utilizado para mapear uma URL (rota) do navegador a uma função específica do Python. Quando o usuário acessa aquela URL, o Flask identifica o decorator e executa a função que está logo abaixo dele, retornando o resultado para a tela.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)