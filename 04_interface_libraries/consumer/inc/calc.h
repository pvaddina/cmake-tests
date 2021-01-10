#pragma once

class Calculator
{
  public:
    Calculator(const int a, const int b) : arg1(a), arg2(b) {}
    void Add();
    void Multiply();
  private:
    int arg1;
    int arg2;
};



