import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

// every application begins with a class that matches the file name
public class JavaBasics {
    public static void myMethod() {
        System.out.println("myMethod has been executed");
    }

    /*
    recursion is the devil's work
    this method adds all of the numbers from k to 0
    e.g., if k was 10
    it would start with 10 > 0 therefore return 10 + recursion(9)
    since the method is called within the method
    the initial call is halted and the new call is actioned
    so 9 > 0 therefore returning 9 + recursion(8)
    this continues all the way until k = 0
    0 > 0 is not true therefore the if moves to the else and returns 0
    the recursion has finally ended
    now each halted call gets picked up again to do
    10 + (9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + (1 + (0))))))))))
    */
    public static int recursion(int k) {
        if (k > 0) {
            return k + recursion(k - 1);
        } else {
            return 0;
        }
    }
    /* 
    every class must contain a main method
    the code within the main method will be executed 
    */
    public static void main(String[] args) {
        System.out.print("Hello World!"); // no new line at the end
        System.out.println("Hello World!"); // new line at the end

        String stringVar = "Dog";
        int integerVar = 5;
        float floatVar = 5.55f;
        char characterVar = 'A';
        boolean booleanVar = false;

        String dog1 = "Golden Retriever";
        String dog2 = "Chocolate Labrador";
        String dogs = dog1 + ", " + dog2;
        System.out.println(dog1.length()); // outputs 16
        // finds the first index of the specified string
        System.out.println(dog2.indexOf("Labrador")); // outputs 10

        int num1 = 3;
        int num2 = 6;
        int num3 = num1 + num2;
        double dbl1 = num1; // outputs 3.0

        String firstName = "Lucy";
        String lastName = "Williams";
        String fullName = firstName.concat(lastName); // outputs LucyWilliams

        String escapeQuote = "I love the TV series \"The Office\".";

        int x = 2;
        int y = 4;
        System.out.println(Math.max(x, y)); // outputs 4
        System.out.println(Math.min(x, y)); // outputs 2
        System.out.println(Math.sqrt(y)); // outputs 2
        System.out.println(Math.abs(-x)); // outputs 2
        System.out.println(Math.random()); // returns a random number such that 0.0 <= x < 1.0
        System.out.println((int)(Math.random() * 100)); // returns a random number such that 0 <= x < 100
        System.out.println(x < y); // outputs true

        int age = 15;
        int votingAge = 18;
        if (age > 100 || age < 0) {
            System.out.println("Invalid age");
        } else if (age >= votingAge) {
            System.out.println("Allowed to vote");
        } else {
            System.out.println("Not allowed to vote");
        }

        int time = 18;
        // if time < 12 then "Good Morning!" else "Good Evening!"
        String greeting = (time < 12) ? "Good Morning!" : "Good Evening!";

        String option = "Settings";
        switch(option) {
            case "Start":
                System.out.println("Starting game.");
                break;
            case "Settings":
                System.out.println("Entering settings.");
                break;
            case "Exit":
                System.out.println("Exiting game.");
                break;
            default:
                System.out.println("Please select an option.");
        }

        while (time < 24) {
            System.out.println("The day is not over yet.");
            time++;
        }
        System.out.println("A new day has begun.");

        int currentAge = -1;
        do {
            currentAge++;
            System.out.println("You are not old enough to vote yet.");
        } 
        while (currentAge < 18);

        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        String[] register = {"Courtney", "Ellie", "Alex", "Henry"};
        for (String student : register) {
            if (student == "Courtney") {
                continue; // continue onto the next iteration without executing the following code
            }
            System.out.println(student);
            if (student == "Alex") {
                break; // break out of the for loop
            }
        }

        int[][] numbers = {{1, 2, 3, 4}, {5, 6, 7}};

        myMethod(); // calls myMethod at the top

        ArrayList<String> animals = new ArrayList<String>();
        animals.add("Monkey");
        animals.add("Snake");
        animals.add("Donkey");
        Collections.sort(animals); // sorts String alphabetically and numbers ascending
        animals.size(); // outputs 3
        animals.get(0); // outputs Monkey
        animals.set(0, "Gorilla");
        animals.remove(0);
        animals.clear();

        HashMap<String, Integer> students = new HashMap<String, Integer>();
        students.put("Millie Bobby Brown", 10); // (key, value)
        students.put("Noah Schnapp", 9);
        students.put("Finn Wolfard", 12);
        System.out.println(students.get("Noah Schnapp")); // outputs 9
        for (String key : students.keySet()) {
            System.out.println(key);
        }
        for (int value : students.values()) {
            System.out.println(value);
        }  

        HashSet<String> vehicles = new HashSet<String>();
        vehicles.add("car");
        vehicles.add("truck");
        vehicles.add("car"); // not added, hashsets don't contain duplicates
        vehicles.add("motorbike");
        System.out.println(vehicles.contains("motorbike")); // outputs true

        /*
        iterator vs for loop
        when removing multiple items from a collection 
        the collection is changing size with each iteration
        a for loop fails to account for this 
        whereas an iterator does
        */
        ArrayList<Integer> numberList = new ArrayList<Integer>();
        numberList.add(17);
        numberList.add(23);
        numberList.add(9);
        numberList.add(11);
        numberList.add(28);
        Iterator<Integer> numberIterator = numberList.iterator();
        while (numberIterator.hasNext()) {
            if (numberIterator.next() < 20) {
                numberIterator.remove();
            }
        }

        try {
            // try block of code
            int[] abc = {1, 2, 3};
            System.out.println(abc[3]); // there is no index 3 in abc
        } catch(Exception e) {
            // catch and handle errors
            System.out.println("Something went wrong.");
        } finally {
            System.out.println("The try catch is finished.");
        }
    }
}