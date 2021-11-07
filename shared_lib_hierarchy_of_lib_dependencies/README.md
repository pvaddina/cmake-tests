# Demonstration of generating and using shared libraries with complex hierarchy

The aim of this example is to showcase this complex hierarcy of dependencies and how that effects the linker and run time.

In this example, we have four project where they are related to each other as follows:

1. addsub and muldiv are individual projects providing basic arithmetic operations like addition, subtraction, multiplication and division. They are standalone shared libraries which do not have any other dependencies
2. arthmeticop is a project that depends on addsub and muldiv projects and provides a single interface for all basic arithmetic operations
3. calc is the consumer project which only relies on arthmeticop project to build. However at run time the addsub and muldiv binaries also need to be available to successfully run the application. Observe the CMakeLists.txt file for the 'calc' project which (especially for Linux) tries to disable checking for dependencies at linking time. 

Note that this project does not support proper installation and appropriate cmake scripts to find the package. This is not the aim of this project.

