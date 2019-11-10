import sqlite3

class BilagModel(object):
    def __init__(self, _id, description, price, username):
        self.id = _id
        self.description = description
        self.price = price
        self.username = username


    @classmethod
    def find_by_id(cls,id):
    	connection = sqlite3.connect('data.db')
    	cursor = connection.cursor()

    	query = "SELECT * FROM users WHERE id = ?"

    	result = cursor.execute(query,(id,))
    	row = result.fetchone()

    	if row:
    		user = User(*row)

    	else:
    		user = None

    	connection.close()
    	return user