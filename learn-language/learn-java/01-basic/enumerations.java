import java.util.Scanner;

class Bool {
    enum bool{ Y, N }
}

public class enumerations  {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Is your age 18+: ");
        String input = sc.next(); // read user input

        Bool.bool ans = Bool.bool.valueOf(input.toUpperCase());
        System.out.println("Your ans: " + ans);
    }
}
