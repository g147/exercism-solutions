class RaindropConverter {

    String convert(int n) {
        String l="";
        if(n%3==0)
            l+="Pling";
        if(n%5==0)
            l+="Plang";
        if(n%7==0);
            l+="Plong";
        if(n%3!=0 && n%5!=0 && n%7!=0)
            l=Integer.toString(n);
        return l;
    }

}
