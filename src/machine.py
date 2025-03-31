import logging
import os
from pydantic import BaseModel, Field

#name of log file
log_file= 'logs/provisioning.log'

# Check if the log file exists, and if not, create it
if not os.path.exists(log_file):
    with open(log_file, 'w'):  # Create the log file if it does not exist
        pass

# Set up logging for this module
logging.basicConfig(
    filename=log_file, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Sub-Class of CPU
class CPUDetails(BaseModel):
    model: str = Field(..., description="The CPU model (e.g., Intel, AMD)")
    cores: int = Field(..., ge=1, description="The number of CPU cores (e.g., 4)")
    
    def to_dict(self):
        return self.model_dump()

# Sub-Class of RAM
class RAMDetails(BaseModel):
    type: str = Field(..., description="The RAM type (e.g., DDR4)")
    size: int = Field(..., ge=1, description="The RAM size in GB (e.g., 16GB)")
    
    def to_dict(self):
        return self.model_dump()

# Main Class Machine
class Machine(BaseModel):
    name: str = Field(..., description="Server name")
    os: str = Field(..., description="Operating System (windows, linux, unix, or bsd)")
    ram: RAMDetails
    cpu: CPUDetails
    disk: str = Field(..., description="Disk details")
    
    #convert the class to dicanatory
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu.to_dict(),
            "ram": self.ram.to_dict(),
            "disk": self.disk
        }
    
    #functaion for the user to input all values
    @staticmethod
    def get_machine_details():
        
        #Verify that name is not empty
        while True:
            name = input("Enter machine name: ")
            if name.strip():
                break
            print("Name cannot be empty.")

        #Verify that os is either windows, linux, unix or bsd
        while True:
            os = input("Enter operating system (windows, linux, unix, or bsd): ").lower()
            if os in {"windows", "linux", "unix", "bsd"}:
                break
            print("Invalid OS input. Please enter 'windows', 'linux', 'unix', or 'bsd'.")

        #Verify that CPU model isnt empty
        while True:
            model = input("Enter CPU model (e.g., Intel, AMD): ")
            if model.strip():
                break
            print("CPU model cannot be empty.")

        #Verify that CPU cores is bigger than 1 and an integer
        while True:
            try:
                cores = int(input("Enter number of CPU cores (e.g., 4): "))
                if cores >= 1:
                    break
                print("CPU cores must be at least 1.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        #Verify that RAM type isnt empty
        while True:
            ram_type = input("Enter RAM type (e.g., DDR4): ")
            if ram_type.strip():
                break
            print("RAM type cannot be empty.")

        #Verify that RAM size is bigger that 1 and an integer
        while True:
            try:
                ram_size = int(input("Enter RAM size in GB (e.g., 16): "))
                if ram_size >= 1:
                    break
                print("RAM size must be at least 1 GB.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        #Verify that disck isnt empty
        while True:
            disk = input("Enter Server disk: ")
            if disk.strip():
                break
            print("Disk cannot be empty.")
        
                

        cpu_details = CPUDetails(model=model, cores=cores) # Adding the value from the user input to CPU subclass

        ram_details = RAMDetails(type=ram_type, size=ram_size) #Adding the value from the user input to RAM subclass

        machine = Machine(name=name, os=os, ram=ram_details, cpu=cpu_details, disk=disk) #Adding the Values from the user input to machine class

        machine_dict = machine.to_dict() # conver the machine values to a dict using to_dict function

        logging.info(f"Machine details: {machine_dict}") #log that the machine was created
        return machine_dict
