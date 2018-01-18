import os

#to make a new directory for a new homepage
def create_project(directory):
	if not os.path.exists(directory):
		print('Making directory: ' + directory)
		os.makedirs(directory)

#to create required data files
def create_files(directory, base_url):
	uncrawled_file = directory + '/uncrawled.txt'
	crawled_file = directory + '/crawled.txt'
	if not os.path.isfile(uncrawled_file):
		write_file(uncrawled_file, base_url)
	if not os.path.isfile(crawled_file):
		write_file(crawled_file, '')

#to create a new file
def write_file(path, val):
	writer = open(path, 'w')
	writer.write(val)
	writer.close()

#Appending into file
def append_file(path, val):
	writer = open(path, 'a')
	writer.write(val + '\n')
	writer.close()

#Deleting contents of file
def delete_from(path):
	writer = open(path, 'w')
	pass
	writer.close()

delete_from('hackboxlive/uncrawled.txt')
