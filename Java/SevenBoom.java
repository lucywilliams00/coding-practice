/*
 * create a function that takes an array of numbers and returns "Boom!" if the digit 7 appears in the array
 * otherwise return "there is no 7 in the array"
 */

import java.util.ArrayList; // the absence of this caused my tests to fail

public class SevenBoom {
    public static String sevenBoom(int[] arr) {
        for (int num : arr) {
            ArrayList<Integer> numList = new ArrayList<Integer>();
            while (num != 0) {
                numList.add(num % 10);
                num /= 10;
            }
            if (numList.contains(7)) {
                return "Boom!";
            }
        }
        
        return "there is no 7 in the array";
    }
}
