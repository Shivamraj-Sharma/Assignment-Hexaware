class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_email(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            print("Invalid email address")
    
    def set_phone_number(self, phone_number):
        if self.validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            print("Invalid phone number")
    
    def set_address(self, address):
        self.address = address
    
   
    def print_all_info(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email Address:", self.email)
        print("Phone Number:", self.phone_number)
        print("Address:", self.address)
    
    def validate_email(self, email):
       
        if '@' in email:
            return True
        else:
            return False
    
    
    def validate_phone_number(self, phone_number):
       
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        else:
            return False

customer1 = Customer()

customer1.set_customer_id(1)
customer1.set_first_name("Raj")
customer1.set_last_name("Kumar")
customer1.set_email("rajkumar@gmail.com")
customer1.set_phone_number("1234567890")
customer1.set_address("India")