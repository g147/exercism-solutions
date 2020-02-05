class Darts {

    private final double x;
	private final double y;
	
    Darts(double x, double y) {
    	this.x = x;
    	this.y = y;
    }

    int score() {
        double d = Math.sqrt( x * x + y * y );
        
        if (d <= 10 && d > 5) {
        	return 1;
        } else if (d <= 5 && d > 1) {
        	return 5;
        } else if (d <= 1) {
        	return 10;
        }
        
        return 0;
    }

}
