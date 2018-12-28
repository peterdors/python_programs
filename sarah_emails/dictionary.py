# Dictionary class file for storing webpages
import random

class Dictionary():

	# Creates 3 static dictionary items for websites we will use.
	# Then returns the dictionary to be used.
	def create_dict(self):
		
		websites = {
			"div.entry-content h2" : 'https://lifehacks.io/love-quotes-for-her/',

			# "div.content-list-component yr-content-list-text text ul li": 'https://www.huffingtonpost.com/richard-kronick/35-cute-love-quotes-for-h_b_11081070.html'

			"div.post-container blockquote": 'http://www.planetofsuccess.com/blog/2017/sweet-quotes-for-her/'
		}

		return websites

	# Chooses a random website to use from the dictionary.
	def get_key(self):
		websites = self.create_dict()

		rand_key = random.choice(websites.keys())

		# print(rand_key)

		return rand_key 

	def get_website_link(self, rand_key):
		websites = self.create_dict()

		val = websites.get(rand_key)
		# print(val)

		return val


