import java.util.Scanner; // imports a class
// import java.util* imports the whole package

public class JavaClass {
    // class attributes
    final int classNumber = 1; // cannot be changed
    int objectNumber; // can be changed
    private String passcode;

    // class constructor
    public JavaClass(int newObjectNumber) {
        objectNumber = newObjectNumber;
    }

    // without a set, read-only
    public String getPasscode() {
        return passcode;
    }

    // without a get, write-only
    public void setPasscode(String newPasscode) {
        this.passcode = newPasscode;
    }

    static void staticMethod() {
        return;
    }

    public void publicMethod() {
        return;
    }

    public static void main(String[] args) {
        JavaClass object1 = new JavaClass(1);
        JavaClass object2 = new JavaClass(2);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter passcode: ");
        String newPasscode = scanner.nextLine();
        object1.setPasscode(newPasscode);
        System.out.println(object1.getPasscode());

        staticMethod(); // can be called without an object
        object1.publicMethod(); // can only be called with an object
    }
}