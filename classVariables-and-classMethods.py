class Bank:
    bank_name = "MCB Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing Bank name:")
    print(f"User1's Bank name: {user1.bank_name}")
    print(f"User2's Bank name: {user2.bank_name}")

    Bank.change_bank_name("HBL Bank")

    print("\nAfter changing Bank name:")
    print(f"User1's Bank name: {user1.bank_name}")
    print(f"User2's Bank name: {user2.bank_name}")

