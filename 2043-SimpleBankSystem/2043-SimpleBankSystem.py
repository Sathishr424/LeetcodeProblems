# Last updated: 26/10/2025, 1:53:55 pm
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or account2 > self.n: return False
        account1 -= 1
        account2 -= 1

        if self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n: return False
        account -= 1
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n: return False
        account -= 1

        if self.balance[account] >= money:
            self.balance[account] -= money
            return True
        
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)