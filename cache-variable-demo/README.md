# Demonstrate using cache variables

Ignore the project code.

First see how the variable can be set from the command line

```console
>> cmake ..
NON_CACHE_VARIABLE=Default value of non-cache variable
STRING_CACHE_VARIABLE=Default value of cache variable
BOOL_CACHE_VARIABLE=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /home/vaddina/workspace/cmake-tests/cache-variable-demo/build

>> cmake .. -DSTRING_CACHE_VARIABLE="A new value for Foo_DEFINITION" -DBOOL_CACHE_VARIABLE=ON -DNON_CACHE_VARIABLE="non-cache variable is also replaced" 
NON_CACHE_VARIABLE=Default value of non-cache variable
STRING_CACHE_VARIABLE=A new value for Foo_DEFINITION
BOOL_CACHE_VARIABLE=ON
-- Configuring done
-- Generating done
-- Build files have been written to: /home/vaddina/workspace/cmake-tests/cache-variable-demo/build
```

After the last command execution check the file **CMakeCache.txt** and notice that the variable *NON_CACHE_VARIABLE* is defined as *uninitialized*. This is because using the command as above with *-DNON_CACHE_VARIABLE="non-cache variable is also replaced"* we have inadvertently created yet another cache variable. This is to demonstrate that one cannot change the value of a **normal** variable via the command line but only that of the **cache** variables. Trying to do so will create yet another uninitialized cache variable with the same name. 

```console
//Demo bool cache variable
BOOL_CACHE_VARIABLE:BOOL=ON

//No help, variable specified on the command line.
NON_CACHE_VARIABLE:UNINITIALIZED=non-cache variable is also replaced

//Demo string cache variable
STRING_CACHE_VARIABLE:STRING=A new value for Foo_DEFINITION
```

Unless a new value is passed from the command line, the current value as in the CMakeCache.txt will not be overwritten, despite the fact that it has been assigned a value using the **SET** command in the CMakeLists.txt


```console
>> cmake ..
NON_CACHE_VARIABLE=Default value of non-cache variable
STRING_CACHE_VARIABLE=A new value for Foo_DEFINITION
BOOL_CACHE_VARIABLE=ON
-- Configuring done
-- Generating done
-- Build files have been written to: /home/vaddina/workspace/cmake-tests/cache-variable-demo/build

>> cmake .. -DSTRING_CACHE_VARIABLE="Yet another value for STRING_CACHE_VARIABLE"  -DNON_CACHE_VARIABLE="non-cache variable is also replaced" 
NON_CACHE_VARIABLE=Default value of non-cache variable
STRING_CACHE_VARIABLE=Yet another value for STRING_CACHE_VARIABLE
BOOL_CACHE_VARIABLE=ON
-- Configuring done
-- Generating done
-- Build files have been written to: /home/vaddina/workspace/cmake-tests/cache-variable-demo/build
´´´
