# A puppet manifest

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80;
      server_name localhost;

      location / {
        return 200 'Hello World!\n';
      }

      location /redirect_me {
        return 301 /;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Enable Nginx server
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Start Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
}
