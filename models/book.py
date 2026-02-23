from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=False)

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


    def __repr__(self, ):
        return f"Book(title={self.title}, pages={self.pages})"
    
    def json(self, ):
        return {
            'title': self.title,
            'pages': self.pages
            }
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_pages(cls, pages):
        return cls.query.filter_by(pages=pages).all()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self, ): #Salva no db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, ): #Deleta do db
        db.session.delete(self)
        db.session.commit()