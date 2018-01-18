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

#Put file into a set
def file_to_set(file_name):
	ret = set()
	reader = open(file_name, 'rt')
	for line in reader:
		ret.add(line.replace('\n',''))
	reader.close()
	return ret

#Put set into a file
def set_to_file(val, file_name):
	delete_from(file_name)
	for link in val:
		append_file(file_name, link)

#delete_from('hackboxlive/uncrawled.txt')
