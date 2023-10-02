# Project: Load Balancer Configuration

This project involves configuring a load balancer and setting up redundancy for web servers. It includes Bash scripts and Puppet manifests to automate the configuration of Ubuntu servers. The goal is to enhance the reliability and scalability of the infrastructure.

## Table of Contents

- [Task 0: Double the number of webservers](#task-0-double-the-number-of-webservers)
- [Task 1: Install your load balancer](#task-1-install-your-load-balancer)
- [Task 2: Add a custom HTTP header with Puppet](#task-2-add-a-custom-http-header-with-puppet)

## Task 0: Double the number of webservers

In this task, we configure web-02 to be identical to web-01 and add a custom Nginx response header to track which web server is answering HTTP requests.

