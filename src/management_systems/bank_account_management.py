"""
Bank Account Management System

This module uses lists, sets, tuples, and dictionaries to manage bank account data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

Data Structures:

1. Lists: To store collections of accounts and transactions.
2. Tuples: To store immutable account details.
3. Sets: To manage unique account types and transaction types.
4. Dictionaries: To map account numbers to their details and manage account balances.

List of accounts with details (Account Number, Account Holder, Balance, Account Type):
accounts = [
    (1001, "Alice", 5000.0, "Savings"),
    (1002, "Bob", 3000.0, "Checking"),
    (1003, "Charlie", 7000.0, "Savings"),
    (1004, "Diana", 10000.0, "Checking"),
    (1005, "Eve", 15000.0, "Savings")
]

List of transactions (Transaction ID, Account Number, Amount, Transaction Type):
transactions = [
    (1, 1001, 500.0, "Deposit"),
    (2, 1002, 200.0, "Withdrawal"),
    (3, 1003, 1000.0, "Deposit"),
    (4, 1004, 500.0, "Withdrawal"),
    (5, 1005, 2000.0, "Deposit")
]

Set of unique account types:
account_types = set()

Adding account types from accounts:
for account in accounts:
    account_types.add(account[3])

Set of unique transaction types:
transaction_types = set()

Adding transaction types from transactions:
for transaction in transactions:
    transaction_types.add(transaction[3])

Dictionary to map account numbers to their details:
account_catalog = {acc[0]: acc for acc in accounts}

Dictionary to manage account balances:
account_balances = {acc[0]: acc[2] for acc in accounts}

Functions:

List-Related Methods:
1. find_account_index(account_number): Finds the index of an account in the list.
2. sort_accounts_by_balance(): Sorts accounts by balance.
3. reverse_transactions(): Reverses the list of transactions.
4. append_transaction(transaction): Appends a new transaction to the list.
5. remove_transaction(transaction_id): Removes a transaction from the list.

Tuple-Related Methods:
1. find_max_min_balance(): Finds the maximum and minimum balance of accounts.
2. count_account_type_occurrences(account_type): Counts the occurrences of a specific account type.

Set-Related Methods:
1. add_account_type(account_type): Adds a new account type.
2. remove_account_type(account_type): Removes an account type.
3. list_all_account_types(): Lists all account types.
4. add_transaction_type(transaction_type): Adds a new transaction type.
5. remove_transaction_type(transaction_type): Removes a transaction type.
6. list_all_transaction_types(): Lists all transaction types.
7. find_common_account_types(other_account_types): Finds common account types between two sets.
8. find_unique_account_types(): Finds unique account types in the bank.
9. clear_account_types(): Clears all account types.

Dictionary-Related Methods:
1. add_account(account_number, account_holder, balance, account_type): Adds a new account to the bank.
2. remove_account(account_number): Removes an account from the bank.
3. get_account_details(account_number): Gets account details.
4. list_accounts_by_type(account_type): Lists all accounts by account type.
5. count_accounts_by_type(account_type): Counts accounts by account type.
6. update_account_details(account_number, new_details): Updates account details.
7. merge_account_catalogs(other_catalog): Merges two account catalogs.
8. get_all_account_numbers(): Gets all account numbers.
9. clear_account_catalog(): Clears the account catalog.

Example usage:
if __name__ == "__main__":
    print("Account Catalog:")
    for acc_number, details in account_catalog.items():
        print(f"{acc_number}: {details}")

    print("\nAccount Types Available:")
    print(account_types)

    print("\nTransaction Types Available:")
    print(transaction_types)

    print("\nAccount Balances:")
    for acc_number, balance in account_balances.items():
        print(f"{acc_number}: {balance}")

    # Add and remove accounts
    add_account(1006, "Frank", 2000.0, "Checking")
    remove_account(1003)

    print("\nAccount Catalog After Changes:")
    for acc_number, details in account_catalog.items():
        print(f"{acc_number}: {details}")

    # Get account details
    print("\nAccount Details for Account Number 1002:")
    print(get_account_details(1002))

    # List accounts by type
    print("\nAccounts of Type 'Savings':")
    print(list_accounts_by_type("Savings"))

    # Count accounts by type
    print("\nCount of Accounts of Type 'Checking':")
    print(count_accounts_by_type("Checking"))

    # Find account index
    print("\nIndex of Account Number 1002:")
    print(find_account_index(1002))

    # Add and remove account types
    add_account_type("Business")
    remove_account_type("Savings")

    # List all account types
    print("\nAll Account Types:")
    print(list_all_account_types())

    # Add and remove transaction types
    add_transaction_type("Transfer")
    remove_transaction_type("Withdrawal")

    # List all transaction types
    print("\nAll Transaction Types:")
    print(list_all_transaction_types())

    # Append and remove transactions
    append_transaction((6, 1001, 300.0, "Deposit"))
    remove_transaction(2)

    print("\nTransactions After Changes:")
    for transaction in transactions:
        print(transaction)

    # Sort accounts by balance
    print("\nAccounts Sorted by Balance:")
    for acc in sort_accounts_by_balance():
        print(acc)

    # Reverse the list of transactions
    print("\nReversed List of Transactions:")
    print(reverse_transactions())

    # Find the maximum and minimum balance of accounts
    max_balance, min_balance = find_max_min_balance()
    print(f"\nMaximum Balance: {max_balance}, Minimum Balance: {min_balance}")

    # Count the occurrences of a specific account type
    print(f"\nOccurrences of 'Checking': {count_account_type_occurrences('Checking')}")

    # Find common account types between two sets
    other_account_types = {"Savings", "Business", "Investment"}
    print(f"\nCommon Account Types: {find_common_account_types(other_account_types)}")

    # Find unique account types in the bank
    print(f"\nUnique Account Types: {find_unique_account_types()}")

    # Update account details
    update_account_details(1002, (1002, "Bob", 3500.0, "Checking"))
    print(f"\nUpdated Account Details for Account Number 1002: {get_account_details(1002)}")

    # Merge two account catalogs
    other_catalog = {
        1007: (1007, "Grace", 4000.0, "Savings"),
        1008: (1008, "Hank", 5000.0, "Checking")
    }
    merge_account_catalogs(other_catalog)
    print("\nMerged Account Catalog:")
    for acc_number, details in account_catalog.items():
        print(f"{acc_number}: {details}")

    # Get all account numbers
    print("\nAll Account Numbers:")
    print(get_all_account_numbers())

    # Clear the account catalog
    clear_account_catalog()
    print("\nAccount Catalog After Clearing:")
    print(account_catalog)
"""
# bank_account_management.py

