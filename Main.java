import java.util.Scanner;

interface MeterBilling {
    double computeAmount(int consumedUnits);
}

class MeterBillCalculator implements MeterBilling {

    @Override
    public double computeAmount(int consumedUnits) {
        if (consumedUnits <= 100) {
            return consumedUnits * 1.0;
        }

        if (consumedUnits <= 300) {
            return 100 * 1.0 + (consumedUnits - 100) * 2.0;
        }

        return 100 * 1.0 + 200 * 2.0 + (consumedUnits - 300) * 5.0;
    }
}

public class Main {
    private static final double TAX_RATE = 0.05;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MeterBilling billing = new MeterBillCalculator();

        while (true) {
            System.out.println("\n*** Meter Billing System ***");
            System.out.print("Customer name (or 'exit' to quit): ");
            String customerName = scanner.nextLine().trim();

            if (customerName.equalsIgnoreCase("exit")) {
                System.out.println("Goodbye.");
                break;
            }

            int previousReading = readInteger(scanner, "Previous meter reading: ");
            int currentReading = readInteger(scanner, "Current meter reading: ");

            if (currentReading < previousReading) {
                System.out.println("Invalid input: current reading must be greater than or equal to previous reading.");
                continue;
            }

            int unitsUsed = currentReading - previousReading;
            double baseAmount = billing.computeAmount(unitsUsed);
            double tax = baseAmount * TAX_RATE;
            double totalDue = baseAmount + tax;

            printReceipt(customerName, unitsUsed, baseAmount, tax, totalDue);
        }

        scanner.close();
    }

    private static int readInteger(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            if (scanner.hasNextInt()) {
                int value = scanner.nextInt();
                scanner.nextLine();
                return value;
            }
            System.out.println("Please enter a valid whole number.");
            scanner.nextLine();
        }
    }

    private static void printReceipt(String customer, int units, double baseAmount, double tax, double total) {
        System.out.println("\n--- Meter Bill Summary ---");
        System.out.println("Customer: " + customer);
        System.out.println("Units consumed: " + units);
        System.out.printf("Base amount: Rs.%.2f%n", baseAmount);
        System.out.printf("Tax (5%%): Rs.%.2f%n", tax);
        System.out.printf("Total due: Rs.%.2f%n", total);
        System.out.println("-----------------------------");
    }
}
