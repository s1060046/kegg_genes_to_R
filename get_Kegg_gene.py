import argparse
import requests
from bs4 import BeautifulSoup
import re

my_parser = argparse.ArgumentParser(description='keggpathway')
my_parser.add_argument('pathway', help='pathway identification')
my_parser.add_argument('output', help='outputfile')


args = my_parser.parse_args()

pathway = args.pathway
output_file = args.output
PATH = "https://www.genome.jp/dbget-bin/get_linkdb?-t+genes+path:"
url = PATH + pathway

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

output = []

for link in soup.find_all('a'):
	data = str(link.get('href'))
	if re.search('mmu', data):
		output.append(data.split(sep = "/")[2])

with open(output_file, 'w') as filehandle:
    for listitem in output:
        filehandle.write('%s\n' % listitem)
