#include <fmt/format.h>
#include <string>

int main() {
  std::string message = fmt::format("Hello, {}!", "World");
  fmt::print("{}\n", message);
  return 0;
}
