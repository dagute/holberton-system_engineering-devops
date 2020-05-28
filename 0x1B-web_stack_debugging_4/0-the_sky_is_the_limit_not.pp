#change the limit

exec { 'increase':
  command  => "sed -i 's/15/5000/g' /etc/default/nginx",
  path     => '/bin',
  provider => 'shell'
}

exec { 'restart':
  command  => 'nginx restart',
  path     => '/etc/init.d/',
  provider => 'shell'
}
