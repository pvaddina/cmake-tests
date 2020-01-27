# Demonstration of CMake install options

[CMake example on Testing and Installing](https://cmake.org/cmake/help/latest/guide/tutorial/index.html#installing-and-testing-step-4)

When installing the project, where are the files installed ? Here a snipppet from the same link above
> The CMake variable CMAKE_INSTALL_PREFIX is used to determine the root of where the files will be installed. 
> If using cmake --install a custom installation directory can be given via --prefix argument. For 
> multi-configuration tools, use the --config argument to specify the configuration.

If you see an error like while installing the project (ex: 'make install') 
> [ 50%] Built target add
> [100%] Built target mul
> Install the project...
> -- Install configuration: ""
> -- Installing: /usr/local/lib/libadd.a
> CMake Error at add_lib/cmake_install.cmake:41 (file):
>   file INSTALL cannot copy file
>   "/home/vaddina/workspace/cmake-tests/install/calc_lib/build/add_lib/libadd.a"
>   to "/usr/local/lib/libadd.a".
> Call Stack (most recent call first):
>   cmake_install.cmake:42 (include)

Then try the same command with higher privileges:
> sudo make install
> [sudo] password for vaddina: 
> [ 50%] Built target add
> [100%] Built target mul
> Install the project...
> -- Install configuration: ""
> -- Installing: /usr/local/lib/libadd.a
> -- Installing: /usr/local/lib/libmul.a

