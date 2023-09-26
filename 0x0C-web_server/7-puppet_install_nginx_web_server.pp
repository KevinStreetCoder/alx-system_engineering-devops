# Ensure Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create a custom Nginx virtual host configuration
file { '/etc/nginx/sites-available/redirect':
  ensure => present,
  content => "server {
    listen 80;
    server_name your_domain.com; # Replace with your actual domain

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    # Additional server configuration if needed
  }",
  require => Package['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/redirect':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect'],
}

# Create a custom HTML page with "Hello World!"
file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Test Nginx configuration and reload it
exec { 'nginx-config-reload':
  command     => '/usr/sbin/nginx -t && /usr/sbin/service nginx reload',
  refreshonly => true,
  require     => [
    Package['nginx'],
    Service['nginx'],
    File['/etc/nginx/sites-available/redirect'],
    File['/etc/nginx/sites-enabled/redirect'],
    File['/usr/share/nginx/html/index.html'],
  ],
}

# Notify the service to restart when configuration changes
Service['nginx'] ~> Exec['nginx-config-reload']
