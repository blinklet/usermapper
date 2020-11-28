# Usermapper #

Create a complex Guacamole manual authentication file, saved as */etc/guacamole/user-mapping.xml*, from a simple confuration file.

## Install ##

This is a Python program. Install from Github:

    $ pip install git+https://github.com/blinklet/usermapper.git@v0.3#egg=usermapper

## Usage ##

Look at the *example-config.yaml* file in this repository to see the configuration file format. This is an opinionated script designed to support training labs. I assume every user will have access to every device in the lab.

Save the configuration file. Then run the script. 

To use default filenames, where the configuration script is named *config.yaml* and the output file will be named *user-mapping.xml* and both files are in the current directory, run the script as follows:

    $ python3 -m usermapper

To choose either the input file or the output file, or both, use the options flags as follows:

    $ python3 -m usermapper -i <input filename> -o <output filename>

For example:

    $ python3 -m usermapper -i test.yaml -o /tmp/guac/map.xml