class BankAccountManagement:
    """
    Bank Account Management System

    This module uses lists, sets, tuples, and dictionaries to manage bank account data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of accounts and transactions.
    2. Tuples: To store immutable account details.
    3. Sets: To manage unique account types and transaction types.
    4. Dictionaries: To map account numbers to their details and manage account balances.
    """

    def __init__(self):
        # List of accounts with details (Account Number, Account Holder, Balance, Account Type)
        self.accounts = [
            (1001, "Alice", 5000.0, "Savings"),
            (1002, "Bob", 3000.0, "Checking"),
            (1003, "Charlie", 7000.0, "Savings"),
            (1004, "Diana", 10000.0, "Checking"),
            (1005, "Eve", 15000.0, "Savings")
        ]

        # List of transactions (Transaction ID, Account Number, Amount, Transaction Type)
        self.transactions = [
            (1, 1001, 500.0, "Deposit"),
            (2, 1002, 200.0, "Withdrawal"),
            (3, 1003, 1000.0, "Deposit"),
            (4, 1004, 500.0, "Withdrawal"),
            (5, 1005, 2000.0, "Deposit")
        ]

        # Set of unique account types
        self.account_types = set()

        # Adding account types from accounts
        for account in self.accounts:
            self.account_types.add(account[3])

        # Set of unique transaction types
        self.transaction_types = set()

        # Adding transaction types from transactions
        for transaction in self.transactions:
            self.transaction_types.add(transaction[3])

        # Dictionary to map account numbers to their details
        self.account_catalog = {acc[0]: acc for acc in self.accounts}

        # Dictionary to manage account balances
        self.account_balances = {acc[0]: acc[2] for acc in self.accounts}

    # List-Related Methods
    def find_account_index(self, account_number):
        """Finds the index of an account in the list."""
        for index, account in enumerate(self.accounts):
            if account[0] == account_number:
                return index
        return -1

    def sort_accounts_by_balance(self):
        """Sorts accounts by balance."""
        return sorted(self.accounts, key=lambda acc: acc[2])

    def reverse_transactions(self):
        """Reverses the list of transactions."""
        return self.transactions[::-1]

    def append_transaction(self, transaction):
        """Appends a new transaction to the list."""
        self.transactions.append(transaction)
        print(f"Transaction '{transaction}' added.")

    def remove_transaction(self, transaction_id):
        """Removes a transaction from the list."""
        self.transactions = [t for t in self.transactions if t[0] != transaction_id]
        print(f"Transaction ID '{transaction_id}' removed.")

    # Tuple-Related Methods
    def find_max_min_balance(self):
        """Finds the maximum and minimum balance of accounts."""
        balances = [acc[2] for acc in self.accounts]
        return max(balances), min(balances)

    def count_account_type_occurrences(self, account_type):
        """Counts the occurrences of a specific account type."""
        return sum(1 for acc in self.accounts if acc[3] == account_type)

    # Set-Related Methods
    def add_account_type(self, account_type):
        """Adds a new account type."""
        self.account_types.add(account_type)
        print(f"Account type '{account_type}' added.")

    def remove_account_type(self, account_type):
        """Removes an account type."""
        self.account_types.discard(account_type)
        print(f"Account type '{account_type}' removed.")

    def list_all_account_types(self):
        """Lists all account types."""
        return self.account_types

    def add_transaction_type(self, transaction_type):
        """Adds a new transaction type."""
        self.transaction_types.add(transaction_type)
        print(f"Transaction type '{transaction_type}' added.")

    def remove_transaction_type(self, transaction_type):
        """Removes a transaction type."""
        self.transaction_types.discard(transaction_type)
        print(f"Transaction type '{transaction_type}' removed.")

    def list_all_transaction_types(self):
        """Lists all transaction types."""
        return self.transaction_types

    def find_common_account_types(self, other_account_types):
        """Finds common account types between two sets."""
        return self.account_types.intersection(other_account_types)

    def find_unique_account_types(self):
        """Finds unique account types in the bank."""
        return self.account_types.difference({"Savings", "Checking"})

    def clear_account_types(self):
        """Clears all account types."""
        self.account_types.clear()
        print("All account types cleared.")

    # Dictionary-Related Methods
    def add_account(self, account_number, account_holder, balance, account_type):
        """Adds a new account to the bank."""
        if account_number not in self.account_catalog:
            self.account_catalog[account_number] = (account_number, account_holder, balance, account_type)
            self.account_balances[account_number] = balance
            self.account_types.add(account_type)
            print(f"Account '{account_holder}' added.")
        else:
            print(f"Account number '{account_number}' already exists.")

    def remove_account(self, account_number):
        """Removes an account from the bank."""
        if account_number in self.account_catalog:
            acc_details = self.account_catalog.pop(account_number)
            self.account_balances.pop(account_number)
            print(f"Account '{acc_details[1]}' removed.")
        else:
            print(f"Account number '{account_number}' not found.")

    def get_account_details(self, account_number):
        """Gets account details."""
        return self.account_catalog.get(account_number, "Account not found.")

    def list_accounts_by_type(self, account_type):
        """Lists all accounts by account type."""
        return [acc for acc in self.accounts if acc[3] == account_type]

    def count_accounts_by_type(self, account_type):
        """Counts accounts by account type."""
        return sum(1 for acc in self.accounts if acc[3] == account_type)

    def update_account_details(self, account_number, new_details):
        """Updates account details."""
        if account_number in self.account_catalog:
            self.account_catalog[account_number] = new_details
            self.account_balances[account_number] = new_details[2]
            print(f"Updated details for account number '{account_number}'.")
        else:
            print(f"Account number '{account_number}' not found.")

    def merge_account_catalogs(self, other_catalog):
        """Merges two account catalogs."""
        for acc_number, details in other_catalog.items():
            if acc_number not in self.account_catalog:
                self.account_catalog[acc_number] = details
                self.account_balances[acc_number] = details[2]
                self.account_types.add(details[3])
        print("Account catalogs merged.")

    def get_all_account_numbers(self):
        """Gets all account numbers."""
        return list(self.account_catalog.keys())

    def clear_account_catalog(self):
        """Clears the account catalog."""
        self.account_catalog.clear()
        self.account_balances.clear()
        print("Account catalog cleared.")

