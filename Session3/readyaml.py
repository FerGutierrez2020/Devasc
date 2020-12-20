import yaml 
with open("fileforYAML.yml") as data:
    yaml_sample = data.read() 
    yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)
print(yaml_dict)
yaml_dict["interface"]["name"] = "GigabitEthernet1"

with open("fileforYAML.yml", "w") as data: 
    data.write(yaml.dump(yaml_dict, default_flow_style=False))
#print(yaml_dict)

#print (type(yaml_dict))
#print(yaml_dict)
#print(yaml.dump(yaml_dict, default_flow_style=False))

