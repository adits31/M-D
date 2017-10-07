import csv
import pandas

# path = "testsad.csv"
# with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path[:-4] + 'final.csv', 'w') as outfile:
# 	inputs = csv.reader(infile)
# 	output = csv.writer(outfile)
# 	for index, row in enumerate(inputs):
# 		# Create file with no header
# 		output.writerow(row)

# d = pandas.read_csv("testsadfinal.csv")

# for index, row in d.iterrows():
# 	row['Lyrics'] = row['Lyrics'].replace("<br/>", "*LBT*")
# 	row['Lyrics'] = row['Lyrics'].replace("</br>", "*LBT*")

# d.to_csv("testifwork2.csv", index = False)

d = pandas.read_csv("testifwork2.csv")

Artists = pandas.DataFrame(d[[0]])
Lyrics = pandas.DataFrame(d[[1]])
Song = pandas.DataFrame(d[[2]])

Artists.to_csv("sadartist.csv", index = False)
Lyrics.to_csv("sadlyrics.csv", index = False)
Song.to_csv("sadsong.csv", index = False)