# Example usage
if __name__ == "__main__":
    bank = BankAccountManagement()

    print("Account Catalog:")
    for acc_number, details in bank.account_catalog.items():
        print(f"{acc_number}: {details}")

    print("\nAccount Types Available:")
    print(bank.account_types)

    print("\nTransaction Types Available:")
    print(bank.transaction_types)

    print("\nAccount Balances:")
    for acc_number, balance in bank.account_balances.items():
        print(f"{acc_number}: {balance}")

    # Add and remove accounts
    bank.add_account(1006, "Frank", 2000.0, "Checking")
    bank.remove_account(1003)

    print("\nAccount Catalog After Changes:")
    for acc_number, details in bank.account_catalog.items():
        print(f"{acc_number}: {details}")

    # Get account details
    print("\nAccount Details for Account Number 1002:")
    print(bank.get_account_details(1002))

    # List accounts by type
    print("\nAccounts of Type 'Savings':")
    print(bank.list_accounts_by_type("Savings"))

    # Count accounts by type
    print("\nCount of Accounts of Type 'Checking':")
    print(bank.count_accounts_by_type("Checking"))

    # Find account index
    print("\nIndex of Account Number 1002:")
    print(bank.find_account_index(1002))

    # Add and remove account types
    bank.add_account_type("Business")
    bank.remove_account_type("Savings")

    # List all account types
    print("\nAll Account Types:")
    print(bank.list_all_account_types())

    # Add and remove transaction types
    bank.add_transaction_type("Transfer")
    bank.remove_transaction_type("Withdrawal")

    # List all transaction types
    print("\nAll Transaction Types:")
    print(bank.list_all_transaction_types())

    # Append and remove transactions
    bank.append_transaction((6, 1001, 300.0, "Deposit"))
    bank.remove_transaction(2)

    print("\nTransactions After Changes:")
    for transaction in bank.transactions:
        print(transaction)

    # Sort accounts by balance
    print("\nAccounts Sorted by Balance:")
    for acc in bank.sort_accounts_by_balance():
        print(acc)

    # Reverse the list of transactions
    print("\nReversed List of Transactions:")
    print(bank.reverse_transactions())

    # Find the maximum and minimum balance of accounts
    max_balance, min_balance = bank.find_max_min_balance()
    print(f"\nMaximum Balance: {max_balance}, Minimum Balance: {min_balance}")

    # Count the occurrences of a specific account type
    print(f"\nOccurrences of 'Checking': {bank.count_account_type_occurrences('Checking')}")

    # Find common account types between two sets
    other_account_types = {"Savings", "Business", "Investment"}
    print(f"\nCommon Account Types: {bank.find_common_account_types(other_account_types)}")

    # Find unique account types in the bank
    print(f"\nUnique Account Types: {bank.find_unique_account_types()}")

    # Update account details
    bank.update_account_details(1002, (1002, "Bob", 3500.0, "Checking"))
    print(f"\nUpdated Account Details for Account Number 1002: {bank.get_account_details(1002)}")

    # Merge two account catalogs
    other_catalog = {
        1007: (1007, "Grace", 4000.0, "Savings"),
        1008: (1008, "Hank", 5000.0, "Checking")
    }
    bank.merge_account_catalogs(other_catalog)
    print("\nMerged Account Catalog:")
    for acc_number, details in bank.account_catalog.items():
        print(f"{acc_number}: {details}")

    # Get all account numbers
    print("\nAll Account Numbers:")
    print(bank.get_all_account_numbers())

    # Clear the account catalog
    bank.clear_account_catalog()
    print("\nAccount Catalog After Clearing:")
    print(bank.account_catalog)