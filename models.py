import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'Course {self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100),  nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publishers = relationship(Publisher, backref='books')

    def __str__(self):
        return f'Course {self.id}: {self.title}:{self.id_publisher}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), nullable = False)

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    count = sq.Column(sq.Integer, )

    bookss = relationship(Book, backref='stocks')
    shops = relationship(Shop, backref='stocks2')

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DATE)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))

    stocks = relationship(Stock, backref='sales')

def craate_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)