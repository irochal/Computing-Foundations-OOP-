## Author: Iro Chalastani Patsioura
import unittest
from client_details import Client
from client_manager import Client_Manager


class TestClient(unittest.TestCase):

    # set up values
    def setUp(self):
        self.name = "Cheryl"
        self.last_name = "Olufsen"
        self.title = "IV"
        self.preferred_pronouns = "Ms"
        self.date_of_birth = "28/03/1991"
        self.occupation = "Analyst Programmer"
        self.account_balance = 71097
        self.overdraft_limit = 342
        self.client = Client(self.name,self.last_name,self.title,self.preferred_pronouns,
                             self.date_of_birth,self.occupation,self.account_balance,self.overdraft_limit)

        # test getters/constructor

    def test_get_name(self):
        self.assertEqual(self.client.get_name(), self.name)

    def test_get_last_name(self):
        self.assertEqual(self.client.get_last_name(), self.last_name)

    def test_get_title(self):
        self.assertEqual(self.client.get_title(), self.title)

    def test_get_preferred_pronouns(self):
        self.assertEqual(self.client.get_preferred_pronouns(), self.preferred_pronouns)

    def test_get_date_of_birth(self):
        self.assertEqual(self.client.get_date_of_birth(), self.date_of_birth)

    def test_get_occupation(self):
        self.assertEqual(self.client.get_occupation(), self.occupation)

    def test_get_account_balance(self):
        self.assertEqual(self.client.get_account_balance(), self.account_balance)

    def test_get_overdraft_limit(self):
        self.assertEqual(self.client.get_overdraft_limit(), self.overdraft_limit)

    # test constructor, ValueError should be raised if any parameter is set to None
    def test_constructor_name_none(self):
        with self.assertRaises(ValueError):
            Client(None,self.last_name,self.title,self.preferred_pronouns, self.date_of_birth,
                   self.occupation,self.account_balance,self.overdraft_limit)

    def test_constructor_last_name_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,None,self.title,self.preferred_pronouns, self.date_of_birth,
                   self.occupation,self.account_balance,self.overdraft_limit)

    def test_constructor_title_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,None,self.preferred_pronouns, self.date_of_birth,
                   self.occupation,self.account_balance,self.overdraft_limit)

    def test_constructor_preferred_pronouns_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,self.title,None,self.date_of_birth,
                   self.occupation,self.account_balance,self.overdraft_limit)

    def test_constructor_date_of_birth_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,self.title,self.preferred_pronouns, None,
                   self.occupation,self.account_balance,self.overdraft_limit)

    def test_constructor_occupation_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,self.title,self.preferred_pronouns,self.date_of_birth,
                   None,self.account_balance,self.overdraft_limit)

    def test_constructor_account_balance_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,self.title,self.preferred_pronouns,self.date_of_birth,
                   self.occupation,None,self.overdraft_limit)

    def test_constructor_overdraft_limit_none(self):
        with self.assertRaises(ValueError):
            Client(self.name,self.last_name,self.title,self.preferred_pronouns, self.date_of_birth,
                   self.occupation,self.account_balance,None)

    # Test setters
    def test_set_name(self):
        new_name = "Iro"
        self.client.set_name(new_name)
        self.assertEqual(self.client.get_name(), new_name)

    def test_set_last_name(self):
        new_last_name = "Chalastani"
        self.client.set_last_name(new_last_name)
        self.assertEqual(self.client.get_last_name(), new_last_name)

    def test_set_title(self):
        new_title = "Miss"
        self.client.set_title(new_title)
        self.assertEqual(self.client.get_title(), new_title)

    def test_set_preferred_pronouns(self):
        new_preferred_pronouns = "She"
        self.client.set_preferred_pronouns(new_preferred_pronouns)
        self.assertEqual(self.client.get_preferred_pronouns(), new_preferred_pronouns)

    def test_set_date_of_birth(self):
        new_date_of_birth = "18/04/2002"
        self.client.set_date_of_birth(new_date_of_birth)
        self.assertEqual(self.client.get_date_of_birth(), new_date_of_birth)

    def test_set_occupation(self):
        new_occupation = "Statistician"
        self.client.set_occupation(new_occupation)
        self.assertEqual(self.client.get_occupation(), new_occupation)

    def test_set_account_balance(self):
        new_account_balance = 50000
        self.client.set_account_balance(new_account_balance)
        self.assertEqual(self.client.get_account_balance(), new_account_balance)

    def test_set_overdraft_limit(self):
        new_overdraft_limit = 500
        self.client.set_overdraft_limit(new_overdraft_limit)
        self.assertEqual(self.client.get_overdraft_limit(), new_overdraft_limit)

    # Testing the repr function
    def test_repr(self):
        expected = "Client('{}','{}','{}','{}','{}','{}','{}','{}')"
        expected = expected.format(self.name,self.last_name,self.title,self.preferred_pronouns,
                             self.date_of_birth,self.occupation,self.account_balance,self.overdraft_limit)
        self.assertTrue(isinstance(repr(self.client), str))
        # assert that when evaluated, it should also be a Car object
        self.assertTrue(isinstance(eval(repr(self.client)), Client))
        # test the value is as expected
        self.assertEqual(repr(self.client), expected)

    # Testing eq and hash functions
    def test_eq(self):
        client = Client("Cheryl","Olufsen","IV","Ms","28/03/1991","Analyst Programmer",71097,342)
        other = Client("Iro","Olufsen","IV","Ms","28/03/1991","Analyst Programmer",71097,342)
        self.assertEqual(self.client,client)
        self.assertNotEqual(self.client,other)

    def test_hash(self):
        client = hash(Client("Cheryl","Olufsen","IV","Ms","28/03/1991","Analyst Programmer",71097,342))
        other = hash(Client("Iro","Olufsen","IV","Ms","28/03/1991","Analyst Programmer",71097,342))
        self.assertEqual(self.client.__hash__(), client)
        self.assertNotEqual(self.client.__hash__(),other)


