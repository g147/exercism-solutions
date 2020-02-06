class Acronym {

    private String fform = "";

    Acronym(String phrase) {
        fform=phrase;
    }

    String get() {
        fform = fform.replaceAll("-", " ");
        fform = fform.replaceAll("\\p{Punct}", "");
        fform = fform.replaceAll("( )+", " ");
        String[] wordsArray = fform.split(" ");
        String shortForm = "";
        for(String words : wordsArray){
            shortForm+=Character.toString(words.charAt(0));
        }
        return shortForm.toUpperCase();
    }

}
