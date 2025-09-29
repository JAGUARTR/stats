import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Taking input from the user
        System.out.print("Enter the first and the second number: ");
        int a = sc.nextInt();
        int b = sc.nextInt();

        // Selecting the operand for the calculations
        System.out.print("Choose and Enter the type of operation you want to perform (+, -, *, /, %): ");
        char op = sc.next().charAt(0);

        solve(a, b, op);
        sc.close();
    }

    private static int solve(int a, int b, char op) {
        int ans = 0;

        // Addition
        if (op == '+') {
            ans = a + b;
        }
        // Subtraction
        else if (op == '-') {
            ans = a - b;
        }
        // Multiplication
        else if (op == '*') {
            ans = a * b;
        }
        // Division
        else if (op == '/') {
            ans = a / b;
        }
        // Modulus
        else if (op == '%') {
            ans = a % b;
        }

        // Printing the final result
        System.out.println("Your answer is: " + ans);
        return ans;
    }
}
