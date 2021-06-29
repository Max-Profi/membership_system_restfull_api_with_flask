from flask import Flask, g
from db_setup import get_db, query_db

app = Flask(__name__)


app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'\x1f.n\xc9\xf0\xec\xd6/`\x95u\xbd\xc5?\x80",n\xb6&\xaa\xf9.\x92'
app.config['TESTING'] = False


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/member/', methods=['GET'])
def get_members():
    return 'this returns all the memberss'


@app.route('/member/', methods=['POST'])
def add_member():
    return 'this adds a new member'


@app.route('/member/<int:member_id>/', methods=['GET'])
def get_member(member_id):
    return 'this returns one member by ID'


@app.route('/member/<int:member_id>/', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'this updates a member by ID'


@app.route('/member/<int:member_id>/', methods=['DELETE'])
def delete_member(member_id):
    return 'this delets a member by ID'






if __name__ == '__main__':
    app.run()
