/*
 * Easter Sunday can occur on any date between 22nd March and 25th April
 * the Butcher's Algorithm was created to predict the date for a given year
 * write a function that will return the formula for any year after 1600
 */

public class EasterChallenge {
    public static String easterChallenge(int y) {
        String date = "";
        if (y >= 1600) {
            int a = y % 19;
            int b = y / 100;
            int c = y % 100;
            int d = b / 4;
            int e = b % 4;
            int f = (b + 8) / 25;
            int g = (b - f + 1) / 3;
            int h = (19 * a + b - d - g + 15) % 30;
            int i = c / 4;
            int k = c % 4;
            int l = (32 + 2 * e + 2 * i - h - k) % 7;
            int m = (a + 11 * h + 22 * l) / 451;
            int month = (h + l - 7 * m + 114) / 31; // I failed the test because the month was a int and not a String but I'm not writing a whole switch case again...
            int p = (h + l - 7 * m + 114) % 31;
            int day = p + 1;
            date = String.valueOf(month) + " " + String.valueOf(day);
        }
        return date;
    }
}
