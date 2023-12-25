# Write file in /tmp

file { '/tmp/school/0-create_a_file.pp' :
path    => '/tmp/school',
content => 'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
