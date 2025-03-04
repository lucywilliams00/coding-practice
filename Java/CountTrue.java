/*
 * create a function which returns the number of true values there are in an array
 * e.g.
 * countTrue([true, false, false, true, false]) --> 2
 * countTrue([false, false, false, false]) --> 0
 * countTrue([]) --> 0
 */

public class CountTrue {
    public static int countTrue(boolean[] arr) {
        int count = 0;
        for (boolean item : arr) {
            if (item == true) {
                count += 1;
            }
        }
        return count;
    }
}
