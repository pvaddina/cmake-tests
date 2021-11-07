#include "arithmetic_op.h"

#include "add.h"
#include "sub.h"
#include "mul.h"
#include "div.h"

int ArithmeticOperations::AddTwoNumbers(const int iOne, const int iTwo)
{
  return add(iOne,iTwo);
}

int ArithmeticOperations::SubtractTwoNumbers(const int iOne, const int iTwo)
{
  return sub(iOne,iTwo);
}

int ArithmeticOperations::MultiplyTwoNumbers(const int iOne, const int iTwo)
{
  return mul(iOne,iTwo);
}

int ArithmeticOperations::DivideTwoNumbers(const int iOne, const int iTwo)
{
  return div(iOne,iTwo);
}

