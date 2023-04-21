# Puppet manifest to install flask using pip3
# Author: Nnaemeka Daniel John

package { 'pip3':
  ensure   => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
