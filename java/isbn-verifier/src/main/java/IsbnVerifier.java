import java.util.*;
import java.util.regex.*;
class IsbnVerifier {

    boolean isValid(String stringToVerify) {
        List<String> allMatches = new ArrayList<String>();
        Matcher m = Pattern.compile("[0-9X]").matcher(stringToVerify);
        int r=0,a=10;
        while (m.find()) {
            allMatches.add(m.group());
        }
        if (allMatches.size() !=10)
            return false;
        for(int i = 0; i < allMatches.size(); i++) {   
            if (allMatches.get(i).equals("X"))
                r+=10;
            else
                r+=a*Integer.parseInt(allMatches.get(i));
            a-=1;
        }  
        return r%11==0;
    }

}
