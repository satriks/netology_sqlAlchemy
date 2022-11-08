import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
'''Скрипт импортирует необходимые модели данных '''
from models import craate_tables, Publisher,Shop,Book,Stock,Sale

'''Скрипт подключается к БД любого типа на ваш выбор.'''

DSN = 'postgresql://postgres:123st321@localhost:5432/netology_Alchemy'
engine = sqlalchemy.create_engine(DSN)

craate_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''Скрипт заполняет БД из файла '''

model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale
        }

with open('tests_data.json', 'r') as file:
    data = json.load(file)

    for record in data:
        session.add(model[record.get('model')](id= record.get('pk'), **record.get('fields')))
        session.commit()

''' Скрипт который выводит название магазина, где продается издатель (по id или имени'''

quer = input('Введите id или имя издателя :')
answer = []
print()
print('Издатель продается в магазинах :', end=' ')

if quer.isdigit():
    for resalt in session.query(Publisher, Shop).join(Book).join(Stock).join(Shop).filter(Publisher.id == quer).all():
        print(resalt[-1].name, end='; ')
else:
    for resalt in session.query(Publisher, Shop).join(Book).join(Stock).join(Shop).filter(Publisher.name == quer).all():
        print(resalt[-1].name, end='; ')
print()
session.close()
