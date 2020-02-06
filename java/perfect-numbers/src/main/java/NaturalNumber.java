public class NaturalNumber {
	private Classification classification;

	public NaturalNumber(int n) {
		if (n <= 0) {
			throw new IllegalArgumentException("You must supply a natural number (positive integer)");
		}
		int sum = 1;
		for (int i = 2; i <= Math.sqrt(n); i++) {
			if (n % i == 0) {
				sum += i;
                if (i != n/i) 
                    sum += n/i;
			}
		}
		if (sum == 1 || sum < n) {
			classification = Classification.DEFICIENT;
		} else if (sum > n) {
			classification = Classification.ABUNDANT;
		} else {
			classification = Classification.PERFECT;
		}
	}

	public Classification getClassification() {
		return classification;
	}
}