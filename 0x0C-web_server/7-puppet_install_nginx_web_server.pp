#ime to practice configuring your server with Puppet! 
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /404.html {
        internal;
    }

    location = /redirect_me {
        return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
    }

    location = / {
        return 200 'Hello World!';
    }
}
",
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
