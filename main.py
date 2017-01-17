# -*- coding: utf-8 -*-
import urllib2
import xml.etree.ElementTree as ET
file = urllib2.urlopen('http://opendata.cwb.gov.tw/opendata/MFC/F-D0047-005.xml')
tree = ET.parse(file)
root = tree.getroot()
ns = {'role': 'urn:cwb:gov:tw:cwbcommon:0.1'}
file.close()

def getWeather(place = u'桃園區', attr = u'T'):
    dataset = root.find('role:dataset', ns)
    locations = dataset.find('role:locations', ns)
    for location in locations.findall('role:location', ns):
        name = location.find('role:locationName', ns)
        if name.text.strip() == place:
            weatherelements = location.findall('role:weatherElement', ns)
            for element in weatherelements:
                if element.find('role:elementName', ns).text.strip() == attr:
                    return element.findall('role:time', ns)

def getSent():
    sent = root.find('role:sent', ns)
    return sent.text.strip()

print 'Issue: ' + getSent()
for element in getWeather():
    time = element.find('role:dataTime', ns)
    print time.text.strip()
    elementvalue = element.find('role:elementValue', ns)
    for value in elementvalue:
        print value.text.strip()
