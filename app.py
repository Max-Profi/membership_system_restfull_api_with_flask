from flask import Flask, g, json, request, jsonify
from db_setup import get_db, query_db, insert_db

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

    get_all_members = query_db('select id, name, email, level from members')

    all_members = []
    for member in get_all_members:
        member_dict ={}
        member_dict['id'] = member['id']
        member_dict['name'] = member['name']
        member_dict['email'] = member['email']
        member_dict['level'] = member['level']
        all_members.append(member_dict)

    return jsonify({'members': all_members})


@app.route('/member/', methods=['POST'])
def add_member():
    new_member_data = request.get_json()

    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']

    insert_db('insert into members (name, email, level) values (?, ?, ?)', [name, email, level])

    new_member = query_db('select id, name, email, level from members where name = ?', [name], one=True)

    return  jsonify({'id': new_member['id'], 'name': new_member['name'],'email': new_member['email'], 'level': new_member['level']})


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
