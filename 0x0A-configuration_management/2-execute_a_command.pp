#Using Puppet, create a manifest that kills a process named killmenow.

exec { 'killmenow':
  command     => '/usr/bin/pkill -f "killmenow"',
  refreshonly => true,
  subscribe   => File['/path/to/killmenow_script'],
}

file { '/path/to/killmenow_script':
  ensure  => present,
  mode    => '0755',
  content => "#!/bin/bash\nwhile true; do sleep 2; done\n",
}
