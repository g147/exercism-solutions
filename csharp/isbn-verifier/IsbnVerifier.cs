using System;
using System.Linq;
using System.Text.RegularExpressions;
public static class IsbnVerifier{
    public static bool IsValid(string num){
        num = num.Replace("-", "");
        return Regex.IsMatch(num, @"^\d{9}[\dX]$") && num.Reverse().Select((x, u) => (x == 'X' ? 10 : x - '0') * (u + 1)).Sum() % 11 == 0;
    }   
}