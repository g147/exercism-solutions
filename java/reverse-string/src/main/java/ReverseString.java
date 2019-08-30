import java.util.*;
class ReverseString {
    String reverse(String inputString) {
        StringBuilder input = new StringBuilder(); 
        input.append(inputString); 
        input = input.reverse(); 
        return input.toString();
    }
  
}
