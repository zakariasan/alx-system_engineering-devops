# Ensure 'php' is used instead of 'phpp' in the wp-settings.php file
# Ensure 'php' is used instead of 'phpp' in the wp-settings.php file
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/path/to/source/wp-settings.php'),
  replace => true,
}

exec { 'fix_phpp':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}

