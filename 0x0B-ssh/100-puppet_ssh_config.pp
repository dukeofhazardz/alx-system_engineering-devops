# A puppet manifest that sets up SSH configuration file so that you can
# connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('./ssh_config.erb'),
}
