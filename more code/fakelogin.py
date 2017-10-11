name = input("Who are you? ").lower()

authorized_users = ['rachael', 'justin', 'jason', 'arthur', 'gio', 'michael']

def login_function(user):
    print(f"If this were real, I'd log in {user}")

while True:
    if name in authorized_users:
        login_function(name)
        break
    else:
        print("You are not logged in as an authorized user. Please log in or sign up")
        name = input("Who are you? ").lower()