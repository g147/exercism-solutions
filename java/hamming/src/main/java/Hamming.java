class Hamming {

    private String leftStrand;
    private String rightStrand;

    Hamming(String leftStrand, String rightStrand) {
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
        if(rightStrand.length() ==0 && leftStrand.length() !=0 ){
            throw new IllegalArgumentException("right strand must not be empty.");
        }
        if(leftStrand.length() ==0 && rightStrand.length() !=0 ){
            throw new IllegalArgumentException("left strand must not be empty.");
        }
        if(rightStrand.length() != leftStrand.length()){
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }
    }

    int getHammingDistance() {
        int distance = 0;
        for(int i=0;i<leftStrand.length();i++){
          if(leftStrand.charAt(i) != rightStrand.charAt(i)){
            distance++;
          }
        }
        return distance;
    }
}
