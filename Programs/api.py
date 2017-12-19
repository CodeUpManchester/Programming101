from urllib2 import Request, urlopen, URLError
from PIL import Image
import json
import cStringIO

def getKittehz():
    kittenRequest = Request("http://placekitten.com")
    try:
        response = urlopen(kittenRequest)
        kittens = response.read()
        print kittens[559:1000]
    except URLError, e:
        print 'No kittehz. Got an error code:', e

def getNasaStuff():
    api_key = 'F2VXBSWfDaFRgw62l1re20ivCxKTtd6hiozLumsn'
    lon = 100.75
    lat = 1.5
    date = '2014-02-01'
    cloud_score = True

    requestString = 'https://api.nasa.gov/planetary/earth/imagery?'
    requestString += '?lon=' + str(lon)
    requestString += '&lat=' + str(lat)
    requestString += '&date=' + date
    requestString += '&cloud_score=' + str(cloud_score)
    requestString += '&api_key=' + api_key

    try:
        nasaRequest = Request(requestString)
        response = urlopen(nasaRequest)
        nasaStuff = response.read()
        data = json.loads(nasaStuff)
        for key in data:
            print key, ':', data[key]

        imageRequest = Request(data['url'])
        response = urlopen(imageRequest)
        imageData = response.read()

        f = cStringIO.StringIO(imageData)
        img = Image.open(f)
        img.show()

        raw_input()
    except URLError, e:
        print 'No NASA stuff. Got an error code:', e

getKittehz()

getNasaStuff()
