# Increases the amount of traffic an Nginx server can handle.

# Define the path to the nginx configuration file
$nginx_config_file = '/etc/default/nginx'

# Increase the ULIMIT in the nginx configuration file
file_line { 'increase_nginx_ulimit':
  path    => $nginx_config_file,
  line    => 'ulimit -n 4096',
  match   => '^ulimit -n.*',
  ensure  => present,
  notify  => Exec['nginx-restart'],
}

# Restart Nginx using systemctl
exec { 'nginx-restart':
  command     => '/bin/systemctl restart nginx',
  refreshonly => true,
  subscribe   => File_line['increase_nginx_ulimit'],
  logoutput   => true,
}

