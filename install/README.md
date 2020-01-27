# Demonstration of target link libraries

The idea here is to demonstrate the power of target_link_libraries and the visibility control 'public'. The calculator depends on add_lib and mul_lib libraries. This example will show how linking against these libraries is enough to get the include paths where the required headers are defined (add.h and mul.h), because the libraries are using the target_include_directories instead of the traditional include_directories


