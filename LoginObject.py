from typing import List, Dict
class LoginObject:

  
  def authenticate(self, login: str, password: str):
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (login in us) and (password in pw):
            print ("Login successful!")
            return True
    print ("Wrong username/password")
    return False

  def get_version(self, token):
    return '1.0.0'

  def logout(self, token): ...
  def get_user_id(self, token, login) -> str: ...
  def get_user_name(self, token, user_id) -> str: ...
  def get_user(self, token, user_id=None) -> Dict[str, str]: ...
  def get_user_all(self, token) -> List[Dict[str, str]]: ...
  def delete_user(self, token, userid): ...
  def get_logout(self, token): ...
  def put_user_password(self, token, new_password, user_id=None): ...
  def put_user_name(self, token, name, user_id=None): ...
  def put_user_right(self, token, right, user_id): ...
  def post_new_user(self, token, name, login) -> str: ...