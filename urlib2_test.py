from urllib.request import urlopen

html = urlopen("http://pages.cs.wisc.edu/~schoinas/cv.txt", timeout=5)
for line in html:
    print(line.rstrip())
data = html.read()
print(len(data))
print(dir(html))
print(type(html))

