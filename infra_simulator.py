import os
from src.machine import Machine
import json
import subprocess
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
list_len=len(server_list)
while True:
    
    size+=1

    # get the server details from the class Machine and then append it to the list of instances
    new_server = Machine.get_machine_details()
    server_list.append(new_server)

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
    except subprocess.CalledProcessError as e:
        print(f"Error executing the Bash script: {e}") # if faild to run the script raise an error