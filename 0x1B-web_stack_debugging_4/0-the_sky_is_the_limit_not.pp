#change the limit

exec { 'increase':
  command => "sed -i 's/15/64000/g' /etc/default/nginx",
  path    => '/bin'
}

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
