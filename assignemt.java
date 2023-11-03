import java.util.*;

public class Powers {
    public static int powerIterative(int baseValue, int exponentValue) {
        int sum = 1;
        for (int i = 0; i < exponentValue; i++) {
            total *= baseValue;
        }
        return total;
    }

    public static int PowerDivideConquer(int baseValue, int exponentValue) {
        if (exponentValue == 0) {
            return 1;
        }
        if (exponentValue < 0) {
            return 0;
        } else if (exponentValue % 2 == 0) {
            long halfPower = calculatePowerDivideConquer(baseValue, exponentValue / 2);
            return halfPower * halfPower;
        } else {
            long halfPower = calculatePowerDivideConquer(baseValue, (exponentValue - 1) / 2);
            return baseValue * halfPower * halfPower;
        }

    }

    public static void findPairsWithSum(int[] S, int targetSum) {
        Arrays.sort(S); // Sort the array to enable efficient pair search
        int[] leftArray = new int[S.length];
        int[] rightArray = new int[S.length];
        int leftSize = 0;
        int rightSize = 0;

        int left = 0, right = S.length - 1;

        while (left < right) {
            int currentSum = S[left] + S[right];

            if (currentSum == targetSum) {
                leftArray[leftSize] = S[left]; // Add left element to the left array
                rightArray[rightSize] = S[right]; // Add right element to the right array
                leftSize++;
                rightSize++;
                left++;
                right--;
            } else if (currentSum < targetSum) {
                left++;
            } else {
                right--;
            }
        }

        printPairs(leftArray, rightArray, leftSize, targetSum); // Print the pairs
    }

    private static void printPairs(int[] leftArray, int[] rightArray, int size, int targetSum) {
        for (int i = 0; i < size; i++) {
            int leftValue = leftArray[i]; // Get the left element
            int rightValue = rightArray[i]; // Get the right element
            System.out.println(leftValue + " + " + rightValue + " = " + targetSum);
        }
    }

    private static void findAndPrintPairs(int[] S, int targetSum) {
        Arrays.sort(S); // Sort the array to enable efficient pair search
        int[] leftArray = new int[S.length];
        int[] rightArray = new int[S.length];
        int leftSize = 0;
        int rightSize = 0;

        int left = 0, right = S.length - 1;

        while (left < right) {
            int currentSum = S[left] + S[right];

            if (currentSum == targetSum) {
                leftArray[leftSize] = S[left]; // Add left element to the left array
                rightArray[rightSize] = S[right]; // Add right element to the right array
                leftSize++;
                rightSize++;
                left++;
                right--;
            } else if (currentSum < targetSum) {
                left++;
            } else {
                right--;
            }
        }

        printPairs(leftArray, rightArray, leftSize, targetSum); // Print the pairs
    }

    public static void main(String[] args) {
        long stime = System.currentTimeMillis();

        long n = 1;
        int x = 5;
        long result = powerDivideConquer(n, x);
        long etime = System.currentTimeMillis();
        System.out.println(etime - stime);
    }
}