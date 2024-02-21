import socket
import threading

class Bank_Account:
    def __init__(self, account_number, holder_name, phone_number):
        self.account_number = account_number
        self.holder_name = holder_name
        self.phone_number = phone_number
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        return f"Amount Deposited: {amount}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            return f"You Withdrew: {amount}"
        else:
            return "Insufficient balance"

    def display(self):
        return f"Net Available Balance= {self.balance}"

    def display_transactions(self):
        return {"Transaction History": self.transactions}

def handle_client(client_socket, addr, bank_account):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            if data == '1':
                amount = float(client_socket.recv(1024).decode('utf-8'))
                if amount < 0:
                    client_socket.sendall("Invalid input. Amount cannot be negative.".encode('utf-8'))
                else:
                    result = bank_account.deposit(amount)
                    client_socket.sendall(f"{result}\nCurrent Balance: {bank_account.display()}".encode('utf-8'))

            elif data == '2':
                amount = float(client_socket.recv(1024).decode('utf-8'))
                if amount < 0:
                    client_socket.sendall("Invalid input. Amount cannot be negative.".encode('utf-8'))
                else:
                    result = bank_account.withdraw(amount)
                    client_socket.sendall(f"{result}\nCurrent Balance: {bank_account.display()}".encode('utf-8'))

            elif data == '3':
                client_socket.sendall(f"Current Balance: {bank_account.display()}".encode('utf-8'))

            elif data == '4':
                transactions = bank_account.display_transactions()
                client_socket.sendall(str(transactions).encode('utf-8'))

            elif data == '5':
                client_socket.sendall("Exiting...".encode('utf-8'))
                break

            else:
                client_socket.sendall("Invalid choice. Please enter a number between 1 and 5.".encode('utf-8'))

        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)

    print("Server is listening on port 5555...")

    # Sample account
    account_number = "7384282933"
    holder_name = "test user"
    phone_number = "3487489302"
    s = Bank_Account(account_number, holder_name, phone_number)

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, s))
        client_handler.start()

if __name__ == '__main__':
    start_server()
