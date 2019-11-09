using System;
using System.Text.RegularExpressions;
using System.Collections;
public static class IsbnVerifier{
    public static bool IsValid(string number){
        ArrayList allMatches = new ArrayList();
        Match m = Regex.Match(number, "[0-9X]");
        int r=0,a=10;
        while (m.Success) {
            allMatches.Add(m.Value);
        }
        if (allMatches.Count !=10)
            return false;
        for(int i = 0; i < allMatches.Count; i++) {   
            if ((string)allMatches[i]=="X")
                r+=10;
            else
                r+=a*Int32.Parse((string)allMatches[i]);
            a-=1;
        }  
        return r%11==0;
    }
}