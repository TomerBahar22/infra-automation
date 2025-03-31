import logging
import os
from pydantic import BaseModel, Field

# Set up logging
log_file = 'logs/machine_creation.log'
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file),
    logging.StreamHandler()
])
logger = logging.getLogger(__name__)

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
    
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu.to_dict(),
            "ram": self.ram.to_dict(),
            "disk": self.disk
        }
    
    @staticmethod
    def get_machine_details():
        name = input("Enter machine name: ")

        while True:
            os = input("Enter operating system (windows, linux, unix, or bsd): ").lower()
            if os in {"windows", "linux", "unix", "bsd"}:
                break
            print("Invalid OS input. Please enter 'windows', 'linux', 'unix', or 'bsd'.")

        while True:
            model = input("Enter CPU model (e.g., Intel, AMD): ")
            if model.strip():
                break
            print("CPU model cannot be empty.")

        while True:
            try:
                cores = int(input("Enter number of CPU cores (e.g., 4): "))
                if cores >= 1:
                    break
                print("CPU cores must be at least 1.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            ram_type = input("Enter RAM type (e.g., DDR4): ")
            if ram_type.strip():
                break
            print("RAM type cannot be empty.")

        while True:
            try:
                ram_size = int(input("Enter RAM size in GB (e.g., 16): "))
                if ram_size >= 1:
                    break
                print("RAM size must be at least 1 GB.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        disk = input("Enter Server disk: ")
                

        cpu_details = CPUDetails(model=model, cores=cores)
        ram_details = RAMDetails(type=ram_type, size=ram_size)
        machine = Machine(name=name, os=os, ram=ram_details, cpu=cpu_details, disk=disk)
        machine_dict = machine.to_dict()

        logger.info(f"Machine created: {machine_dict}")
        return machine_dict
