from main import app, db

if __name__ == '__main__':
    """ 
        db.drop_all()
        db.create_all()
    """

    app.run(debug=True)
    # 'debug=True' - adapta a exibição a qualquer alteração feita no codigo em tempo real
