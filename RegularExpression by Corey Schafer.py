
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
Meta Characters(need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com 
321-555-4321
123.555.1234 
123*555*1234 

800-555-1234 
900-555-1234 

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat 
pat 
bat 
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'


# pattern.finditer(): returns match objects with extra information and functionalilty

#########################################################################
# print(r'\tTab') # r stands for Raw String  t = tab

'''
##########################################################################
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match) # return an iterator that contains all of the matches
# return <_sre.SRE_Match object; span=(1, 4), match='abc'>: span(1, 4) is the begining and the end of the match, which is useful using slicing
# print(text_to_search[1:4])
##########################################################################
pattern = re.compile(r'\.')  # use backslash to escape "."
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)

##########################################################################
pattern = re.compile(r'coreyms\.com')  # use backslash to escape "."
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)
##########################################################################
pattern = re.compile(r'\d')  # anything digit
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)
##########################################################################

pattern = re.compile(r'\W')  # anything not a charactor
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)
##########################################################################
pattern = re.compile(r'\s')  # whitespace(space, tab, newline)
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)

##########################################################################
pattern = re.compile(r'\bHa')  # Word Boundary
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)
#<_sre.SRE_Match object; span=(66, 68), match='Ha'> /n is a word boundary
#<_sre.SRE_Match object; span=(69, 71), match='Ha'> whitespace is a word boundary

###########################################################################
pattern = re.compile(r'^Start') # from the begining of a string matches 'Start'
matches = pattern.finditer(sentence) # search the text with the pattern
for match in matches:
	print(match)

###########################################################################
pattern = re.compile(r'end$') # at the end of a string matches 'end'
matches = pattern.finditer(sentence) # search the text with the pattern
for match in matches:
	print(match)


###########################################################################
# How to Match Phone Number Above:
pattern = re.compile(r'\d\d\d') # matches three digits together
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)

###########################################################################
# How to Match Phone Number Above:
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # phone number or ip
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)
###########################################################################
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x8e in position 776
# Soving by: with open encoding = 'utf-8'

###########################################################################
# Parsing any phone number but not astarisk, using concept called charactor set
# notice that in the bracket, no need to put \ infront of '.'
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # Matches Characters in brackets
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)

###########################################################################
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') # Matches only 800 or 900
matches = pattern.finditer(text_to_search) # search the text with the pattern
for match in matches:
	print(match)

###########################################################################
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)

###########################################################################
pattern = re.compile(r'[1-5]')
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)
	
###########################################################################
# search for all lowercase
pattern = re.compile(r'[a-z]')
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)
		
###########################################################################
# search for all lowercase and upercase
pattern = re.compile(r'[a-zA-Z]') # a-z A-Z back to back
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)

###########################################################################
pattern = re.compile(r'[^a-zA-Z]') # within the chacractor set, ^ negates the set
with open('data.txt', 'r', encoding='utf-8' ) as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print(match)

###########################################################################
# search for cat, mat, pat except bat:
pattern = re.compile(r'[^b]at') 
matches = pattern.finditer(text_to_search) 
for match in matches:
	print(match)

###########################################################################
# 26:20 Quantifier:
###########################################################################

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
matches = pattern.finditer(text_to_search) 
for match in matches:
	print(match)
###########################################################################

# To match Mr. Shafer, Mr Smith, Mr. T
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search) 
for match in matches:
	print(match)



###########################################################################
# Group:
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search) 
for match in matches:
	print(match)


###########################################################################
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


###########################################################
# group method using parenthesis and match.group():

matches = pattern.finditer(urls)
for match in matches:
	print(match.group(0)) # using the group method to get the group
	
###########################################################
# reaching group2 and group3 in the pattern and substitute it to urls
# pattern.sub()

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

###########################################################
###########################################################

# findall(): return the matches as a list of strings
# return groups in the pattern
# if no group exists, return all of the matches in a list of strings


pattern = re.compile(r'(Mr|Ms|Mrs).?\s[A-Z]\w*') 
matches = pattern.findall(text_to_search) 
for match in matches:
	print(match)

###########################################################

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
matches = pattern.findall(text_to_search) 
for match in matches:
	print(match)

###########################################################
# pattern.match(): only matches things in the beginning of the string
# it doesn't return a iterable like finditer() or findall()
pattern = re.compile(r'Start')
matches = pattern.match(sentence)
print(matches)

###########################################################
# pattern.search(): 
pattern = re.compile(r'bring')
matches = pattern.search(sentence)
print(matches)

###########################################################
# flags:
# eg. re.IGNORECASE == re.I
pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)

############################################################
'''
# another way to write without re.compile():
pattern = r'Start'
matches = re.findall(pattern, sentence)
print(matches)

pattern = r'end'
matches = re.finditer(pattern, sentence)
for match in matches:
	print(match)


