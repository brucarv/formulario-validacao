from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()

    errors = []

    if len(data['name']) < 3:
        errors.append('Nome deve ter pelo menos 3 caracteres.')

    if not re.match(EMAIL_REGEX, data['email']):
        errors.append('Email inválido.')

    if len(data['password']) < 8 or not re.search(r'[A-Z]', data['password']) or not re.search(r'\d', data['password']):
        errors.append('Senha deve ter no mínimo 8 caracteres, incluindo um número e uma letra maiúscula.')

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    return jsonify({'success': True, 'message': 'Validação bem-sucedida!'})

if __name__ == '__main__':
    app.run(debug=True)
