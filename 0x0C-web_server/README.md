# Project: Web Server Configuration with Puppet

## Introduction

This project focuses on configuring a web server using Puppet, specifically Nginx, to meet specific requirements. The tasks involve installing and configuring Nginx, creating custom pages, and setting up redirections.

## Task 1: Install and Configure Nginx with Puppet

To install and configure Nginx using Puppet, we created a Puppet manifest file named `7-puppet_install_nginx_web_server.pp`. The manifest accomplishes the following tasks:

- Ensures that the Nginx package is installed.
- Ensures that the Nginx service is enabled and running.
- Creates a custom Nginx virtual host configuration for redirection.
- Creates a symbolic link to enable the site.
- Creates a custom HTML page with "Hello World!"
- Tests the Nginx configuration and reloads it when changes are made.
- Notifies the service to restart when configuration changes.

You can apply this Puppet manifest to your server to configure Nginx with the specified requirements.

## Requirements

The following requirements were met in the Puppet manifest:

1. Nginx should be listening on port 80.
2. When querying Nginx at its root `/` with a GET request, it returns a page containing the string "Hello World!"
3. The redirection is a "301 Moved Permanently."

## Usage

Apply the Puppet manifest to your server as follows:

```bash
sudo puppet apply 7-puppet_install_nginx_web_server.pp
