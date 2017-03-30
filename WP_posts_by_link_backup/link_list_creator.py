def create_link_list(document):
	
	python_list = list()

	with open(document) as links:
		for line in links.readlines():
			link = line.strip()
			if link:
			    python_list.append(link)

	return python_list