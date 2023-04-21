# Puppet manifest to kill a process named killmenow using `pkill`
# Author: Nnaemeka Daniel John

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
