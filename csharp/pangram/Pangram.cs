using System;
public static class Pangram{
    public static bool IsPangram(string input){
        input=input.ToLower();
        string a = "abcdefghijklmnopqrstuvwxyz";
        char[] aa = a.ToCharArray();
        for(int i=0; i<aa.Length; i++){
            if(input.Contains(aa[i])==false){
                return false;
            }
        }
        return true;
    }
}
