import re

filename = input("Enter filename: ")

file = open(filename, "r", encoding="utf-8")
text = file.read()
file.close()

links = re.findall(r'\"(https|http):\/\/(.+?)\"', string=text)
for link in links:
    print("%s://%s" % (link[0], link[1]))

