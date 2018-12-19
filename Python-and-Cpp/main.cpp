#include <stdlib.h>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
  if(argc > 1){
    cout << atoi(argv[1]);
    return atoi(argv[1]);
  }
  cout << -1;
  cout << "\nError: No value given!";
  return 0;
}
