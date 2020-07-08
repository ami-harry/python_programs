import java.util.Scanner;

public class hello {

    public static void main(String[] args) {
        System.out.println("hello Harry");
        Scanner sk = new Scanner(System.in);
        System.out.println("Enter your name");
        String name = sk.nextLine();
        System.out.println("Your name is " + name);
        System.out.println(name);

    }
}
