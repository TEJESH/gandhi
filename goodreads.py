import time
import sys
import re
from goodreads import client
from goodreads import group
from goodreads import session
from goodreads import user
gc = client.GoodreadsClient('nTRaECtlyOjSmjJnLKRaiw', 'hCXp9GKlAe3sk1QIj0jXLF4UGLt9vfj54hDAfzHY')
#gc.authenticate('nrdWjPAm8ZvH33eDncxHcHz2VXhdiXng', 'k_CkrFrrffJZGgFoggmddWBXGTxqmqNlrg1AgwAZAObczx03aES_KhmUYvLC1PuS')
#print raw_input('id')


for x in xrange(1,10):
	id = raw_input('id')
	
	name = raw_input('name')
	#namer = re.sub(r' ', '%20', str(name))
	#print namer
	
	book = gc.book(id)
	authors = book.authors
	bookn = gc.search_books_links(name)
	bookr = re.sub(r', u', '\n', str(bookn))
	length = len(bookr.split('\n'))

	
	#id1 = gc.book('Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)')
	#print id1
	print authors
	print book
	print bookr
	print length
	#print bookn['authors']
while 1:
    time.sleep(10)