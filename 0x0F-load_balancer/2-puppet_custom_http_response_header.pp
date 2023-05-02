# A Puppet manifesto to automate the task of creating a custom HTTP header response

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Define custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "add_header X-Served-By ${hostname};",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Class['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
}
