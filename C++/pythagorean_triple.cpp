#include <stdio.h>
#include <math.h>
using namespace std;
vector<int> sides;  

int bigger (int x, int y)
{
  if (x > y) {
    // cout << "return " << x << " \n";
    sides.push_back(y);
    return x;
  } else {
    // cout << "return " << y << "\n";
    sides.push_back(x);
    return y;
  }
}

bool PythagoreanTriple(const int a, const int b, const int c)
{
  cout << a << ", " << b << ", " << c << "\n";
  // cout << a + b + c << "\n"; 
  // cout << pow(a, 2) + pow(b, 2) + pow(c, 2) << "\n";
  
  // Get the largest argument  
  int l = bigger(bigger(a, b), c);
  cout << "Longest side: " << l << "\n";
  cout << "Other sides: " << sides[0] << ", " << sides[1] << "\n";  
  cout << pow(sides[0], 2) << " + " << pow(sides[1], 2) << " = " << pow(l, 2) << "?\n";
  
  if (pow(sides[0], 2) + pow(sides[1], 2) == pow(l, 2)) {
    cout << "TRUE\n";
    cout << "Erasing Sides: " << sides[0] << ", " << sides[1] << "\n";
    sides.erase(sides.begin());
    sides.erase(sides.begin());
    cout << "Are they gone?: " << sides[0] << ", " << sides[1] << "\n\n";
    return true;
  } else {
    cout << "FALSE\n";
    cout << "Erasing Sides: " << sides[0] << ", " << sides[1] << "\n";
    sides.erase(sides.begin());
    sides.erase(sides.begin());
    cout << "Are they gone?: " << sides[0] << ", " << sides[1] << "\n\n";
    return false;
  }
  
}
