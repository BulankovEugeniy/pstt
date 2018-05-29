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
	querry = 'select id_instagram from posts'
	db_cursor.execute(querry)
	return db_cursor.fetchall()


#cursor.execute(req)
#data = get_posts_ids(db, cursor)
#print(data)
#
#cursor.close()
#db.close()

def insert_post(db_cursor, db_connect, post):
	querry = ("insert into posts(" + 
					"taken_at_timestamp, " +
					"shortcode, " +
					"thumbnail_resources, " +
					"id_instagram, " + 
					"display_url, " + 
					"category, " +
					"picture, " +
					"username) values (" +
					post.get("taken_at_timestamp") + ", " +
					post.get("shortcode") + ", " +
					post.get("thumbnail_resources") + ", " +
					post.get("id") + ", " +
					post.get("display_url") + ", " +
					post.get("category") + ", " +
					post.get("picture") + ", " +
					post.get("username") + ");")
	db_cursor.execute(querry)
	db_connect.commit()
	
def connect_to_db():
	db = mysql.connector.connect(user='pstt', password='123458', host='localhost', db='progsupertetrotest')
	return db
