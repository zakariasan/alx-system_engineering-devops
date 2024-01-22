#  Bash script that uses ssh to connect to your server using the private key 
# 100-puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/home/your_username/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}
