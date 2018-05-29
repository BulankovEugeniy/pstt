import test_request
import mysql_operations
import download_file

db = mysql_operations.connect_to_db()
cur = db.cursor()
data = test_request.do_it()
mysql_post_ids = mysql_operations.get_posts_ids(db, cur)

for post in data:
	if post.get("id") in mysql_post_ids:
		continue
	post["category"] = test_request.get_category()
	post["username"] = test_request.get_user_name(post.get("shortcode"))
	post["picture"] = download_file.take_string(post.get("thumbnail_resources"),post.get("category"),5)
	print(post.get("username"))
	mysql_operations.insert_post(db, cur, post)

cur.close()
db.close()
