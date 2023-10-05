# Project Title

## Description
This project aims to configure an Nginx web server on an Ubuntu 20.04 LTS server, ensuring that Nginx is running and listening on port 80 for all the server's active IPv4 IPs. The provided Bash script automates the setup and configuration of Nginx to meet these requirements.

## Table of Contents
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Nginx likes port 80](#task-0-nginx-likes-port-80)
- [Usage](#usage)
- [License](#license)

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing
- You are not allowed to use wget

## Tasks

### Task 0: Nginx likes port 80
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

**Requirements:**
- Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to the above requirements

## Usage
To use the provided Bash script to configure Nginx, follow these steps:

1. Clone this repository to your Ubuntu 20.04 LTS server.
2. Open a terminal and navigate to the project directory.
3. Make the Bash script executable by running the following command:
   ```bash
   chmod +x 0-nginx_likes_port_80

