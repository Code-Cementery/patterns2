
import csv
import codecs

a = set()
prefix = 'http://merlin2.bgk.bme.hu/'

with codecs.open('data/hits.csv', 'r', encoding='utf8') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    for row in spamreader:

        a.add(row['url'][len(prefix):])


print(a)


