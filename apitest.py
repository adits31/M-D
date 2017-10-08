import urllib.request as r
import json
import urllib.parse
import os
import time

def get_photos(emotion, tags):
	print("Finding " + emotion + " images using " + str(tags))
	total_photos = 0;
	for tag in tags:
		data = {}
		data['tag'] = tag
		data['limit'] = '20'
		data['api_key'] = 'fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4'
		tumblr = 'https://api.tumblr.com/v2/tagged?' + urllib.parse.urlencode(data)

		time.sleep(5)
		resp = r.urlopen(tumblr)
		things = json.loads(resp.read())
		urls = []
		for i in range(len(things["response"])):
			if(things["response"][i]["type"] == "photo"):
				try:
					urls.append(things["response"][i]["photos"][0]["original_size"]["url"])
				except IndexError:
					continue

		for i in range(len(urls)):
			num = len(next(os.walk("C:\\Users\\Manu\\Documents\\tumblr_pics_" + emotion))[2])
			urllib.request.urlretrieve(urls[i], "C:\\Users\\Manu\\Documents\\tumblr_pics_" + emotion + "\\img" + str(num) + ".jpg")
		total_photos += len(urls)
	return total_photos

emotions = {"fear" : ["fear", "death", "spooky"], \
			"love" : ["love", "warmth", "intimacy"], \
			"angry" : ["annoyed", "irritated", "livid"]}
for e in emotions:
	print(get_photos(e, emotions[e]))
# frightened, dread
# passion, 