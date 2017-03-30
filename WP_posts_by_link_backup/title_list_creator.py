def create_title_list(document):
	
	python_list = list()

	with open(document) as links:
		for line in links.readlines():
			try:
				title = line.strip().split("/")[-2]
				python_list.append(title)
			except:
				pass

	return python_list