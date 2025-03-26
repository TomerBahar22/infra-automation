# import json
# import machine

# #Name of the server
# name=machine.get_name()

# #type of server Operating system


# #RAM Valuse size , type and usage    

# #CPU info model , cores , usage


# #the name of the file
# nameoffile="instances.json"

# #dictionary of the server info
# serverinfo={
#     "name":name,
#     "os":os,
#     "RAM":ram,
#     "CPU":cpu

# }
# #import my dictionary to json file 
# with open(nameoffile, 'w') as f:
#     json.dump(serverinfo, f, indent=4)

# #output to user that the process was sucssesful
# print(f"The server information as been saved to {nameoffile}")