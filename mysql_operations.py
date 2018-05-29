import mysql.connector

#config = {
#	'user': 'pstt',
#	'password': '123458',
#	'host': 'localhost',
#	'db': 'progsupertetrotest'
#}
#
#db = mysql.connector.connect(**config)
#
#cursor = db.cursor()
#
#
def get_posts_ids(db_connect, db_cursor):
	result = []
	querry = 'select id_instagram from posts'
	db_cursor.execute(querry)
	db_result = db_cursor.fetchall()
	for db_res in db_result:
		result.append(db_res[0])
	return result


#cursor.execute(req)
#data = get_posts_ids(db, cursor)
#print(data)
#
#cursor.close()
#db.close()

def insert_post(db_connect, db_cursor, post):
	print(post.get("shortcode"))		
	querry = ("insert into posts(" + 
					"taken_at_timestamp, " +
					"shortcode, " +
					"thumbnail_resources, " +
					"id_instagram, " + 
					"display_url, " + 
					"category, " +
					"username) values ('" +
					str(post.get("taken_at_timestamp")) + "', '" +
					str(post.get("shortcode")) + "', '" +
					str(post.get("thumbnail_resources")) + "', " +
					str(post.get("id")) + ", '" +
					str(post.get("display_url")) + "', '" +
					str(post.get("category")) + "', '" + 
					str(post.get("username")) + "')")
	db_cursor.execute(querry)
	db_connect.commit()
	
def connect_to_db():
	db = mysql.connector.connect(user='pstt', password='123458', host='localhost', db='progsupertetrotest')
	return db
