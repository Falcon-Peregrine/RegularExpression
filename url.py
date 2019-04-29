import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

'''
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
'''
###########################################################
# findall():return

matches = pattern.findall()