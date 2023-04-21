# Puppet manifest to create a file in /tmp/school with specific permissions and ownership
# Author: Nnaemeka Daniel John

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
