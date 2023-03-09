0x01-shell_permissions
This directory contains scripts that demonstrate how to manage file and directory permissions in a Linux shell environment. The scripts cover topics such as using commands like chmod, chown, and chgrp to modify permissions, changing file ownership and group membership, and running commands with elevated privileges using sudo. The README.md file in this directory provides an overview of the scripts and their functions.

Files
0-iam_betty: changes the user ID to betty
1-who_am_i: prints the effective user ID
2-groups: prints all the groups the current user is a part of
3-new_owner: changes the owner of the file hello to the user betty
4-empty: creates an empty file called hello
5-execute: adds execute permission to the owner of the file hello
6-multiple_permissions: adds execute permission to the owner and group owner and read permission to other users to the file hello
7-everybody: adds execute permission to all users to the file hello
8-James_Bond: sets the file hello's permissions to 007
9-John_Doe: sets the mode of the file hello to -rwxr-x-wx
10-mirror_permissions: sets the mode of the file hello to the same as olleh
11-directories_permissions: adds execute permission to all subdirectories of the current directory
12-directory_permissions: creates a directory called dir_holberton with specific permissions
13-change_group: changes the group owner of the file hello to holberton.