Overview of application: 

This is an application designed for a bank in order to be able to manage a specific client 
list loaded in the application. The client list should include the name, surname, title,
preferred pronoun, date of birth, occupation, account balance and overdraft limit.
This application allows the bank to add, delete as well as edit the details
of a client. Moreover, the application allows the bank to search clients by
exactly matching names, date of birth or negative account balance. Then the application
returns back a new list of the details of clients with matching results. Moreover, the 
bank can use the application in order to add or subtract money from an account of a specific
client. The bank can also change a client 5£ if their account balance exceeds their
overdraft limit. Finally, the application allows the bank to save the new list, with 
the updated details of the clients, into a new csv file.\

Assumptions:

The first assumption is that the bank should have a list of clients that includes all of their details\
The second assumption is that in the client list the name, surname, preferred pronoun, date
of birth and occupation should be entered as a string while the account balance and overdraft
limit as integers\
The third assumption is that the user of the application should enter exact matching names,\
and dates of birth when searching for a client\
The fourth assumption is that system will not be used by multiple users of the bank at once 
since that could cause problems (i.e: the final list to be different) if different client details
were edited at the same time from different users.\
The fifth assumption is that the end user that is going to use the application will have some
very basic skills in using a computer/laptop\
The sixth assumption is that the list uploaded in the application will be in csv form\

Running the application:

In order to run the application there needs to exist a list with the client details in csv form. \
Other than that the user then needs to run the client details file and the client manager file \
and then use the main file in order to search for clients, or make changes to client details or\
the client list. The user can also use the main file in order to save the update list into a new csv. 

Using the application example: 

Let's assume that there exist a list with 100 clients and two specific clients are: 
Client("Adan","Skures","Ms","II","20/11/1971","Legal Assistant",62068,273) and\
Client("Vivian","Domerq","Honorable","III","04/04/1973","Marketing Assistant",99924,310)\

First of all, assuming that the user wants to add a client they need to go to the main file and\
call the add client function to which they will enter the details of the client they want to add \
to the list. So given a new client "Iro" the user needs to call: 
my_client_list.add_client(Client("Iro","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0))\
Then this client is added to the list!

Now if they want to remove a client they need to call the delete function and enter the client\
details of the client they want to remove. So given that they want to remove "Vivian" they\
need to call:\
my_client_list.delete_client(Client("Vivian", "Domerq", "Honorable", "III", "04/04/1973", "Marketing Assistant", 99924, 310))\
Then this client is removed from the list!\
Note that if the client details entered are wrong and the application cannot find the client then an
appropriate warning is returned to the user. 

If they want to edit the details of a client they first need to call the find client by index function in order to 
now the position of the client on the list. So by just entering their name and surname in the function they 
can find out their. Now let's assume that the user wants to edit the details of Adan, so they need to call:\
my_client_list.get_index_of_client("Adan","Skures")\
This returns back the number 95\
Note that if the user enters a non valid index number (i.e: an index outside the range of the list)
the application returns back an appropriate warning\
Now in order to edit for example the occupation of Adan the user needs to call the edit function
and enter updated details (in this case occupation) as well as the index number. So the user needs to call:\
 my_client_list.edit_client_details(Client("Adan","Skures","Ms","II","20/11/1971","Statistician",62068,273))\
Then the occupation changes successfully and the list is updated!\
Again if the user enters a non-valid index number (i.e: an index outside the range of the list)
the application returns back an appropriate warning\

Now if they want to search a client by name then the user needs to call the find client by name function, 
enter the name (e.g "Adan") of the client they want to search. So they need to call:\
my_client_list.get_client_from_name("Adan")\
Then the user gets back the full details of Adan.\
Note that if the name does not exist then the application returns back an appropriate warning

Similarly, if the user wants to search a client based on their date of birth they need to call the
get client from birthday function and enter the date of birth they want to search. So for
example if they enter the date of birth of Adan (i.e: 20/11/1971), they need to call:\
my_client_list.get_client_from_birthday("20/11/1971")\
Then the application returns back all the details on Adan\
Again if the date of birth does not exist then the application returns back an appropriate 
warning

Just like above, if the user wants to find all the clients with negative account balance they 
need to call the get client from negative account balance function. In this function they do
not need to enter any client details. So the user need to call:\
my_client_list.get_clients_with_negative_balance()\
If there are clients with negative account balance then the application returns back a list of
the clients and their details. If there are no clients with negative account balance then the 
application returns back an appropriate warning. 

Now the user can also add an amount of money to the account balance of a specific client (e.g : Adan's account), by 
calling the add money to account function and entering the client to whom they want to
add money to their account, as well as the amount of money they want to add. So the user 
need to call:\
my_client_list.add_money_to_account(Client("Adan","Skures","Ms","II","20/11/1971","Statistician",62068,273), 1000)\
Then the application returns back the new account balance (in this case: 63068) and the account balance of this client is updated on the list\
Note that if the amount added is non valid (i.e: is negative), then the application returns back 
and appropriate warning statement. 

Similarly, the user can subtract money form a clients account by simply calling the subtract 
money from account function and entering the client details and the amount of money that they 
want to subtract. Let's assume that the user want to subtract money from Adan's account, 
then they need to call: 
my_client_list.add_money_to_account(Client("Adan","Skures","Ms","II","20/11/1971","Statistician",63068,273), 1000)\
Then the application returns a statement with the new account balance (in this case: 62068), and the account
balance of the client is updated on the list.\
Note that if after the subtraction the account balance of the client is below the overdraft
limit then the client is charged 5£ and an appropriate statement informing the user is returned\
Also note that if the amount added is non valid (i.e: is negative), then the application returns back 
and appropriate warning statement. \

NOTE THAT: If the user wants to get back the updated list of the clients, when adding, deleting,
editing, adding money, or subtracting money, then the user needs to call the print all clients function in order to get back the new list in a specific format. So for example if the 
user wants to get back the list with the added client they need to call:\
my_client_list.add_client(Client("Iro","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0))\
and then:\
print(my_client_list.print_all_clients())

Finally, if the user wants to save the updated client list, they just need to call the 
save list function together with the get client list function. This can be done in the following 
way:\
save_list(my_client_list.get_client_list())


