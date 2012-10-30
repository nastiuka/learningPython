
"""eteration = 10 
for x in range(0,eteration):
	print "Hello World" 

% = 75
lojka_deogtea = 15.0 / 100
sare_pe_rana = 8.62 / 100

%_total = % + % * lojka_deogtea + % * sare_pe_rana
print gruz_total
"""
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	if (first =='a'or'e'or'i'or'o'or'u') :
		new_word = word + pyg
		print new_word
	else:
		end_word = len(word)
		new_word = word[1:end_word] + first + pyg
		print new_word
else:
	print 'empty'
