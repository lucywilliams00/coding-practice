import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// this is a better example of a class
public class TVRatings {
    public String title;
    public int seasons;
    public List<Float> ratings;
    public static String[] critics = {"Mary", "Andrew", "Brennan", "Ally", "Phoebe"};

    public TVRatings(String title, int seasons, List<Float> ratings) {
        this.title = title;
        this.seasons = seasons;
        this.ratings = ratings;
    }

    public static List<Float> getRatings() {
        List<Float> ratings = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);
        for (String critic: critics) {
            System.out.print("Enter " + critic + "'s rating: ");
            float rating = scanner.nextFloat();

            while (!validRating(rating)) {
                System.out.print("Rating must be between 0 and 10 inclusive. Enter " + critic + "'s rating: ");
                rating = scanner.nextFloat();
            }

            ratings.add(rating);
        }

        return ratings;
    }

    public static boolean validRating(float rating) {
        if (rating < 0 || rating > 10) {
            return false;
        } else {
            return true;
        }
        // this if statement can be simplified to the following
        // return !(rating < 0) && !(rating > 10);
    }

    public static float getAverage(List<Float> ratings) {
        float total = 0;
        for (float rating: ratings) {
            total = total + rating;
        }
        return total / ratings.size();
    }

    public static void main(String[] args) {
        TVRatings TVD = new TVRatings("The Vampire Diaries", 8, getRatings());
        System.out.println("The series " + TVD.title + " after " + TVD.seasons +
                " seasons has an average rating of " + getAverage(TVD.ratings));
    }
}
