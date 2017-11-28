using System;
using System.Collections.Generic;
using System.Linq;

public static class Filter
{
  public static IEnumerable<string> GooseFilter(IEnumerable<string> birds)
  {
    // return IEnumerable of string containing all of the strings in the input collection, except those that match strings in geese
    string[] geese = new string[] { "African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher" };
    List<string> list = new List<string>();
    
    foreach (string bird in birds){
      Console.WriteLine(bird);
      if (!geese.Contains(bird)) {
        // Console.WriteLine("NOT A GOOSE!!!");
        list.Add(bird);
      }
    }

    return list;
  }
}
