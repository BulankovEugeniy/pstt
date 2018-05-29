import test_request
import mysql_operations
import download_file
import os

os.chdir('/home/bulevg/pstt/')
db = mysql_operations.connect_to_db()
cur = db.cursor()
data = test_request.do_it()
mysql_post_ids = mysql_operations.get_posts_ids(db, cur)

for post in data:
	if int(post.get("id")) in mysql_post_ids:
		continue
	post["category"] = test_request.get_category()
	post["username"] = test_request.get_user_name(post.get("shortcode"))
	download_file.take_string(post.get("thumbnail_resources"),post.get("category"),5 , post.get("id"))
	mysql_operations.insert_post(db, cur, post)

mysql_operations.delete_24h_posts(db, cur)
mysql_operations.delete_non_post_files(db, cur)

cur.close()
db.close()
