"""for exercise 9.12"""
from user import User
#import user
# you can write etiher both of them

class Privileges():
    def __init__(self,privileges=["can add post","can delete post","can ban user"]):
        self.priv = privileges

    def show_privileges(self):
            """used to show privileges
            """
            for self.p in self.priv:
                msg = "\n The admin has privileges: \n"
                msg += str(self.p)
                print(msg)

class Administrator(User):
    """making a class for exercise 9.7 from exercise 9.5
    """
    def __init__(self):
        self.px = Privileges()


#admin = Administrator()
#admin.px.show_privileges()
