import urllib2, re
import dictionary as d
import os

class Scraper(object):
	"""docstring for Scraper"""
	def __init__(self, file_to_save_in, website_link, predictable_dl_link, ext):
		super(Scraper, self).__init__()
		self.file_to_save_in = file_to_save_in
		self.website_link = website_link
		self.predictable_dl_link = predictable_dl_link
		self.ext = ext



def ensure_dir(file_path):
    # directory = os.path.dirname(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

def download_files():
	# Initialize the class instance.
	s = Scraper(d.file_to_save_in, d.website_link, d.predictable_dl_link, d.pdf_ext)

	file_path = os.path.abspath(s.file_to_save_in)

	ensure_dir(file_path)
	try:
		website = urllib2.urlopen(s.website_link)
		html = website.read()
	except Exception as e:
		print("Error occurred connecting to website")
	
	# Build our regex.
	pdf_regex = s.predictable_dl_link + s.ext
	# Build our list of links to download from.
	pdf_links = re.findall(pdf_regex, html)
	
	# Use i to prepend to each downloaded file name for ease of file sorting.
	i = 0
	for link in pdf_links:
		search_regex = re.search(s.predictable_dl_link + "(.+)", link)

		if (search_regex):
			pdf_string = search_regex.group(1)
	
		try:
			response = urllib2.urlopen(link)
		except Exception as e:
			print("Error occurred from response")

		fileName = str(i) + " " + pdf_string
		file = open(file_path + "/" + fileName, 'w')
		file.write(response.read())
		file.close()	
		i += 1


if __name__ == '__main__':
	
	download_files()

