import requests
import json
import datetime
import time
import urllib
import random

#params_to_get = [
#'taken_at_timestamp',
#'id',
#'shortcode',
#'display_url',
#'thumbnail_resources',
#'username',
#'datetime',
#'is_video'
#]

#tags_to_get = [
#"россия",
#"природа",
#"инстаграмнедели",
#"инстаграманет"
#]

def get_tag_posts(tag):
	req = requests.get("https://www.instagram.com/explore/tags/" + tag + "/?__a=1")
	responses = json.loads(req.text)
	responses = responses.get('graphql').get('hashtag').get('edge_hashtag_to_media').get('edges')
	return responses

def get_params_from_post(post, params):
	post = post.get('node')
	result = {}
	for param in params:
		result[param] = post.get(param)
		if param == "thumbnail_resources":
			result[param] = post.get(param)[0].get("src")
		if param == "datetime":
			tstamp = float(post.get('taken_at_timestamp'))
			result[param] = datetime.datetime.fromtimestamp(tstamp)
	return result

def get_user_name(shortcode):
	req = requests.get("https://www.instagram.com/p/" + shortcode + "/?__a=1")
	responses = json.loads(req.text)
	responses = responses.get('graphql').get('shortcode_media').get('owner').get('username')
	return responses

def get_posts_from_tag_info(tag_info, params):
	result = []
	for post in tag_info:
		result.append(get_params_from_post(post, params))
	return result	

def get_tag(tag,params):
	return get_posts_from_tag_info(get_tag_posts(tag),params)

def get_all_tags(tags, params):
	result = []
	for tag in tags:
		for post in get_tag(tag, params):
			if is_24_hour_delta(post.get("taken_at_timestamp")) == True:
				continue	
			if post.get('is_video') == True:
				continue	
			result.append(post)
	return result

def is_24_hour_delta(taken_at_timestamp):
	if time.mktime(datetime.datetime.now().timetuple()) - float(taken_at_timestamp) > 86400:
		return True
	else:
		return False

def get_category():
	number = random.randint(1,4)
	if number == 1:return "red"
	if number == 2:return "yellow"
	if number == 3:return "blue"
	if number == 4:return "green"

def do_it():
	params_to_get = [
	'taken_at_timestamp',
	'id',
	'shortcode',
	'display_url',
	'thumbnail_resources',
	'username',
	'datetime',
	'is_video']
	tags_to_get = ["россия","природа","инстаграмнедели","инстаграманет"]
	return get_all_tags(tags_to_get, params_to_get)
