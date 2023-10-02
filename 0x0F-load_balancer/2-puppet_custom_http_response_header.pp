# This Puppet manifest configures Nginx to add a custom HTTP response header on a new Ubuntu machine.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx with custom HTTP response header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

