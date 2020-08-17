import pyshorteners
inurl=input('Enter url\n')

s = pyshorteners.Shortener()
print(s.tinyurl.short(inurl)) ##Enter url here 