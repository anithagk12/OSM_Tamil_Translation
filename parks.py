import overpy
import sys
import csv
import overpass

api = overpy.Overpass()
fobj=open("Chennai_Parks.csv","w")
fobj.write("Park in Chennai")
id="ID"
name="NAME"
head=(id+","+name)
fobj.write('\n'+head)
results = api.query("""[out:json][timeout:25];
(node["leisure"="park"](12.9201721,80.1238331,13.2401721,80.4438331)["name"~"."]["name:ta"!~"."]; way["leisure"="park"](12.9201721,80.1238331,13.2401721,80.4438331); relation["leisure"="park"](12.9201721,80.1238331,13.2401721,80.4438331); );out body;>; out skel qt;
""")
for way in results.nodes:
    Name=way.tags.get("name")
    if Name==None:
        Name="None"
    Id=way.id
    id=str(Id)
    print(Name)
    print(id)
    inp=(id+","+Name)
    fobj.write('\n'+inp)
