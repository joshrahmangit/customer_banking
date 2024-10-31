from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """Main function to interact with the user and display the account information."""
    # Prompt the user for savings account details
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the annual percentage rate (APR) for savings: "))
    savings_months = int(input("Enter the number of months: "))

    # Call the create_savings_account function
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Display the results for the savings account
    print(f"Savings Account: Interest Earned: ${savings_interest_earned:.2f}, Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user for CD account details
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the annual percentage rate (APR) for the CD: "))
    cd_maturity = int(input("Enter the number of months: "))

    # Call the create_cd_account function
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Display the results for the CD account
    print(f"CD Account: Interest Earned: ${cd_interest_earned:.2f}, Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
