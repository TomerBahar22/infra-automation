#function to check if the input is float 
def is_float(num):
    try:
        if float(num) and "." in num: 
            return True
    except ValueError:
        return False
        
#the class Machine 
class Machine:
    def __init__(self, ram, cpu , os , name ,memory):
        self.ram = ram
        self.cpu=cpu
        self.os=os
        self.name=name
        self.memory=memory
    
    #RAM Valuse size , type and usage
    def get_ram():
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
        
        return ram
    
    #Name of the server
    def get_name():
        name=input("Enter server name :")
        
        return name

    #type of server Operating system
    def get_os():
        os=input("Enter Operating system name (e.g Linux) :")
        while os.lower() not in ["windows" , "linux" , "unix", "bsd"]:
            os=input("the  Operating system you have entered doesnt exist please enter a valid one (e.g Linux)  :")   
       
        return os 

    #CPU info model , cores , usage
    def get_cpu():
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
        
        return cpu
    
    #make dicmemory total , used , free , usage
    def get_memory():
        memory={}
        memory_total=input("Enter memory total (e.g 32GB) :")
        while not memory_total.isdigit():
            memory_total=input("The memory total you have entered isnt valid please enter a valid one using integers (e.g 32GB) :")
        memory["total"]=memory_total

        memory_used=input("Enter memory total (e.g 12B) :")
        while not memory_used.isdigit():
            memory_used=input("The memory used you have entered isnt valid please enter a valid one using integers (e.g 12B) :")
        memory["used"]=memory_used

        memory_free=input("Enter memory total (e.g 20GB) :")
        while not memory_free.isdigit():
            memory_free=input("The memory free you have entered isnt valid please enter a valid one using integers (e.g 20GB) :")
        memory["free"]=memory_free

        memory_usage=input("Enter memory usage (e.g 37.5) :")
        while not is_float(memory_usage):
            memory_usage=input("The memory usage you have entered isnt valid please enter a valid one using float numbers (e.g 37.5) :")
        memory["usage"]=memory_usage
        
        return memory