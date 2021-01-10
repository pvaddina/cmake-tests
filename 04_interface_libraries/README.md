# Using interface libraries

## Directory: generator
Contains a header only library (the super complicated addition and multiplication function implementations). Use the provided 'generator/build.sh' script to build, and install the library. The install step shall install the cmake config files

## Directory: consumer
Consumes the header only library 'add_mul_lib' and it happens as any other normal library using find_package and target_link_libraries. 
