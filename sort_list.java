import java.util.List;
import java.util.Arrays;

class sorter {
  public static List<String> sort(List<String> textbooks) {
    // Given a list of strings, return the sorted list.
    
    // Test with a new list.
    // List<String> test = Arrays.asList("Hello", "World!", "How", "Are", "You");
    // test.sort(String.CASE_INSENSITIVE_ORDER);
    // System.out.println(test); 
    
    System.out.print("Original list: ");
    System.out.print(textbooks);
    System.out.print(System.lineSeparator());
    
    textbooks.sort(String.CASE_INSENSITIVE_ORDER);
    
    System.out.print("Sorted list: ");
    System.out.print(textbooks);
    System.out.print(System.lineSeparator());

    return textbooks;
  }
}
