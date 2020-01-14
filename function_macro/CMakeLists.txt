cmake_minimum_required(VERSION 3.5.1)
project(Hello-World)

function(PASS_VAR_NAMES n a)
  message("++++++++++ PASS_VAR_NAMES: Print by single de-referencing: " ${n} " " ${a})
  message("++++++++++ PASS_VAR_NAMES: Print by two de-referencing: " ${${n}} " " ${${a}} "\n")
endfunction()

function(PRINT_PARENT_SCOPE_VALUES)
  message("++++++++++ PRINT_PARENT_SCOPE_VALUES: Print parent scope values with single de-referencing: " ${Name} " " ${Age})
  message("++++++++++ PRINT_PARENT_SCOPE_VALUES: Print parent scope values by two de-referencing: " ${${Name}} " " ${${Age}} "\n")
endfunction()

function(FOO)
  message("++++++++++ FOO: Value of 'Age' before creating local function variable with same name: " ${Age})
  # Set a variable with name 'Age' in the function scope
  SET(Age 43)
  message("++++++++++ FOO: Creating a local function variable with name 'Age' and assigning value: " ${Age})
endfunction()

function(GOO a)
  SET(${a} 99 PARENT_SCOPE)
  message("++++++++++ GOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${Age})
endfunction()

function(HOO Age)
  SET(Age 99 PARENT_SCOPE)
  message("++++++++++ HOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${Age})
  message("++++++++++ HOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${${Age}}) # Note 'Age' is the value of the function 
endfunction()

function(JOO)
  SET(Age 55 PARENT_SCOPE)
  message("++++++++++ JOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${Age})
endfunction()

function(COMP_ADDR intro name address Age) 
  SET(${intro} ${${name}} " is " ${${Age}} "years old and lives at " ${${address}}  PARENT_SCOPE) 
endfunction() 

 
SET(Name "Tom")
SET(Age "UNDEFINED")

macro(Moo arg1)
endmacro()


PASS_VAR_NAMES(Name Age)
PASS_VAR_NAMES(${Name} ${Age})
PRINT_PARENT_SCOPE_VALUES()

FOO()
message("++++++++++ Value for 'Age' after FOO: " ${Age} "\n")
GOO(${Age})
message("++++++++++ Value for 'Age' after GOO: " ${Age} "\n")
HOO(${Age})
message("++++++++++ Value for 'Age' after HOO: " ${Age} "\n")
JOO(${Age})
message("++++++++++ Value for 'Age' after JOO: " ${Age} "\n")

SET(Address "One Nation str. 21, 13423, Mars")
SET(Comp "None")
COMP_ADDR(Comp Name Address Age)
message("++++++++++ " ${Comp} "\n")


add_executable(hello main.cpp)


