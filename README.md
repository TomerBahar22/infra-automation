# DevOps Infrastructure Provisioning & Configuration Automation Project

## Overview

This project is a modular Python-based infrastructure provisioning and configuration automation tool. Initially, it simulates infrastructure provisioning, but future enhancements will integrate AWS and Terraform to create real resources. The goal is to provide a solid foundation for automating infrastructure deployment and service configuration.

## Features

- Accepts user inputs for defining virtual machines (VMs).
- Validates input using Python.
- Uses an object-oriented, modular code structure.
- Automates service installation using Bash scripts.
- Implements logging and error handling for reliability.

---

## Project Structure

```
infra-automation/
|-- scripts/       # Bash scripts for automation
|-- configs/       # Configuration files (e.g., instances.json)
|-- logs/          # Log files for tracking execution
|-- src/           # Python source code for infrastructure automation
|-- README.md      # Project documentation
```

---

## Setup & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/TomerBahar22/infra-automation.git
cd infra-automation
```

### 2. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Infrastructure Provisioning Tool

Run the main script to start the provisioning process:
```bash
python src/infra_simulator.py
```

The script will prompt the user to define virtual machines dynamically. Configurations will be validated and stored in `configs/instances.json`.

### Example Execution
```bash
Enter VM Name: VM1
Enter OS (Ubuntu/CentOS): Ubuntu
Enter CPU Cores: 4
Enter RAM (GB): 8
Enter Disk: 8

Provisioning virtual machine: VM1
Validating inputs...
Machine VM1 created successfully!
Starting service installation...
Service installation completed successfully.
```

---

## Logging & Error Handling

Logs are stored in `logs/provisioning.log` and include:
- Provisioning start and end timestamps.
- Any errors encountered.
- Success messages for completed actions.

### Checking Logs
To view logs, use:
```bash
tail -f logs/provisioning.log
```

---

## Future Enhancements

- Integrate AWS to provision real cloud instances.
- Automate infrastructure management using Terraform.
- Expand service configurations with more automation capabilities.



