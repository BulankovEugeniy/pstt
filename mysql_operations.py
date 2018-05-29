import mysql.connector
import time
import datetime
import os

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

def delete_24h_posts(db_connect, db_cursor):
	target_timestamp = time.mktime(datetime.datetime.now().timetuple()) - 86400
	querry = "delete from posts where taken_at_timestamp < " + str(target_timestamp)
	db_cursor.execute(querry)
	db_connect.commit()

def delete_non_post_files(db_connect, db_cursor):
	post_ids = get_posts_ids(db_connect, db_cursor)
	files_list = os.listdir("pic")
	for f in files_list:
		if int(f.split(".")[0]) in post_ids == False:
			os.remove("pic/" + f)
	return True


#print(type(os.listdir("pic")[1].split(".")[0]))
