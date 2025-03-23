import json

#function to check if the input is float 
def is_float(num):
    try:
        if float(num) and "." in num: 
            return True
    except ValueError:
        return False

#Name of the server
name=input("Enter server name :")

#type of server Operating system
os=input("Enter Operating system name (e.g Linux) :")
while os.lower() not in ["windows" , "linux" , "unix", "bsd"]:
    os=input("the  Operating system you have entered doesnt exist please enter a valid one (e.g Linux)  :")    

#RAM Valuse size , type and usage    
ram={}

ram_size=input("Enter server RAM size (e.g 16GB)  :")
while not ram_size.isdigit():
    ram_size=input("the RAM size you entered is incorrect , please enter a valid RAM size use only integers :")
ram["size"]=ram_size

ram_type=input("Enter server RAM type (e.g DDR4)  :")
ram["type"]=ram_type

ram_usage=input("Enter the RAM usage percentage: ")
while not ram_usage.isdigit():
    ram_usage=input("the RAM usage you entered is incorrect , please enter a valid RAM usage use only integers :") 
ram["usage"]=ram_usage
#CPU info model , cores , usage
cpu={}

cpu_model=input("Enter a CPU model (e.g AMD )")
cpu["model"]=cpu_model

cpu_cores=input("Enter a CPU cores (e.g 12 )")
while not cpu_cores.isdigit():
    cpu_cores=input("The CPU cores you enter is incorrect , please enter a valid CPU cores use only integers (e.g 12 )")
cpu["cores"]=cpu_cores

cpu_usage=input("Enter a CPU usage (e.g 30.5 )")  
while not is_float(cpu_usage):
     cpu_usage=input("The CPU usage you enter is incorrect , please enter a valid CPU usage use only integers (e.g 30.5 )")
cpu["usage"]=cpu_usage

#the name of the file
nameoffile=(f"{name}.json")

#dictionary of the server info
serverinfo={
    "name":name,
    "os":os,
    "RAM":ram,
    "CPU":cpu

}
#import my dictionary to json file 
with open(nameoffile, 'w') as f:
    json.dump(serverinfo, f, indent=4)

#output to user that the process was sucssesful
print(f"The server information as been saved to {name}")