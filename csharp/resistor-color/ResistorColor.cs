using System;
public static class ResistorColor{
    public static int ColorCode(string color){
        String[] a = new String[10];
        a = Colors();
        int pos = Array.IndexOf(a, color);
        return pos;
    }

    public static string[] Colors(){
        String[] arr = new String[] {"black","brown","red","orange","yellow","green","blue","violet","grey","white"};
        return arr;
    }
}