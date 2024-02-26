#!/usr/bin/python3

import os, sys, folium
from folium.plugins import MarkerCluster
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def getExif(basePath, imgPath):
    img = Image.open(basePath + imgPath)
    data = img._getexif()
    if data:
        table = {}
        for t, v in data.items():
            tag = TAGS.get(t, t)
            table[tag] = v
        return table
    else:
        return None

def getGPS(data):
    if 'GPSInfo' in data:
        gps = {}
        for t, v in data['GPSInfo'].items():
            tag = GPSTAGS.get(t, t)
            gps[tag] = v
        return gps
    else:
        return None

def getCoords(gps):
    if gps:
        latRef = gps.get('GPSLatitudeRef')
        lonRef = gps.get('GPSLongitudeRef')
        latDeg, latMin, latSec = gps.get('GPSLatitude')
        lonDeg, lonMin, lonSec = gps.get('GPSLongitude')
        
        latitude = (latDeg + latMin/60.0 + latSec/3600.0) * (-1 if latRef in ['S', 'W'] else 1)
        longitude = (lonDeg + lonMin/60.0 + lonSec/3600.0) * (-1 if lonRef in ['S', 'W'] else 1)
        
        return latitude, longitude
    else:
        return None

def getImgs(basePath):
    imgs = []
    for path in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, path)):
            # check if it's an img file
            i = path.index('.')
            imgExts = [".jpg", ".jpeg", ".png", ".gif"]
            if path[i:] not in imgExts:
                continue
            imgs.append(path) 

    return imgs

def plot(files):
    m = folium.Map(location=[files[0]['lat'], files[0]['long']], zoom_start=5)
    cluster = MarkerCluster().add_to(m)
     
    for file in files:
        folium.Marker(
            location=[file['lat'], file['long']],
            tooltip=file['name']
        ).add_to(cluster)

    m.save("index.html")
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        base = sys.argv[1]
    else:
        base = "./"
    print(base)
    imgs = getImgs(base)


    files = []
    for img in imgs:
        exif = getExif(base, img)
        if exif is None:
            continue
        gps = getGPS(exif)
        if gps is None:
            continue
        lat, long = getCoords(gps)
        files.append({"lat": lat, "long": long, "name": img})

    plot(files)

