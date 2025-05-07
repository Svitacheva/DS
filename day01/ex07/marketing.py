import sys


def get_arg_and_print_result():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    clients = set(clients)
    participants = set(participants)
    recipients = set(recipients)

    if len(sys.argv) != 2:
        print('Error: No task name or many tasks')
        sys.exit(1)

    arg = sys.argv[1]
    if arg == 'call_center':
        not_get_email(clients, recipients)
    elif arg == 'potential_clients':
        not_clients(participants, clients)
    elif arg == 'loly_program':
        not_participate(clients, participants)
    else:
        print('Error: Incorrect task name')
        sys.exit(1)


def not_get_email(clients, recipients):
    print(list(clients - recipients))


def not_clients(participants, clients):
    print(list(participants - clients))


def not_participate(clients, participants):
    print(list(clients - participants))


if __name__ == '__main__':
    get_arg_and_print_result()
