import csv
import pandas
import requests
import re
import time
import urllib.request
from bs4 import BeautifulSoup

def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"

    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)

# path = "sadboi.csv"
# with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path[:-4] + 'final.csv', 'w') as outfile:
#      inputs = csv.reader(infile)
#      output = csv.writer(outfile)
#      for index, row in enumerate(inputs):
#          # Create file with no header
#          output.writerow(row)

# happy = pandas.read_csv('happy.csv')
sad = pandas.read_csv('sadboi.csv')

# print("happy")
#
# lyrics = []
# foundSongs = []
# foundArtists = []
# count = 0
# total = 0
# for index, row in happy.iterrows():
# 	r = get_lyrics(row['Artist'], row['Song'])
# 	if r != "Exception occurred \nHTTP Error 404: Not Found":
# 		lyrics += [r]
# 		foundSongs += [row['Song']]
# 		foundArtists += [row['Artist']]
# 		print(index)
# 		count += 1
# 	total += 1
# print(count, total)
#
# dicto = {'Artist': foundArtists, 'Song': foundSongs, 'Lyrics': lyrics}
# df = pandas.DataFrame(data=dicto)
# df.to_csv("test.csv", index = False)

print("sad")

lyrics = []
foundSongs = []
foundArtists = []
count = 0
total = 0
for index, row in sad.iterrows():
	r = get_lyrics(row['Artist'], row['Song'])
	if r != "Exception occurred \nHTTP Error 404: Not Found":
		lyrics += [r]
		foundSongs += [row['Song']]
		foundArtists += [row['Artist']]
		print(index)
		count += 1
	total += 1
	time.sleep(1)
print(count, total)

dicto = {'Artist': foundArtists, 'Song': foundSongs, 'Lyrics': lyrics}
df = pandas.DataFrame(data=dicto)
df.to_csv("testsad.csv", index = False)
