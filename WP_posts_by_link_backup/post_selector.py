def export_posts(urls, titles, source, destination):
	
	writer = True
	stack = False
	wanted = False
	count = 0

	with open(source) as post_backup:
		with open(destination, "w+") as for_importer:

			for line in post_backup.readlines():

				if writer == True:
					for_importer.write(line)

				if line.startswith("	<item>"):
					stack = True
					stack_content = ""
					writer = False
				elif line.startswith("	</item>"):
					stack = False
					if wanted == True:
						for_importer.write(stack_content)
						for_importer.write(line)
						wanted = False


				if stack == True:
					stack_content += line
					if (line.startswith("		<title>") and ("-").join(line.strip("\n")[9:-8].lower().replace(":", "").replace("&#039;", "").replace("’", "").replace("-&#124;", "").replace(".", "").replace("!", "").replace("-&amp;", "").replace("?","").replace(",","").replace("“", "").replace("”", "").split(" ")) in titles) or (line.startswith("		<link>") and line.strip()[6:-7] in urls):
						count += 1
						wanted = True

	return count