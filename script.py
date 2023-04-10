import requests


class MyUser:
    def __init__(self, id, email, username, name):
        # Constructor for the MyUser class
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        # String representation for the MyUser object
        return f"User: id={self.id}, email={self.email}, username={self.username}, name={self.name}"


def find_user_by_name(name):
    # Function to find a user by name using data from a website
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = response.json()

    # Loop through the users data to find a user with the given name
    for user_data in users_data:
        if user_data['name'] == name:
            # If a user with the given name is found, create a MyUser object with the user's data and return it
            return MyUser(user_data['id'], user_data['email'], user_data['username'], user_data['name'])

    # If no user with the given name is found, return a message indicating that the user was not found.
    return "User not found."


user_name = input("Enter a user name: ")
user = find_user_by_name(user_name)
print(user)
