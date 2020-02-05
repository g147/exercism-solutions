class ResistorColorDuo {
    int value(String[] colors) {
        String result ="";
        for(int i=0; i<2;i++){
            int res = colorCode(colors[i]);
            if(res!=-1)
                result+=Integer.toString(res);
            else
                result+="";
        }
        return Integer.parseInt(result);
    }
    int colorCode(String color) {
        for (int i = 0; i < colors().length; i++) {
            if (colors()[i].equals(color)){
                return i;
            }
        }
        return -1;
    }
    String[] colors() {
        String[] arr = new String[] {"black","brown","red","orange","yellow","green","blue","violet","grey","white"};
        return arr;
    }
}
