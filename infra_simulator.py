import os
from src.machine import Machine
import json
config_path = "configs/instances.json"

# Check if the file exists and is not empty
if os.path.exists(config_path) and os.path.getsize(config_path) > 0:
    # If the file exists and has content, load it
    with open(config_path, "r") as f:
        server_list = json.load(f)
else:
    # If the file is empty or doesn't exist, initialize an empty list
    server_list = []

# get the server details from the class Machine and then append it to the list of instances
new_server = Machine.get_machine_details()
server_list.append(new_server)

# Write the updated server list back to the file
with open(config_path, "w") as f:
    json.dump(server_list, f, indent=4)  # Use json.dump to save the updated list
