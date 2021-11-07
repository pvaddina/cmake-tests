#include <iostream>
#include "arithmetic_op.h"

int main()
{
  const int one = 100;
  const int two = 5;

  ArithmeticOperations op;

  std::cout << one << "+" << two << " = " << op.AddTwoNumbers(one, two) << std::endl;
  std::cout << one << "-" << two << " = " << op.SubtractTwoNumbers(one, two) << std::endl;
  std::cout << one << "x" << two << " = " << op.MultiplyTwoNumbers(one, two) << std::endl;
  std::cout << one << "/" << two << " = " << op.DivideTwoNumbers(one, two) << std::endl;

  return 0;
}


