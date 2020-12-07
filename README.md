# Ansible role for nginx installation

## Usage

1. Clone the repository
2. Run the next commands
```
chmod +x start.sh
chmod +x inventory_generator.py
```
3. Define a list of hosts, separated by commas. For example, `127.0.0.1,127.0.0.2`.
4. Run `start.sh` with parameters
```start.sh hosts_list username keyfile_location```. Fill the prompt
5. Wait until script is done
6. Check a result