import time
import os
full = 80 #238 if full screen but 80 when on small screen
word = 'Bens Statement Converter'
wordlen = int(len('Bens Statement Converter'))
gap = full - wordlen
for i in range(full):
	gap2 = gap - i
	print('-'*full, ' '*full, ' '*full, sep = '')
	print(' '*i, word, ' '*gap2, sep = '')
	print(' '*full, ' '*full, '-'*full, sep = '')
	time.sleep(0.01)
	os.system('clear')
