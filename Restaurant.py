import overpy
import sys
import csv
import overpass

api = overpy.Overpass()
fobj=open("Restaurant.csv","w")
fobj.write("Restaurant in Chennai")
id="ID"
name="NAME"
link ="LINK"
head=(id+","+link+","+name)
fobj.write('\n'+head)
results = api.query("""[out:json][timeout:3600];(node["amenity"="restaurant"](12.9201721,80.1238331,13.2401721,80.4438331)["name:ta"!~"."](12.9201721,80.1238331,13.2401721,80.4438331););out meta;>;out meta qt;
""")
for way in results.nodes:
    EnName=way.tags.get("name:en")       
    if EnName==None:
        Name=way.tags.get("name")
        EnName=Name
        if EnName==None:
            EnName="None"
    Id=way.id
    id=str(Id)
    osm="https://www.openstreetmap.org/node/"
    OSM=str(osm)
    Link=OSM + id
    print(EnName)
    print(id)
    inp=(id+","+Link+","+EnName)
    fobj.write('\n'+inp)
