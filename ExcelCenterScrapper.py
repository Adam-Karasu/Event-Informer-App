from lxml import html
import requests

page = requests.get('http://excel.london/whats-on') 
tree = html.fromstring(page.content)
name = tree.xpath('//span[@class="name"]/text()')
date = tree.xpath('//span[@class="date"]/text()')
date1 = tree.xpath('//span[@class="date2"]/text()')

count = len(name) - 1 
position = 0;
while position <= count:
	print 'Event Name: ', name[count]
	print 'Start Date: ',date[count]
	print 'End Date: ',date1[count], '\n'
	count -= 1
