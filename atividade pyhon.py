from flask import Flask

app = Flask(__name__)

@app.route('/')
def curriculo():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Meu Currículo</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px auto; max-width: 800px; line-height: 1.6; color: #333; }
            header { text-align: center; margin-bottom: 40px; }
            h1 { color: #2c3e50; margin-bottom: 5px; }
            h2 { color: #2980b9; border-bottom: 2px solid #ecf0f1; padding-bottom: 5px; margin-top: 30px; }
            .contato { color: #7f8c8d; font-size: 1.1em; }
            ul { list-style-type: square; }
        </style>
    </head>
    <body>
        <header>
            <h1>Seu Nome Completo</h1>
            <p class="contato">seu.email@exemplo.com | (00) 90000-0000 | LinkedIn: /in/seuperfil</p>
        </header>

        <h2>Resumo Profissional</h2>
        <p>Desenvolvedor(a) júnior focado no desenvolvimento de aplicações web utilizando Python e o microframework Flask. Tenho facilidade para aprender novas tecnologias e procuro sempre aplicar as melhores práticas de programação.</p>

        <h2>Experiência Profissional</h2>
        <ul>
            <li><strong>Estudante de Programação</strong> - Projetos Pessoais (Atualmente)
                <p>Desenvolvimento de pequenas aplicações web, criação de rotas e integração com HTML utilizando o Flask.</p>
            </li>
        </ul>

        <h2>Formação Acadêmica</h2>
        <ul>
            <li><strong>Curso de Desenvolvimento Web (Python)</strong> - Instituição X (Conclusão: 2026)</li>
        </ul>

        <h2>Habilidades</h2>
        <ul>
            <li>Linguagens: Python, HTML, CSS</li>
            <li>Frameworks: Flask</li>
            <li>Ferramentas: Git, GitHub</li>
        </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5001)