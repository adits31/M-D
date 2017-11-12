import pandas
import csv
#removes any songs from a CSV that do not have lyrics that were found
def saveCSV(songArtistCSV):
	df = pandas.read_csv(songArtistCSV, encoding = 'latin-1')
	df = df[df['lyrics'] != '-1']
	df.to_csv(songArtistCSV[:-4]+"trimmed.csv")
