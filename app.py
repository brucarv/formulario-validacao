from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_dance.contrib.google import make_google_blueprint, google
import re
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'supersecret')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')

jwt = JWTManager(app)

# Configuração do OAuth com Google
app.config['OAUTHLIB_INSECURE_TRANSPORT'] = True  # Apenas para ambiente local
app.config['GOOGLE_OAUTH_CLIENT_ID'] = os.environ.get('GOOGLE_OAUTH_CLIENT_ID', 'your-client-id')
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET', 'your-client-secret')

google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")

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

    access_token = create_access_token(identity=data['email'])
    return jsonify({'success': True, 'message': 'Validação bem-sucedida!', 'token': access_token})

@app.route('/protected')
@jwt_required()
def protected():
    return jsonify(message="Você acessou uma rota protegida com JWT!")

@app.route('/login/google')
def login_google():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    session['email'] = resp.json()["email"]
    return f"Login via Google bem-sucedido. Bem-vindo(a), {session['email']}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

