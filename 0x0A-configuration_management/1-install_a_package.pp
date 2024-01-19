#Using Puppet, install flask from pip3.
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

package { 'python3-pip':
  ensure  => installed,
  before  => Exec['install-flask'],
}

