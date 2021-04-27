#!/usr/bin/python3

#       Name: Area-Checker
#    Purpose: Writes subreddit comments about a city area to a CSV file
#     Author: SpuriousKelpie
# Disclaimer: GPL-3.0 License

import sys, praw, datetime, csv
from prawcore.exceptions import ResponseException

script_name = sys.argv[0]
id = ""
secret = ""
user_agent = ""
urls = []

def usage():
	"""Prints usage information for script"""
	print("Usage: %s [city subreddit] [city area]" % script_name)
	exit(0)

def get_date(created):
	"""Returns formatted timestamp"""
	return datetime.datetime.fromtimestamp(created).strftime("%d/%m/%Y, %H:%M:%S")

if len(sys.argv) != 3:
	usage()

# Create authorised read-only Reddit instance
try:
	reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent = user_agent)
except ResponseException:
	print("[!] Error with OAuth authentication")

# Return last thousand posts from the subreddit
posts = reddit.subreddit(sys.argv[1]).new(limit=None)

# Store URL of posts that contain the area in their title
for post in posts:
	if sys.argv[2].capitalize() in post.title or sys.argv[2].lower() in post.title:
		if not ".jpg" in post.url:
			urls.append(post.url)

# Write all comments on the post to a CSV file
for url in urls:
	post = reddit.submission(url="%s" % url)
	post.comments.replace_more(limit=None)
	with open("%s-%s.csv" % (sys.argv[1].lower(), sys.argv[2].lower()), "w", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["Comment", "Post Title", "Date & Time"])
		for comment in post.comments:
			writer.writerow([comment.body, post.title, get_date(comment.created)])
