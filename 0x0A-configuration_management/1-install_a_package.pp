#Instal python flask from pip3

package { 'flask' :
ensure          => 'installed'
install_options => ['-I', '2.1.0'],
provider        => 'pip3',
}
