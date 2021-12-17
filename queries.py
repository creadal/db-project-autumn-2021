from sqlalchemy import engine
from create_db import User, Publisher, Book, Review
from sqlalchemy import create_engine, func, Integer, text, desc, column, and_
from sqlalchemy.orm import sessionmaker
from random import *

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/library")

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

# 1.1 Какой процент пользователей оформил подписку в зависимости от пола
print('1.1')

q1_1 = session.query(User.gender, func.avg(User.sub.cast(Integer))*100).group_by(User.gender)

for row in q1_1:
    print(row)

print('\n', q1_1)


# 1.2 Сколько пользователей младше 30 лет
print('\n1.2')

q1_2 = session.query(func.count(User.id)).filter(text('age<30'))

print(q1_2.all())

print('\n', q1_2)

# 1.3 Вывести все книги написанные в прошлом веке отсортированные по названию
print('\n1.3')

q1_3 = session.query(Book.name, Book.author, Book.release_date).filter(text('release_date<\'1/1/2000\'')).order_by(Book.name)

for row in q1_3:
    print(row)

print('\n', q1_3)

# 1.4 Посмотреть средний возраст пользователей по региону
print('\n1.4')

q1_4 = session.query(User.location, func.avg(User.age)).group_by(User.location)

for row in q1_4:
    print(row)

print('\n', q1_4)

# 2.1 Узнать издательства для каждой из книг
print('\n2.1')

q2_1 = session.query(Book.name, Publisher.name).join(Book, Book.publisher == Publisher.id)

for row in q2_1:
    print(row)

print('\n', q2_1)

# 2.2 Узнать сколько каждый читатель оценил книг положительно (оценка 6 или больше)
print('\n2.2')

q2_2 = session.query(User.first_name, User.last_name, func.count(Review.grade).label('positive_grade'))\
                    .join(User, User.id == Review.user_id).filter(Review.grade > 5)\
                    .group_by(User.first_name, User.last_name)

for row in q2_2:
    print(row)

print('\n', q2_2)

# 2.3 Узнать среднюю оценку для каждой книги
print('\n2.3')

q2_3 = session.query(Book.name, func.avg(Review.grade).label('average_score')).\
                     join(Book, Book.id == Review.book_id).group_by(Book.name).order_by(desc('average_score'))

for row in q2_3:
    print(row)

print('\n', q2_3)

# 3.1 Вывести рейтинг издательств (средняя оценка всех книг) среди женщин и мужчин
print('\n3.3')

q3_3_grades = session.query(Book.publisher, User.gender, func.avg(Review.grade).label('score'))\
                    .join(Book, Book.id == Review.book_id)\
                    .join(User, User.id == Review.user_id)\
                    .group_by(Book.publisher, User.gender).subquery()

q3_3 = session.query(Publisher.name, q3_3_grades.c.gender, q3_3_grades.c.score).join(Publisher, Publisher.id == q3_3_grades.c.publisher)

for row in q3_3:
    print(row)

print('\n', q3_3)

# 3.2 Узнать оценку самой популярной книги издательства Bloomsbury
print('\n3.1')

q3_1_books = session.query(Publisher.id).filter(Publisher.name == 'Bloomsbury').subquery('bloomsbury')
q3_1_ratings = session.query(Book.name, func.avg(Review.grade).label('average_score')).\
                    join(Book, Book.id == Review.book_id).group_by(Book.name).filter(Book.publisher == q3_1_books.c.id)\
                    .order_by(desc('average_score')).subquery('ratings')
q3_1_max = session.query(func.max(q3_1_ratings.c.average_score).label('rating')).subquery('max_rating')
q3_1 = session.query(q3_1_ratings.c.name, q3_1_ratings.c.average_score)\
                            .filter(q3_1_ratings.c.average_score == q3_1_max.c.rating)

for row in q3_1:
    print(row)

print('\n', q3_1)

# 3.3 Узнать любимую книгу самого младшего читателя
print('\n3.2')

q3_2_age = session.query(func.min(User.age).label('age')).subquery('min_age')
q3_2_grades = session.query(User.first_name, User.last_name, func.max(Review.grade).label('grade')).join(Book, Book.id == Review.book_id)\
                .join(User, Review.user_id == User.id).group_by(User.id).filter(User.age == q3_2_age.c.age).subquery('grades')
q3_2 = session.query(User.first_name, User.last_name, Book.name, Review.grade).join(Book, Book.id == Review.book_id)\
                .join(User, Review.user_id == User.id)\
                .filter(
                    and_(
                        q3_2_grades.c.first_name == User.first_name, 
                        q3_2_grades.c.last_name == User.last_name,
                        q3_2_grades.c.grade == Review.grade
                    )
                )

for row in q3_2:
    print(row)

print('\n', q3_2)