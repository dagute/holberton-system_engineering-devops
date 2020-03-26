#Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/usr/share/nginx/html/index.html':
  content => 'Holberton School',
  path    => '/usr/share/nginx/html/index.html'
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
