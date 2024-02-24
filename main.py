from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)

    user2 = User()
    user2.surname = 'James'
    user2.name = 'Ridley'
    user2.age = 19
    user2.position = 'deputy captain' # заместитель
    user2.speciality = 'technical engineer'
    user2.address = 'module_2'
    user2.email = 'james_cool2001@mars.org'
    db_sess.add(user2)

    user3 = User()
    user3.surname = 'Stefen'
    user3.name = 'Brome'
    user3.age = 24
    user3.position = 'electrician'
    user3.speciality = 'engineer'
    user3.address = 'module_4'
    user3.email = 'Stefeeeen@mars.org'
    db_sess.add(user3)

    user4 = User()
    user4.surname = 'Anna'
    user4.name = 'Mesloy'
    user4.age = 21
    user4.position = 'pilot'
    user4.speciality = 'pilot'
    user4.address = 'module_3'
    user4.email = 'annie@mars.org'
    db_sess.add(user4)

    db_sess.commit()


if __name__ == '__main__':
    main()
