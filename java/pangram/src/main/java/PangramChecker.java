public class PangramChecker {

    public boolean isPangram(String input) {
        input = input.toLowerCase();
        String letters = "abcdefghijklmnopqrstuvwxyz";
        char[] lettersArray = letters.toCharArray();
        for (char a: lettersArray){
            if(input.contains(Character.toString(a))==false)
                return false;
        }
        return true;
    }

}
