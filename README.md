Infra Automation
Overview
infra-automation is a Python-based project for automating the provisioning of server infrastructure. It allows users to create machine configurations interactively, stores them in a JSON file, and runs installation scripts for services like Nginx on the created machines.

The project is structured with Python classes for defining machine details, logging the process, and running bash scripts for installing and configuring services.

Features
Server Configuration: Allows users to define machine specifications (name, OS, CPU, RAM, disk).

Logging: Logs all actions, including machine creation and script execution.

JSON Configuration: Stores the created machine details in a instances.json file.

Automation Scripts: Runs installation scripts (like Nginx installation) on the provisioned machines.

Requirements
Python 3.x or higher

Bash (for running scripts)

pydantic (for data validation)

subprocess (for running shell commands)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/TomerBahar22/infra-automation.git
cd infra-automation
Install required Python dependencies:

bash
Copy
Edit
pip install pydantic
Ensure that scripts/install_config_service.sh is available and executable:

bash
Copy
Edit
chmod +x scripts/install_config_service.sh
Configuration
Log File: All logs are saved to logs/provisioning.log.

Instances File: Machine configurations are stored in configs/instances.json.

If instances.json doesn't exist, it will be created automatically when the script runs.

Usage
Run the provisioning script to start creating machines:

bash
Copy
Edit
python provision.py
Follow the interactive prompts to input machine details:

Machine Name

Operating System (choose from: windows, linux, unix, bsd)

CPU Model and Cores

RAM Type and Size

Disk Details

Once the machines are defined, you will be asked if you'd like to install a service (e.g., Nginx) on each of the machines.

If you confirm, the installation script (scripts/install_config_service.sh) will be executed on the provisioned machines.

Example
When running the provision.py script, the program will:

Ask for machine details.

Log the details into logs/provisioning.log.

Save the list of provisioned machines to configs/instances.json.

If you choose to install a service, the corresponding bash script will be executed to install the service on the machines.
