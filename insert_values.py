from sqlalchemy import engine
from create_db import User, Publisher, Book, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import *

with open('first_names.txt') as f:
    fisrt_names = [name.strip() for name in f.readlines()]
with open('last_names.txt') as f:
    last_names = [name.strip() for name in f.readlines()]

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/library")

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

for i in range(1, 21):
    new_user = User(
        id = i,
        first_name = choice(fisrt_names),
        last_name = choice(last_names),
        age = int(normalvariate(25, 5)),
        gender = choice(['male', 'female']),
        location = choice(['EU', 'NA', 'RU', 'CN', 'AU', 'AF', 'SA', 'JP']),
        sub = randint(1, 100) > 30
    )
    session.add(new_user)

session.commit()

publlist = [
    {
        'name': 'O\'Reilly',
        'location':'NA'
    },
    {
        'name': 'Bloomsbury',
        'location':'EU'
    },
    {
        'name': 'Doubleday',
        'location':'NA'
    }
]

booklist = [
    {
        'name': 'What is Web 2.0',
        'desc':'''The concept of "Web 2.0" began with a conference brainstorming session 
                        between O'Reilly and MediaLive International. Dale Dougherty, web pioneer and O'Reilly 
                        VP, noted that far from having "crashed", the web was more important than ever, with exciting 
                        new applications and sites popping up with surprising regularity. What's more, the companies 
                        that had survived the collapse seemed to have some things in common. Could it be that the dot-com 
                        collapse marked some kind of turning point for the web, such that a call to action such as "Web 2.0" 
                        might make sense? We agreed that it did, and so the Web 2.0 Conference was born.''',
        'author': 'Tim O\'Reilly',
        'genre': 'education',
        'publisher': 1,
        'release_date': '23/9/2009'
    },
    {
        'name': 'Deep Learning: A Practitioner\'s Approach',
        'desc':'''Although interest in machine learning has reached a high point, lofty expectations often scuttle 
            projects before they get very far. How can machine learning—especially deep neural networks—make a real difference 
            in your organization? This hands-on guide not only provides the most practical information available on the subject, 
            but also helps you get started building efficient deep learning networks.''',
            'author': 'Josh Patterson, Adam Gibson',
        'genre': 'education',
        'publisher': 1,
        'release_date': '28/7/2017'
    },
    {
        'name': 'Learning Python',
        'desc':'''Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. 
            Based on author Mark Lutz’s popular training course, this updated fifth edition will help you quickly write 
            efficient, high-quality code with Python. It’s an ideal way to begin, whether you’re new to programming or a 
            professional developer versed in other languages.''',
        'author': 'Mark Lutz',
        'genre': 'education',
        'publisher': 1,
        'release_date': '1/6/2013'
    },
    {
        'name': 'Harry Potter and the Philosopher\'s Stone',
        'desc':'''Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J. K. Rowling. 
            The first novel in the Harry Potter series and Rowling's debut novel, it follows Harry Potter, a young wizard who 
            discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of 
            Witchcraft and Wizardry. Harry makes close friends and a few enemies during his first year at the school, and with the 
            help of his friends, he faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harry's parents, 
            but failed to kill Harry when he was 
            just 15 months old.''',
        'author': 'J. K. Rowling',
        'genre': 'fantasy',
        'publisher': 2,
        'release_date': '27/6/1997'
    },
    {
        'name': 'Harry Potter and the Chamber of Secrets',
        'desc':'''Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling 
            and the second novel in the Harry Potter series. The plot follows Harry's second year at Hogwarts School 
            of Witchcraft and Wizardry, during which a series of messages on the walls of the school's corridors warn 
            that the "Chamber of Secrets" has been opened and that the "heir of Slytherin" would kill all pupils who 
            do not come from all-magical families. These threats are found after attacks that leave residents of the 
            school petrified. Throughout the year, Harry and his friends Ron and Hermione investigate the attacks.''',
        'author': 'J. K. Rowling',
        'genre': 'fantasy',
        'publisher': 2,
        'release_date': '2/7/1998'
    },
    {
        'name': 'Harry Potter and the Prisoner of Azkaban',
        'desc':'''Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author 
            J. K. Rowling and is the third in the Harry Potter series. The book follows Harry Potter, a young wizard, 
            in his third year at Hogwarts School of Witchcraft and Wizardry. Along with friends Ronald Weasley and Hermione Granger, 
            Harry investigates Sirius Black, an escaped prisoner from Azkaban, the wizard prison, believed to be one of 
            Lord Voldemort's old allies.''',
        'author': 'J. K. Rowling',
        'genre': 'fantasy',
        'publisher': 2,
        'release_date': '8/7/1999'
    },
    {
        'name': 'The Shining',
        'desc':'''The Shining is a 1977 horror novel by American author Stephen King. 
                        It is King's third published novel and first hardback bestseller; its success firmly 
                        established King as a preeminent author in the horror genre. The setting and characters 
                        are influenced by King's personal experiences, including both his visit to The Stanley 
                        Hotel in 1974 and his struggle with alcoholism. The novel was adapted into a 1980 film 
                        of the same name. The book was followed by a sequel, Doctor Sleep, published in 2013, 
                        which was adapted into a film of the same name.''',
        'author': 'Stephen King',
        'genre': 'horror',
        'publisher': 3,
        'release_date': '28/1/1977'
    },
    {
        'name': 'Carrie',
        'desc':'''Carrie is a gothic horror novel by American author Stephen King. 
                        It was his first published novel, released on April 5, 1974, with a first print-run 
                        of 30,000 copies.[1] Set primarily in the then-future year of 1979, it revolves around 
                        the eponymous Carrie White, a friendless, bullied high-school girl from an abusive 
                        religious household who uses her newly discovered telekinetic powers to exact revenge 
                        on those who torment her. In the process, she causes one of the worst local disasters 
                        the town has ever had. King has commented that he finds the work to be "raw" and "with
                        a surprising power to hurt and horrify." Much of the book uses newspaper clippings, 
                        magazine articles, letters, and excerpts from books to tell how Carrie destroyed the 
                        fictional town of Chamberlain, Maine while exacting revenge on her sadistic classmates
                        and her own mother Margaret. Carrie was one of the most frequently banned books in United 
                        States schools in the 1990s[2] because of its violence, cursing, underage sex and negative 
                        view of religion.''',
        'author': 'Stephen King',
        'genre': 'horror',
        'publisher': 3,
        'release_date': '5/4/1974'
    },
    {
        'name': 'Night Shift',
        'desc':'''This new book of stories from the author of Carrie, 
                        The Shining, and 'Salem's Lot is a chilling collection of strange 
                        imaginings, ghoulish twists, and diabolical terror.
                        Stephen King, a modern master of the macabre, has brought together 
                        nineteen of his most unsettling short pieces—bizarre tales of dark 
                        doings and unthinkable acts from the twilight regions where horror 
                        and madness take on eerie, unearthly forms... where noises in the 
                        walls and shadows by the bed are always signs of something dreadful 
                        on the prowl.''',
        'author': 'Stephen King',
        'genre': 'horror',
        'publisher': 3,
        'release_date': '15/12/2020'
    },
]

for i in range(len(publlist)):
    new_publ = Publisher(id=i+1, **publlist[i])
    session.add(new_publ)

for i in range(len(booklist)):
    new_book = Book(id=i+1, **booklist[i])
    session.add(new_book)

session.commit()

for i in range(len(booklist) * 10):
    new_review = Review(
        id = i + 1,
        user_id = randrange(1, 21),
        book_id = randrange(1, len(booklist) + 1),
        grade = randrange(1, 11)
    )
    session.add(new_review)

session.commit()
session.close()