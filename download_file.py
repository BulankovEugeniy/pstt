import urllib.request
import scipy.misc
import tempfile
import PIL.Image
import numpy

def download_file(url_to_download):
	file = urllib.request.urlopen(url_to_download).read()
	return file

def make_np_from_picture(uploaded_file):
	tf = tempfile.TemporaryFile()
	tf.write(uploaded_file)
	result = scipy.misc.imread(tf)
	tf.close()
	return result

def make_ramka(arr, color, frame_pix):
	if color == 'red':
		color_to_insert = numpy.array([255,0,0])
	if color == 'yellow':
		color_to_insert = numpy.array([255,255,0])
	if color == 'blue':
		color_to_insert = numpy.array([0,0,255])
	if color == 'green':
		color_to_insert = numpy.array([0,128,0])
	arr[0:arr.shape[0], 0:frame_pix] = color_to_insert
	arr[0:arr.shape[0], arr.shape[1] - frame_pix:arr.shape[1]] = color_to_insert
	arr[0:frame_pix, 0:arr.shape[1]] = color_to_insert
	arr[arr.shape[0] - frame_pix:arr.shape[0], 0:arr.shape[1]] = color_to_insert
	return arr
	
def save_image(arr, picture_name):
	img = PIL.Image.fromarray(arr, 'RGB')
	img.save(picture_name)
	return True

def take_string(download_url, color, frame_pix, id_instagram):
	result = download_file(download_url)
	result = make_np_from_picture(result)
	result = make_ramka(result, color, frame_pix)
	file_to_save = open("pic/" + str(id_instagram) + ".jpg", "w")
	save_image(result, file_to_save)
	file_to_save.close()
	return True

#print(take_string('https://scontent-arn2-1.cdninstagram.com/vp/4045ab9664ec534653255202bbd5d91f/5BA78AE8/t51.2885-15/s150x150/e35/32725494_168860993794566_5442663590639173632_n.jpg', 'green', 5))
