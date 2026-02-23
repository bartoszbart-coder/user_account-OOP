class UserAccount:
    def __init__(self,user:str,password:str, max_login_attempts:int=3):
        if not isinstance(user,str) or not user.strip():
            raise ValueError("Username must be a non-empty string")
        self.user=user.strip()
        self.password=password
        self._failed_attempts=0
        self._is_logged_in=False
        self._max_login_attempts=max_login_attempts
        self._locked=False

    @property
    def password(self):
        raise AttributeError("Password cannot be read")
    
    @password.setter
    def password(self,value):
        if not isinstance(value,str):
            raise TypeError("It has to be a string")
        if len(value)<8 or not any(i.isdigit()for i in value):
            raise ValueError("Password needs to contain at least 1 digit and 8 characters")
        self._password=value
    
    @property
    def is_logged_in(self):
        return self._is_logged_in
    
    def check_password(self,guess):
        return guess==self._password
    
    def login(self,guess):
        if self._locked:
            return "LOCKED"
        if self.check_password(guess):
            self._failed_attempts=0
            self.is_logged_in=True
            return "OK"
        self._failed_attempts += 1 
        if self._failed_attempts >=self._max_login_attempts:
            self._locked=True
        return "FAIL"
    def logout(self):
        self._is_logged_in=False

if __name__ == "__main__":
    acc = UserAccount("Bartosz", "Passw0rd9", max_login_attempts=3)

    print(acc.login("wrong"))      # FAIL
    print(acc.login("wrong"))      # FAIL
    print(acc.login("wrong"))      # FAIL
    print(acc.login("Passw0rd9"))  # LOCKED
    print(acc.is_logged_in)        # False