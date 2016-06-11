from lxml import html
import requests

from Tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)


page = requests.get('http://excel.london/whats-on')
tree = html.fromstring(page.content)
name = tree.xpath('//span[@class="name"]/text()')
date = tree.xpath('//span[@class="date"]/text()')
date1 = tree.xpath('//span[@class="date2"]/text()')

count = len(name) - 1
position = 0;
while position < count:
     text.insert(INSERT, '\nEvent Name: ' + name[position] + '\n')
     text.insert(INSERT, 'Start Date: ' + date[position]+ '\n')
     text.insert(INSERT, 'End Date: ' + date1[position], '\n')
     text.insert(INSERT, '\n')
     position += 1


text.pack()


root.mainloop()

