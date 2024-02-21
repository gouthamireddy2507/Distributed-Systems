# client.py
import socket

def menu():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Balance")
    print("4. List Transactions")
    print("5. Exit")

def deposit(client_socket):
    amount = float(input("Enter amount to be Deposited: "))
    if amount < 0:
        print("Invalid input. Amount cannot be negative.")
    else:
        client_socket.sendall('1'.encode('utf-8'))
        client_socket.sendall(str(amount).encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

def withdraw(client_socket):
    amount = float(input("Enter amount to be Withdrawn: "))
    if amount < 0:
        print("Invalid input. Amount cannot be negative.")
    else:
        client_socket.sendall('2'.encode('utf-8'))
        client_socket.sendall(str(amount).encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

def display_balance(client_socket):
    client_socket.sendall('3'.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

def display_transactions(client_socket):
    client_socket.sendall('4'.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

def exit_program(client_socket):
    client_socket.sendall('5'.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(response)
if __name__ == '__main__':
    option = input("Enter 1 for deposit or 2 for withdrawal: ")

    if option == '1':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 5556))  # Connect to deposit server
    elif option == '2':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 5555))  # Connect to withdraw server
    else:
        print("Invalid option. Exiting.")
        exit()

    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            deposit(client_socket)
        elif choice == '2':
            withdraw(client_socket)
        elif choice == '3':
            display_balance(client_socket)
        elif choice == '4':
            display_transactions(client_socket)
        elif choice == '5':
            exit_program(client_socket)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    client_socket.close()