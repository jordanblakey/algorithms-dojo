using System;

public static class Kata
{
  public static bool IsDivisible(int wallLength, int pixelSize)
  // Given two integers, return true if the first is divisible by the second.
  {   
    Console.WriteLine(wallLength);
    Console.WriteLine(pixelSize);
    if (wallLength % pixelSize == 0){
      return true;
    }    
    return false;
  }
}
