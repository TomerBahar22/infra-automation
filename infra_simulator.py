import logging
import os
from src.machine import Machine
import json
import subprocess

log_file = 'logs/provisioning.log'

# Check if the log file exists
if not os.path.exists(log_file):
    with open(log_file, 'w'):  # Create the log file if it does not exist
        pass
    
# Set up logging for this script
logging.basicConfig(
    filename=log_file, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

config_path = "configs/instances.json"

# Check if the file exists and is not empty
if os.path.exists(config_path) and os.path.getsize(config_path) > 0:
    # If the file exists and has content, load it
    with open(config_path, "r") as f:
        server_list = json.load(f)
else:
    # If the file is empty or doesn't exist, create an empty list
    server_list = []

#save the amount of servers you made each run of the scripts 
size=0 
# save the amout of servers you have before running the script 
list_len=len(server_list)

#a loop to run for each server the user choose to add
while True:

    size+=1
    # get the server details from the class Machine and then append it to the list of instances
    new_server = Machine.get_machine_details()
    server_list.append(new_server)
    logging.info(f"Created a new server: {new_server['name']} with OS: {new_server['os']}")
    # Write the updated server list back to the file
    with open(config_path, "w") as f:
        json.dump(server_list, f, indent=4)  # Use json.dump to save the updated list
    if input("would you like to create another machine (type yes for another or type everything else for no):").strip().lower() == "yes": # Ask if you wish to create another machine or finish
        continue
    else:
        break
    
#ask for each machine that you made if you want to install nginx
for i in range(size):
    print(f"Running installation script for machine {list_len+i}...")
    bash_script = 'scripts/install_config_service.sh' #Path to the Bash script
    try:
        subprocess.run(['bash', bash_script], check=True) # using subprocess to try and run the bash script 
        logging.info(f"Successfully ran the installation script for machine {list_len + i}.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing the Bash script: {e}") # if faild to run the script raise an error
        logging.error(f"Error executing the Bash script for machine {list_len + i}: {e}")