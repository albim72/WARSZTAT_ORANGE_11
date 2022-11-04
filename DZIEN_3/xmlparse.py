from xml.dom.minidom import parse
dom = parse("osoba.xml")
osoby = dom.getElementsByTagName('osoby')
osoba = dom.getElementsByTagName('osoba')

print(type(osoby))
print(type(osoba))

print(' '.join(t.nodeValue for t in osoby[0].childNodes if t.nodeType == t.TEXT_NODE))
print(' '.join(t.nodeValue for t in osoba[0].childNodes if t.nodeType == t.TEXT_NODE))
print(' '.join(t.nodeValue for t in osoba[1].childNodes if t.nodeType == t.TEXT_NODE))
