public class Counter {
  public int countSheeps(Boolean[] arr) {
    // For an array of booleans, count the # of elements that are true.
    // System.out.println(arr.length);
    int count = 0;
    int place = 500;
    int i = 0;
    for(i = 0; i < arr.length; i++) {
      if (arr[i] == null) {
        // System.out.printf("arr.length: %d \n", arr.length);
        // System.out.printf("i: %d \n", i);
        // System.out.printf("arr[i]: %b \n", arr[i]);
        // System.out.printf("DEBUG NULL POINTER");
      }
      if (arr[i] != null && arr[i] == true) {
        count ++;
        // System.out.printf("Count: %d ", count);
      }
      if (i == arr.length) {return count;}
      if (i+1 == 500) {
        System.out.printf("Limit reached.");
        break;
      }
    }
    return count;
  }
}
