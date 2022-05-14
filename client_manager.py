## Author: Iro Chalastani Patsioura
from client_details import Client


# Creating the client manager class
class Client_Manager:

    def __init__(self):
        # creating an empty list and populating it with the rows of the csv file that the user enters
        self.__client_list = []
        with open("MOCK_DATA (6).csv","r") as f:
            for line in f:
                details = line.strip().split(",")
                self.__client_list.append(Client(details[0], details[1], details[2], details[3], details[4], details[5],
                                                 int(details[6]), int(details[7])))

    # Create a function that returns back the client list
    def get_client_list(self):
         return self.__client_list

    # Creating a function that prints all clients in a specific format
    def print_all_clients(self):
        out = "{:30} {:30} {:30} {:30} {:30} {:30} {:30} {:30}"
        print(out.format("First Name", "Last Name", "Title","Preferred Pronouns", "Date Of Birth",
                         "Occupation", "Account Balance", "Overdraft Limit"))
        for client in self.__client_list:
            print(out.format(client.get_name(), client.get_last_name(), client.get_title(), client.get_preferred_pronouns(),
                             client.get_date_of_birth(), client.get_occupation(), str(client.get_account_balance()),
                             str(client.get_overdraft_limit())))

    # Creating the function to add a client, where the user adds all the details of a client
    # and then the client is added to the list
    def add_client(self,client):
            if isinstance(client,Client):
                self.__client_list.append(client)
                return self.__client_list
            else:
                # If some details are missing let the user know
                print("Not valid client entered. Please check")

    # Creating a function that deletes the client that the user enters
    def delete_client(self,client):
        if isinstance(client,Client):
            self.__client_list.remove(client)
            return self.__client_list
        else:
            # If some details are missing or the client does not exist let the user know
            print("Not valid client entered. Please check")

    # Creating a function gets the name and last name of a client and returns their index number
    # so that their details can be edidted
    def get_index_of_client(self,name,last_name):
        for clnt in self.__client_list:
            # Finding the index by matching name and last name
            if clnt.get_name() == name \
                and clnt.get_last_name() == last_name:
                return self.__client_list.index(clnt)
        else:
            # Raising an error if the details are wrong or client does not exist
            print("Client not found. Please check")

    # Creating a function that allows the user to enter the index number of a client and the
    # edited details, and returns back the client with the new details
    def edit_client_details(self, client, index):
        if  index > len(self.__client_list) or index < 0:
            print("Not valid index number. Please check")
        elif isinstance(client,Client) and 0 <= index <= len(self.__client_list):
                self.__client_list[index] = client

    # Creating a function that adds money to a specific client's account
    # The function allows the user to enter the specific client and the amount to be added
    def add_money_to_account(self, client, amount_to_be_added):
        if client not in self.__client_list:
            print("Non valid client entered. Please check")
        else:
            for clnt in self.__client_list:
                if clnt == client:
                    # the amount needs to be positive to be added
                    if amount_to_be_added > 0:
                        # Using the getter and setter functions to access the account balance and change it
                        clnt.set_account_balance(clnt.get_account_balance() + amount_to_be_added)
                        print("The new account balance is: ", clnt.get_account_balance())
                    else:
                        # Raising an error if the amount entered is not valid
                        print("Non valid deposit amount entered. Please check")

        # Creating a funtion that allows to subtract money form a specific client's account
        # The function allows the user to enter the specific client and the amount to be subtracted

    def subtract_money_from_account(self, client, amount_to_be_subtracted):
        if client not in self.__client_list:
            print("Non valid client entered. Please check")
        else:
            for clnt in self.__client_list:
                if clnt == client:
                    # we need a positive amount to subtract and to
                    # Check if the account balance is less than the overdraft limit, and imposing a 5£ fee
                    if amount_to_be_subtracted > 0 and \
                            clnt.get_account_balance() - amount_to_be_subtracted < - clnt.get_overdraft_limit():
                        # Use getters and setters to access and change the account balance
                        clnt.set_account_balance(clnt.get_account_balance() - amount_to_be_subtracted - 5)
                        print("The account balance is:", clnt.get_account_balance(),
                              "You have been charged 5£ because you went above your overdraft limit")
                        # Use getters and setters to access and change the account balance
                    elif amount_to_be_subtracted > 0:
                        # Use getters and setters to access and change the account balance
                        clnt.set_account_balance(clnt.get_account_balance() - amount_to_be_subtracted)
                        print("The new account balance is: ", clnt.get_account_balance())

    # Creating a funtion that returns back teh client(s) with a specific name
    def get_client_from_name(self,client_name):
        # Creating an empty list and populating it with the client(s) details
        list_of_client_names = []
        for client in self.__client_list:
            # Checking if the client name exists on the list
            if client.get_name() == client_name:
                list_of_client_names.append(client)
                return list_of_client_names
        else:
            # If the name does not exist informing the user about this
            print("There are no clients with such name. Please check the name entered")

    # Creating a function that returns the client(s) based on their birthdays
    def get_client_from_birthday(self, client_date_of_birth):
        # Creating a list and populating with the client(s) details
        list_of_clients_birthday = []
        for client in self.__client_list:
            # Checking if the date exists on the list
            if client.get_date_of_birth() == client_date_of_birth:
                list_of_clients_birthday.append(client)
                return list_of_clients_birthday
        else:
            # If there are not clients with the specific date of birth let the user know
            print("There are no clients with this date of birth. Please check the date of birth entered")

    # Creating a function that returns the client(s) who have a negative account balance
    def get_clients_with_negative_balance(self):
        # Creating a list and populating it with the client(s) details
        list_of_clients_with_negative_balance = []
        for client in self.__client_list:
            # Checking if there are clients with negative account balance
            if client.get_account_balance() < 0:
                list_of_clients_with_negative_balance.append(client)
                return list_of_clients_with_negative_balance

        else:
            # If there are no clients with negative account balance let the user know
            print("There are no clients with negative account balance")








