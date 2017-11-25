using System;
public class Kata
{
  public static bool Check(object[] a, object x)
  // Given an array, return true if an array from arg 1 contains the contents of arg 2
  {
    Console.WriteLine(x);
    Console.WriteLine("[{0}]", string.Join(", ", a));
    if (Array.IndexOf(a, x) > -1) {
      return true;
    }
    return false;
  }
}
