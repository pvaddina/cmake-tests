#include <iostream>
#include "calc.h"

int main()
{
  const int one = 20;
  const int two = 5;
  Calculator c{one, two};

  c.Add();
  c.Multiply();

  return 0;
}


