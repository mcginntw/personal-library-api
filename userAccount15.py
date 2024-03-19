import warnings

class UserAccount:
    """A class representing a user account with username and password."""

    def __init__(self, username, password):
        """
        Initialize a UserAccount object.

        :param username: The username for the user account.
        :type username: str
        :param password: The password for the user account.
        :type password: str
        """
        self.username = username
        self.password = password

    def retrieve_login_details(self):
        """
        Retrieve the login details of the user account.

        :return: A dictionary containing the username and password.
        :rtype: dict
        """
        return {'username': self.username, 'password': self.password}

    def change_username(self, new_username):
        """
        Change the username of the user account.

        :param new_username: The new username to set.
        :type new_username: str
        """
        self.username = new_username

    def change_password(self, new_password):
        """
        Change the password of the user account.

        :param new_password: The new password to set.
        :type new_password: str
        """
        self.password = new_password

    def delete_username(self):
        """Delete the username of the user account."""
        self.username = None

    def delete_password(self):
        """Delete the password of the user account."""
        self.password = None

    def is_valid_username(self):
        """
        Check if the username is valid.

        Username must be at least 3 characters long and contain only alphanumeric characters.

        :return: True if the username is valid, False otherwise.
        :rtype: bool
        """
        warnings.warn("The is_valid_username method is deprecated and will be removed in a future release.", DeprecationWarning)
        return len(self.username) >= 3 and self.username.isalnum()
