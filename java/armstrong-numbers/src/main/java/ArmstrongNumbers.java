class ArmstrongNumbers {

	boolean isArmstrongNumber(int number) {
		String [] arr = Integer.toString(number).split("");
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += Math.pow(Integer.parseInt(arr[i]), arr.length);
		}
		return sum == number;
	}

}
