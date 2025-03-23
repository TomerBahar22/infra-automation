import json
#Name of the server
name=input("enter server name :")

#type of server Operating system
os=input("enter Operating system name (e.g Linux) :")
while not os.isalpha():
    os=input("the  Operating system you have entered is incorrect please enter a valid  use only letters  :")    

#RAM Valuse size , type and usage    
ram={}

ram_size=input("enter server RAM size (e.g 16GB)  :")
while not ram_size.isdigit():
    ram_size=input("the RAM size you entered is incorrect , please enter a valid RAM size use only integers :")
ram["size"]=ram_size

ram_type=input("enter server RAM type (e.g DDR4)  :")
ram["type"]=ram_type

ram_usage=input("Enter the RAM usage percentage: ")
while not ram_usage.isdigit():
    ram_usage=input("the RAM usage you entered is incorrect , please enter a valid RAM usage use only integers :") 
ram["usage"]=ram_usage

nameoffile=(f"{name}.json")

serverinfo={
    "name":name,
    "os":os,
    "ram":ram
}
with open(nameoffile, 'w') as f:
    json.dump(serverinfo, f, indent=4)
print(f"The server information as been saved to {name}")