## Author: Iro Chalastani Patsioura
# Creating the client class that has all the details of a client
class Client:
    # Constructor
    def __init__(self, name,last_name,title,preferred_pronouns,date_of_birth,occupation,account_balance,overdraft_limit):
        if (name == None) or (last_name == None) or (title == None) or (preferred_pronouns == None) or (date_of_birth == None) \
                or (occupation == None) or (account_balance == None) or (overdraft_limit == None):
            message = "A field for client details is empty, please check."
            raise ValueError(message)
        # Adding the attributes and making them private for "privacy" reasons
        self.__name = name
        self.__last_name = last_name
        self.__title = title
        self.__preferred_pronouns = preferred_pronouns
        self.__date_of_birth = date_of_birth
        self.__occupation = occupation
        self.__account_balance = account_balance
        self.__overdraft_limit = overdraft_limit

    #Creating an equality funtion in order to make clients with the same attributes equal, so that we can add, remove and edit their details
    def __eq__(self, other):
        if type(other) is type(self):
            return (self.__name, self.__last_name,self.__title, self.__preferred_pronouns,
                    self.__date_of_birth, self.__occupation, self.__account_balance, self.__overdraft_limit)\
                   == (other.__name, other.__last_name, other.__title, other.__preferred_pronouns,
                    other.__date_of_birth, other.__occupation, other.__account_balance, other.__overdraft_limit)
        else:
            return NotImplemented

    #Creating a hash function to make hashes of clients with the same attributes equal
    def __hash__(self):
        return hash((self.__name, self.__last_name,self.__title, self.__preferred_pronouns,
                    self.__date_of_birth, self.__occupation, self.__account_balance, self.__overdraft_limit))

    #Define getter functions in order to be able to access the private attributes
    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_preferred_pronouns(self):
        return self.__preferred_pronouns

    def get_title(self):
        return self.__title

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_occupation(self):
        return self.__occupation

    def get_account_balance(self):
        return self.__account_balance

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    #Definig setter functions in order to be able to change the private attributes
    def set_name(self,new_name):
        self.__name = new_name

    def set_last_name(self,new_last_name):
        self.__last_name = new_last_name

    def set_title(self, new_title):
        self.__title = new_title

    def set_preferred_pronouns(self,new_preferred_pronouns):
        self.__preferred_pronouns = new_preferred_pronouns

    def set_date_of_birth(self, new_date_of_birth):
        self.__date_of_birth = new_date_of_birth

    def set_occupation(self, new_occupation):
        self.__occupation = new_occupation

    def set_account_balance(self, new_account_balance):
        self.__account_balance = new_account_balance

    def set_overdraft_limit(self, new_overdraft_limit):
        self.__overdraft_limit = new_overdraft_limit

    # Adding a repr function in order to represent the object
    def __repr__(self):
        out = "Client('{name}','{last_name}','{title}','{preferred_pronouns}','{date_of_birth}'," \
              "'{occupation}','{account_balance}','{overdraft_limit}')"
        return out.format(name = self.get_name(),last_name = self.get_last_name(),title = self.get_title(),
                          preferred_pronouns = self.get_preferred_pronouns(),date_of_birth = self.get_date_of_birth(),
                 occupation = self.get_occupation(), account_balance = self.get_account_balance(),
                          overdraft_limit = self.get_overdraft_limit())

