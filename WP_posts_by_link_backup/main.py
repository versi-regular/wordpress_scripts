from link_list_creator import create_link_list
from title_list_creator import create_title_list
from post_selector import export_posts

if __name__ == "__main__":

	wanted_posts_URL = create_link_list("link_list.txt")
	wanted_posts_title = create_title_list("link_list.txt")

	found = export_posts(wanted_posts_URL, wanted_posts_title, "whatweekly.wordpress.2017-03-29.xml", "whatweekly.wordpress.for_importer.xml")

	print(found, "wanted posts found out of:\n", len(wanted_posts_URL), "wanted posts entered as links, and\n", len(wanted_posts_title), "wanted posts entered as titles.")