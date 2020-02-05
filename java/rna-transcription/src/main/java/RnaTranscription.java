class RnaTranscription {
    String transcribe(String dnaStrand) {
        StringBuilder a = new StringBuilder();
	    for (char i: dnaStrand.toCharArray())
	        a.append((i=='G')? 'C': (i=='C')? 'G': (i=='T')? 'A': 'U');
    	return a.toString();
    }
}
