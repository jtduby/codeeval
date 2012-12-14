public class Pp {

	public static void main(String[] args) {
		int testVal = 10;
		int largest;
		largest = runTest(testVal);
		System.out.println(largest);
	}


	private static int runTest(int n) {
		int curr = 0;
		for(int i=0; i<n; i++) {
			if (isPrime(i) && isPalindrome(i)) {
				curr = i;
			}
		}
		return curr;
	}	

	private static boolean isPrime(int n) {
		return true;
	}

	private static boolean isPalindrome(int n) {
		return true;
	}

	private static int nextPalindrome(int n) {
		
	}

}
