# A Puppet manifesto to automate the task of creating a custom HTTP header response

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Define custom header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};"
  match   => '^# custom headers$\n',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  notify  => Service['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
  notify  => Service['nginx'],
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
