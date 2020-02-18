# CMake tests
A repo testing various features of CMAKE. This is mostly a tutorial for myself to recall what I might have surely forgotten after a while. 

## CMake exporting targets
One of the most common requirements in development is: Release parts of dependencies as libraries and applications link against them, where the location of the libraries and the applications could be different. The key is to provide this integration seamlessly.

### 01_install-method_singlee-config.in-files and 01_install-method_multiple-config.in-files
These two examples are supposed to demonstrate generating couple of targets (in this case libraries for mathematical functions addition and multiplication) and finally generating a tool that links against these libraries. They demostrate installing the generated targets to any configurable location, and the application using these generated targets with find_package function call.

The only difference between the two being one uses a single Config.cmake.in where as the other example uses multiple files, one each for each project. 

### 02_sub-directory-method
This is the simples of all the methods where the generated and the consumer projects lie in the same binary tree and are added as subdirectories in a parent CMakeLists.txt

