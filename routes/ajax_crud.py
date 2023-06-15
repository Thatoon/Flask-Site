from flask import (
    render_template, # Renderizar Página
    request, # Pegar informações enviadas pelos forms
    url_for, # Caminho url do arquivo
    redirect, # Redirecionar a uma função
    jsonify, # formatar em JSON
    make_response
)
from flask_login import (
    login_user, # Introduz o usuário na sessão
    logout_user, # Retira o usuário da sessão
    current_user, # pega o usuário da sessão
    login_required, # Restringir o Usuário de acessar certas views
)
# coisa minha :)
from main import (
    app, # Aplicação
    db, # Database
    lm, # Login Manage
    by, # Flask-Bcrypt
)
from models.model import todo, perfil
from forms.Forms import formRegister, formLogin

@app.route('/toDo', methods=['GET', 'POST'])
def toDo():
    cards = todo.query.filter_by(fk_user=current_user.id)
    return render_template('tools/toDo.html', box=cards)

@app.route('/ajax/create', methods=['GET', 'POST'])
def create_AJAX():
    try:
        print('--- /ajax/create ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"   {Data}")

        # -- Parte lógica -- faça oq quiser com a informação

        content = Data.get('word')
        user = current_user.id

        # Envio ao banco
        db.session.add(todo(content=content, user=user))
        db.session.commit()

        ser = todo.query.filter_by(title=content)
        # -- formate a nova informação em JSON e retorne
        return make_response(jsonify({
            'id': f'{ser.id}',
            'create': True,
        }), 200)

    except:
        return make_response(jsonify({ 'create' : False }), 200)

@app.route('/ajax/update', methods=['GET', 'POST'])
def update_AJAX():
    try:
        print('--- /ajax/update ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")

        # -- lógica --
        my_card = todo.query.get()
        my_card.title = Data.get('title')
        db.session.commit()

        return make_response(jsonify({'update': True}), 200)
    except:
        return make_response(jsonify({ 'update' : False }), 200)

@app.route('/ajax/delete', methods=['GET', 'POST'])
def delete_AJAX():
    try:
        print('--- /ajax/delete ---')

        # -- pega requisição JSON
        Data = request.get_json()
        print(f"  {Data}")

        # -- lógica --
        my_card = todo.query.get()
        db.session.delete(my_card)
        db.session.commit()

        return make_response(jsonify({'delete': True}), 200)
    except:
        return make_response(jsonify({ 'delete' : False }), 200)