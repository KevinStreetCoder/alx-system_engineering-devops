# Puppet Configuration Management Project

This project contains Puppet manifests for performing various configuration management tasks on an Ubuntu 20.04 LTS system. The tasks include creating files, installing packages, and executing commands using Puppet.

## Requirements

- Ubuntu 20.04 LTS
- Puppet 5.5
- Puppet-lint 2.1.1
- Ruby 2.7
- Ruby-augeas
- Ruby-shadow

## Usage

1. Clone this repository to your Ubuntu 20.04 LTS system.
2. Install Puppet and Puppet-lint using the provided commands in the project requirements.
3. Navigate to the project directory.
4. Use the following commands to execute the Puppet manifests:

   - Task 0: Create a file
     ```
     sudo puppet apply 0-create_a_file.pp
     ```

   - Task 1: Install a package
     ```
     sudo puppet apply 1-install_a_package.pp
     ```

   - Task 2: Execute a command
     ```
     sudo puppet apply 2-execute_a_command.pp
     ```

## Files

- `0-create_a_file.pp`: Puppet manifest to create a file in `/tmp`.
- `1-install_a_package.pp`: Puppet manifest to install the Flask package.
- `2-execute_a_command.pp`: Puppet manifest to execute a command to kill a process.

## Author

@KevinStreetCoder

## @ALX

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
