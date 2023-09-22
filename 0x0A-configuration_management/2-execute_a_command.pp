# This Puppet manifest executes a command to kill a process named 'killmenow.'

exec { 'killmenow':
  command => 'pkill killmenow',
  # Ensure that the process is killed if it exists.
  onlyif  => 'pgrep killmenow',
}
