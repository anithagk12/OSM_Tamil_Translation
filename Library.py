import overpy
import sys
import csv
import overpass

api = overpy.Overpass()
fobj=open("Librarys.csv","w")
fobj.write("Librarys in Chennai")
id="ID"
name="NAME"
link ="LINK"
head=(id+","+link+","+name)
fobj.write('\n'+head)
results = api.query("""[out:json][timeout:3600];(node["amenity"="library"](12.9201721,80.1238331,13.2401721,80.4438331)["name:ta"!~"."](12.9201721,80.1238331,13.2401721,80.4438331););out meta;>;out meta qt;
""")
for way in results.nodes:
    Name=way.tags.get("name")
    if Name==None:
        EnName=way.tags.get("name:en")
        if EnName==None: 
            EnName="None"
    else:
        Words=set('aeious')
        Ename=set(Name)
        if ((Ename & Words)==set([])):
            EnName="None"
        else:
            EnName=Name
    Id=way.id
    id=str(Id)
    osm="https://www.openstreetmap.org/node/"
    OSM=str(osm)
    Link=OSM + id
    print(EnName)
    print(id)
    inp=(id+","+Link+","+EnName)
    fobj.write('\n'+inp)
