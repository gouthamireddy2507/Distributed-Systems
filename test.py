import socket

def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

def run_test():
    print("Testing...")

    account_details = {
        'account_number': "7384282933",
        'holder_name': "test user",
        'phone_number': "3487489302"
    }

    for detail, value in account_details.items():
        request = f"{detail}|{value}"
        send_request(request)

    test_transactions = [
        ("deposit", 100.0),
        ("withdraw", 30.0),
        ("display_balance", None),
        ("deposit", 50.0),
        ("withdraw", 20.0),
        ("display_transactions", None),
        ("exit", None)
    ]

    for action, amount in test_transactions:
        if amount is not None:
            request = f"{action}|{amount}"
        else:
            request = action

        send_request(request)

if __name__ == "__main__":
    run_test()
