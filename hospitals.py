import overpy
import sys
import csv
import overpass

api = overpy.Overpass()
fobj=open("Chennai_Hospitals.csv","w")
fobj.write("Hospitals in Chennai")
id="ID"
name="NAME"
head=(id+","+name)
fobj.write('\n'+head)
results = api.query("""[out:json][timeout:3600][bbox:12.9201721,80.1238331,13.2401721,80.4438331];(node["amenity"="hospital"]["name"~"."]["name:ta"!~"."];);out meta;
""")
for way in results.nodes:
    Name=way.tags.get("name")
    if Name is  None:
        Name="None"
    Id=way.id
    id=str(Id)
    print(Name)
    print(id)
    inp=(id+","+Name)
    fobj.write('\n'+inp)