class TestClientManager(unittest.TestCase):

    def setUp(self):
        self.client_manager = Client_Manager()

    # Testing if the get client list returns a list with length of 100
    def test_get_client_list(self):
        actual = self.client_manager.get_client_list()
        self.assertTrue(isinstance(actual,list))
        self.assertEqual(len(actual), 100)

    # Testing if the add client function returns a list with the added client (a list of length 101)
    def test_add_client(self):
        actual = self.client_manager.add_client(Client("Iro","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0))
        self.assertEqual(len(actual),101)

    # Testing if the  delete client function works by checking that the length of the list is 99
    def test_delete_client(self):
        actual = self.client_manager.delete_client((Client("Adan","Skures","Ms","II",
                                               "20/11/1971","Legal Assistant",62068,273)))
        self.assertEqual(len(actual),99)

    # Testing that if we try to delete a client that is not on the list, then the delete function
    # returns an appropriate warning
    def test_delete_client_non_valid_client(self):
        actual = self.client_manager.add_client(Client("Rea","Chalastani","Ms","She/her","04/12/2000","Data Scientist",5000,0))
        self.assertTrue("Not valid client entered. Please check")

    # Testing that the get index function returns back an index (integer)
    def test_get_index_of_client(self):
        actual = self.client_manager.get_index_of_client("Bennie","Mossbee")
        self.assertTrue(isinstance(actual,int))

    # Testing that if we enter a client that does not exist the index function returns an appropriate statement
    def test_index_of_non_existing_client(self):
        self.client_manager.get_index_of_client("Ben", "Mossbee")
        self.assertTrue("Client not found. Please check")

    # Testing that the edit client function works, by checking if the occupation has changed successfully
    def test_edit_client(self):
        self.client_manager.edit_client_details((Client("Bennie","Mossbee","Rev", "Jr", "08/01/1994",
                                                     "HR Assistant", 25344, 397)), 98)
        client = self.client_manager.get_client_list()
        self.assertEqual(client[98].get_occupation(), "HR Assistant")

    # Testing that if an invalid index number is entered the function returns an appropriate warning
    def test_edit_client_using_invalid_index(self):
        self.client_manager.edit_client_details((Client("Bennie", "Mossbee", "Rev", "Jr", "08/01/1994",
                                                        "HR Assistant", 25344, 397)), 122)
        self.assertTrue("Not valid index number. Please check")

    # Testing that the get client from name function works by checking that if we enter the name Cheryl a list
    # of 1 person (length 1) is returned
    def test_get_client_list_from_name(self):
        actual = self.client_manager.get_client_from_name("Cheryl")
        self.assertEqual(len(actual),1)

    # Testing that if a name that is not on the list is entered in the get client from name function
    # then the function returns an appropriate statement
    def test_get_client_list_from_name_namedoesnotexist(self):
        self.client_manager.get_client_from_name("Athina")
        self.assertTrue("There are no clients with such name. Please check the name entered")

    # Testing that the get client from name function works by checking that if we enter the date 20/03/1991 a list
    # of 1 person (length 1) is returned
    def test_get_client_from_birthday(self):
        actual = self.client_manager.get_client_from_birthday("28/03/1991")
        self.assertEqual(len(actual),1)

    # Testing that if a date that is not on the list is entered in the get client from name function
    # then the function returns an appropriate statement
    def test_get_client_from_birthday_birthdaydoesnotexist(self):
        self.client_manager.get_client_from_birthday("05/03/2008")
        self.assertTrue("There are no clients with this date of birth. Please check the date of birth entered")

    # Testing that the get clients with negative account function works by checking that it returns back an empty list
    # since there are no clients with negative balance in the mock list
    def test_get_clients_with_negative_account_balance(self):
        actual = self.client_manager.get_clients_with_negative_balance()
        self.assertEqual(actual, None)

    # Testing that the add money to account function works
    def test_add_money_to_account(self):
        self.client_manager.add_money_to_account(Client("Cheryl","Olufsen","Ms","IV","28/03/1991","Analyst Programmer",71097,342), 3)
        self.client_manager.get_client_list()
        client = self.client_manager.get_client_list()
        self.assertEqual(client[99].get_account_balance(),71100)

    # Testing that if a non valid amount is entered to the add function , then it returns back
    # an appropriate warning statement
    def test_add_non_valid_amount_to_account(self):
        self.client_manager.add_money_to_account(Client("Cheryl","Olufsen","Ms","IV","28/03/1991","Analyst Programmer",71097,342), -10)
        self.assertTrue("Non valid deposit amount entered. Please check")

    # Testing that if a non valid client is entered to the add function , then it returns back
    # an appropriate warning statement
    def test_add_non_valid_client_entered_to_add_function(self):
        self.client_manager.add_money_to_account(Client("Marios","Filippou","Ms","IV","28/03/1991","Analyst Programmer",71097,342), -10)
        self.assertTrue("Non valid client entered. Please check")

    # Testing that the subtract money from account function works
    def test_subtract_money_from_account(self):
        actual = self.client_manager.subtract_money_from_account(Client("Adan","Skures","Ms","II","20/11/1971",
                                                             "Legal Assistant",62068,273),1000)
        client = self.client_manager.get_client_list()
        self.assertEqual(client[95].get_account_balance(), 61068)

    # Testing that if a non valid client is entered to the add function , then it returns back
    # an appropriate warning statement
    def test_subtract_non_valid_client_entered_to_subtract_function(self):
        self.client_manager.add_money_to_account(Client("George","Walton","Ms","II","20/11/1971",
                                                             "Personal Assistant",62068,273),1000)
        self.assertTrue("Non valid client entered. Please check")

    # Testing that if the account balance after the withdrawal is over the overdraft limit
    # the client is charged 5 additional £
    def test_subtract_money_from_account_over_overdraft_limit(self):
        self.client_manager.subtract_money_from_account(Client("Adan","Skures","Ms","II","20/11/1971",
                                                             "Legal Assistant",62068,273),70000)
        client = self.client_manager.get_client_list()
        self.assertEqual(client[95].get_account_balance(), -7937)
        self.assertTrue("The account balance is: -7937 You have been charged 5£"
                        " because you went above your overdraft limit")

























