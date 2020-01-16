cmake_minimum_required(VERSION 3.5.1)
project(Hello-World)

##########################################################################################################
## FUNCTIONS
##########################################################################################################
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
  message("++++++++++ GOO: Name of a=" ${a})
  message("++++++++++ GOO: Value of a=" ${${a}})
  SET(${a} 99 PARENT_SCOPE) # Note: ${a}=Age. Therefore this is pretty much like creaing a new variable in the Parent scope
  message("++++++++++ GOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${Age})
endfunction()

function(JOO Age)
  message("++++++++++ JOO: " ${Age})
  message("++++++++++ JOO: " ${${Age}})   # Why is this also 'Age' ?
  SET(Age 55 PARENT_SCOPE)
  message("++++++++++ JOO: Set value for variable 'Age' in the PARENT_SCOPE to: " ${Age})
endfunction()


function(COMP_ADDR intro name address a) 
  message("++++++++++ COMP_ADDR: " ${Age})
  message("++++++++++ COMP_ADDR: " ${${Age}})
  SET(${intro} ${${name}} " is " ${${a}} "years old and lives at " ${${address}}  PARENT_SCOPE) 
endfunction() 

function(DEMO_DEFAULT_ARGS)
  foreach(arg ${ARGV})
    message("1.arg=" ${arg})
  endforeach()

  foreach(arg IN LISTS ${ARGV})
    message("2.arg=" ${arg})
  endforeach()

  if(ARGV4)
    message("Fourth argment=" ${ARGV4})
  endif()
endfunction()


##########################################################################################################
## MACROS
##########################################################################################################
macro(MAC_CREATE_A)
  SET(A 111111)
endmacro()

macro(MAC_CREATE_B)
  SET(B 222222)
endmacro()

 
##########################################################################################################
## FUNCTION tests
##########################################################################################################
SET(Name "Tom")
SET(Age "UNDEFINED")

macro(Moo arg1)
endmacro()


PASS_VAR_NAMES(Name Age)
PASS_VAR_NAMES(${Name} ${Age})
PRINT_PARENT_SCOPE_VALUES()

FOO()
message("++++++++++ Value for 'Age' after FOO: " ${Age} "\n")
GOO(Age)
message("++++++++++ Value for 'Age' after GOO: " ${Age} "\n")
JOO(Age)
message("++++++++++ Value for 'Age' after JOO: " ${Age} "\n")

SET(Address "One Nation str. 21, 13423, Mars")
SET(Comp "None")
COMP_ADDR(Comp Name Address Age)
message("++++++++++ " ${Comp} ". Age=" ${Age} "\n")

DEMO_DEFAULT_ARGS(1 2 3 "Four" "Five" 6 7)

##########################################################################################################
## MACROS tests
##########################################################################################################
message("")
message("++++++++++ Value A=" ${A} " before the call to the Macro")
message("++++++++++ Value B=" ${B} " before the call to the Macro")
MAC_CREATE_A()
MAC_CREATE_B()
message("++++++++++ Value A=" ${A} " after the call to the Macro")
message("++++++++++ Value B=" ${B} " after the call to the Macro")


add_executable(hello main.cpp)


