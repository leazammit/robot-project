from LoginObject import LoginObject
from robot.api.logger import info, debug, trace, console

class LoginLibrary:

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        self._session = None
        self.login = ''
        self.password = ''
        self._connection: LoginObject = None

    def connect(self, ip):
        self._connection = LoginObject(ip)

    def disconnect(self):
        self._connection = None

    @property
    def connection(self):
        if not self._connection:
            raise SystemError('No Connection established! Connect to server first!')
        return self._connection

    @property
    def session(self):
        if self._session is None:
            raise PermissionError('No valid user session. Authenticate first!')
        return self._session

    def set_login_name(self, login):
        '''Sets the users login name and stores it for authentication.'''
        self.login = login
        info(f'User login set to: {login}')

    def set_password(self, password):
        '''Sets the users login name and stores it for authentication.'''
        self.password = password
        info(f'Password set.')

    def execute_login(self):
        '''Triggers the authentication process at the backend and stores the session token.'''
        self._session = self.connection.authenticate(self.login, self.password)
        if self.session:
            info(f'User session successfully set.')
            debug(f'Session token is: {self.session}')
        self.login = self.password = ''

    def login_user(self, login, password) -> None:
        '''`Login User` authenticates a user to the backend.

        The session will be stored during this test suite.'''
        self._session = self.connection.authenticate(login, password)

    def logout_user(self):
        '''Logs out the current user.'''
        self.connection.logout(self.session)

    def get_user_details(self, user_id=None):
        '''Returs the user details of the given user_id or if None the own user data.'''
        return self.connection.get_user(self.session, user_id)


    def get_username(self, user_id=None):
        '''Returns the users full name of the given user_id or if None the own user data.'''
        return self.connection.get_user_name(self.session, user_id)
    
    def get_server_version(self):
        return self.connection.get_version(self.session)