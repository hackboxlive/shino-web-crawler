import os

def create_project(directory):
	if not os.path.exists(directory):
		print('Making directory: ' + directory)
		os.makedirs(directory)

create_project('hackboxlive')
