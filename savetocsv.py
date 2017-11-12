import lyricwikia as lw
import time
import pandas
import csv

def saveCSV(songArtistCSV):
	df = pandas.read_csv(songArtistCSV, encoding = 'latin-1')
	nf = 0
	lyrArr = []
	for index, row in df.iterrows():
		try:
			lyrics = lw.get_lyrics((row["Artist"]+";")[:row["Artist"].find(";")],row["Song"])
			lyrArr += [lyrics]
		except Exception as e:
			print(row["Song"], " not found.")
			nf+=1
			lyrArr += [-1]
		print("Song Index ", index)
	print("Number of Songs not Found: ", nf)
	df["lyrics"] = lyrArr
	df.to_csv(songArtistCSV[:-4]+"lyrics.csv")
