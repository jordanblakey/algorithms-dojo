using System;
using System.Linq;
using System.Collections.Generic;

public class Kata
{
  public static void PrintArray(string x, int[] y){
    // Given two lists of integers, square the elements in the first and cube the elements in the second.
    // If the sum of the first list > sum of the second, return true. Else, return false.
    
    Console.WriteLine("{0}: {1}", x, string.Join(",", y));
  }

  public static bool ArrayMadness(int[] a, int[] b)
  {
    List<int> aList = new List<int>();
    List<int> bList = new List<int>();

    PrintArray("Original a:", a);
    foreach (int x in a) {
      aList.Add(x * x);
      Console.WriteLine(x * x);
    }
    PrintArray("Squared a:", a);
    int aListSum = aList.Sum(x => Convert.ToInt32(x));
    Console.WriteLine("{0}: {1}", "Sum of squared a list:", aListSum);
    
    PrintArray("Original b:", b);
    foreach (int x in b) {
      bList.Add(x * x * x);
      Console.WriteLine(x * x * x);
    }
    PrintArray("Cubed b:", b);
    int bListSum = bList.Sum(x => Convert.ToInt32(x));
    Console.WriteLine("{0}: {1}", "Sum of cubed b list:", bListSum);

    if (aListSum > bListSum) {return true;}
    else {return false;}
  }
}
