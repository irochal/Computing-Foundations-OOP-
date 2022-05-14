## Author: Iro Chalastani Patsioura
from client_details import Client
from client_manager import Client_Manager
import csv


def main():

    my_client_list = Client_Manager()

    print("Should create new client object/instance/value")
    print(my_client_list)

    print("Get list of clients and print it")
    print((my_client_list.print_all_clients()))

    print("Find clients details depending on their name and print a new list")
    print((my_client_list.get_client_from_name("iro")))

    print("Find clients based on their birthdays and print a new list")
    print((my_client_list.get_client_from_birthday("17/04/1997")))

    print("Find all clients with negative account balances and print them")
    print((my_client_list.get_clients_with_negative_balance()))

    print("Add a new client to the list")
    my_client_list.add_client(Client("Iro","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0))
    print("Print the new list with the added client")
    print(my_client_list.print_all_clients())

    print("Remove a client from a list")
    my_client_list.delete_client(Client("Vivian", "Domerq", "Honorable", "III", "04/04/1973", "Marketing Assistant", 99924, 310))
    print("Print the new updated list")
    print(my_client_list.print_all_clients())

    print("Find index of client")
    print(my_client_list.get_index_of_client("Adan","Skures"))

    print("Edit client details")
    my_client_list.edit_client_details((Client("Pierrette","Boyall","Rev","Sr",
                                               "28/01/1988","General Manager",15952,179)), -30)
    print("Print new edited list")
    print(my_client_list.print_all_clients())

    print("Add money to a client's account balance")
    print(my_client_list.add_money_to_account(Client("Iro","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0), 1000))
    print("Print new updated list")
    print(my_client_list.print_all_clients())

    print("Subtract money from an account")
    print(my_client_list.subtract_money_from_account((Client("Adan","Skures","Ms","II","20/11/1971",
                                                             "Legal Assistant",62068,273)),1000))

    print("Print new updated list")
    print(my_client_list.print_all_clients())

    # Create a function that saves the final list into a new csv file, called new_list
    def save_list(new_list):
        with open('new_list.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for client in new_list :
                row = client.get_name(), client.get_last_name(), client.get_title(),\
                client.get_preferred_pronouns(), client.get_date_of_birth(), client.get_occupation(),\
                client.get_account_balance(), client.get_overdraft_limit()
                writer.writerow(row)

    save_list(my_client_list.get_client_list())


main()
