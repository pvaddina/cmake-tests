#include <iostream>
#include "add.h"
#include "mul.h"

int main()
{
  const int one = 20;
  const int two = 5;
  std::cout << one << "+" << two << " = " << add(one,two) << std::endl;
  std::cout << one << "x" << two << " = " << mul(one,two) << std::endl;

  return 0;
}


