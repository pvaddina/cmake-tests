cmake_minimum_required(VERSION 3.5.1)
project(Hello-World)

function(Foo age)
  message("########## Access variable from parent scope before it is even declared: " ${Name})
  set(age 43)
  message("########## Set the value for 'age' to: " ${age})
endfunction()

set(Name 'Tom')
set(age 'UNDEFINED')

macro(Moo arg1)
endmacro()

Foo(${age})
message("########## Value for 'age' after function call: " ${age})


set(Address 'One Nation str. 21, Mars')
add_executable(hello main.cpp)


