import json
with open("fileforjson.json") as data: 
   json_data = data.read() 
   
json_dict = json.loads(json_data)

type(json_dict)
print(json_dict)

###Modificando el campo description####
json_dict["interface"]["description"] = "Backup Link"

###Guardando la nueva info en el archivo json###
with open("fileforjson.json", "w") as fh: 
    json.dump(json_dict, fh, indent = 4)

print(json_dict)