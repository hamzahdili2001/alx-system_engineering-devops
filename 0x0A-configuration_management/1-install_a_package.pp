# Ensure that the python3-pip package is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask using pip3 with the specified version
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
  creates => '/usr/local/lib/python3.8/dist-packages/flask',
}
