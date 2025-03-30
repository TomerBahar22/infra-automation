import logging
from pydantic import BaseModel, Field, field_validator, ValidationError

# Set up logging
log_file = 'logs/machine_creation.log'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler(log_file),  # Write logs to file
        logging.StreamHandler()         # Also display logs to the console
    ])
logger = logging.getLogger(__name__)

#Sub-Class of CPU
class CPUDetails(BaseModel):
    model: str = Field(..., description="The CPU model (e.g., Intel, AMD)")
    cores: int = Field(..., ge=1, description="The number of CPU cores (e.g., 4)")

    #Validaet model is a string
    @field_validator('model')
    def validate_cpu_model(value):
        if not isinstance(value, str):
            raise ValueError("CPU model must be a string (e.g., Intel, AMD).")
        return value

    #Validaet cores is an int
    @field_validator('cores')
    def validate_cpu_cores(value):
        if not isinstance(value, int):
            raise ValueError("CPU cores must be a number (e.g., 4).")
        return value

    #Convert Cpu to a dictanory
    def to_dict(self):
        return self.model_dump()

#Sub-Class of RAM
class RAMDetails(BaseModel):
    type: str = Field(..., description="The RAM type (e.g DDR4)")
    size: int = Field(..., ge=1, description="The RAM size in GB (e.g 16GB)")

    #Validaet type is a str
    @field_validator('type')
    def validate_ram_type(value):
        if not isinstance(value, str):
            raise ValueError("RAM type must be a valid name (e.g., DDR4).")
        return value

    #Validaet size is an int
    @field_validator('size')
    def validate_ram_size(value):
        if not isinstance(value, int):
            raise ValueError("RAM size must be a number (e.g., 4).")
        return value

    #Convert RAM to a dictanory
    def to_dict(self):
        return self.model_dump()


#MainClass Machine
class Machine(BaseModel):
    name: str = Field(..., description="Server name")
    os: str = Field(..., pattern="^(windows|linux|unix|bsd)$", description="Operating System (windows, linux, unix, or bsd)")
    ram: RAMDetails = Field(..., description="RAM details")
    cpu: CPUDetails = Field(..., description="CPU details")
    memory: int = Field(..., description="Memory details")

    #Validaet os is windows ,linux , unix , bsd
    @field_validator('os')
    def validate_os(value):
        if value.lower() not in {"windows", "linux", "unix", "bsd"}:
            raise ValueError("Operating System must be (windows, linux, unix, or bsd).")
        return value

    #Validaet total is a float or int
    @field_validator('memory')
    def validate_memory_total(value):
        if not isinstance(value, (float, int)):
            raise ValueError("Memory total must be a number (e.g., 32GB).")
        return value

    #return a dicanory of my class only work without iser input
    def to_dict(self):
        return {
        "name": self.name,
        "os": self.os,
        "cpu": self.cpu.to_dict(),
        "ram": self.ram.to_dict(),
        "memory": self.memory.to_dict()
    }

    @staticmethod
    def get_machine_details():
        # Get machine name
        name = input("Enter machine name: ")

        # Get and validate OS
        while True:
            os = input("Enter operating system (windows, linux, unix, or bsd): ").lower()
            if os in {"windows", "linux", "unix", "bsd"}:
                break  # valid input, exit loop
            else:
                print("Invalid OS input. Please enter 'windows', 'linux', 'unix', or 'bsd'.")

        # Get and validate CPU model
        while True:
            model = input("Enter CPU model (e.g., Intel, AMD): ")
            if model.strip():  # Ensure model is not empty
                break  # valid input, exit loop
            else:
                print("CPU model cannot be empty. Please enter a valid CPU model.")

        # Get and validate CPU usage
        while True:
            try:
                usage = float(input("Enter CPU usage percentage (0-100): "))
                if 0 <= usage <= 100:
                    break  # valid input, exit loop
                else:
                    print("CPU usage must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 0 and 100.")

        # Get and validate number of CPU cores
        while True:
            try:
                cores = int(input("Enter number of CPU cores (e.g., 4): "))
                if cores >= 1:
                    break  # valid input, exit loop
                else:
                    print("CPU cores must be at least 1.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of CPU cores.")

        # Get and validate RAM type
        while True:
            ram_type = input("Enter RAM type (e.g., DDR4): ")
            if ram_type.strip():  # Ensure RAM type is not empty
                break  # valid input, exit loop
            else:
                print("RAM type cannot be empty. Please enter a valid RAM type.")

        # Get and validate RAM size
        while True:
            try:
                ram_size = int(input("Enter RAM size in GB (e.g., 16): "))
                if ram_size >= 1:
                    break  # valid input, exit loop
                else:
                    print("RAM size must be at least 1 GB.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the RAM size.")

        # Get and validate RAM usage
        while True:
            try:
                ram_usage = float(input("Enter RAM usage percentage (0-100): "))
                if 0 <= ram_usage <= 100:
                    break  # valid input, exit loop
                else:
                    print("RAM usage must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number for RAM usage.")

        # Get and validate memory total
        while True:
            try:
                memory = float(input("Enter total memory in GB: "))
                if memory > 0:
                    break  # valid input, exit loop
                else:
                    print("Total memory must be a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number for total memory.")


        # Create and return the Machine instance
        cpu_details = CPUDetails(model=model, usage=usage, cores=cores)
        ram_details = RAMDetails(type=ram_type, size=ram_size, usage=ram_usage)

        machine = Machine(name=name, os=os, ram=ram_details, cpu=cpu_details, memory=memory)

        # Return a dictionary with each key separately
        machine_dict = {
            "name": machine.name,
            "os": machine.os,
            "cpu": machine.cpu.to_dict(),
            "ram": machine.ram.to_dict(),
            "memory": machine.memory.to_dict()
        }

        logger.info(f"Machine created: {machine_dict}")
        return machine_dict