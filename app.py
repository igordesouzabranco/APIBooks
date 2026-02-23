from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controlers.book import Book, BookList

from server.instance import server

api = server.api
app = server.app

api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    
    # Cria as tabelas manualmente antes de rodar
    with app.app_context():
        db.create_all()

    server.run()


