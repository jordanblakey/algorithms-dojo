using System;
using System.Linq;

public static class Kata
{
  public static bool PanForGold(string[] bucket)
  // Given an array of strings, return true if it contains string "gold".
  {
    Console.WriteLine(string.Join(",", bucket));
    if (bucket.Contains("gold")){
      return true;
    }
    return false;    
  }
}
