# Coding Username & Password Verification, Team checker, and List of Players 
from pyscript import display, document #type:ignore 
#  Coding Username and Password verification 
def account_authenticator(e):
    # Clear previous output 
    document.getElementById('output').innerHTML = ''
    
    # Get values
    uname = document.getElementById('input1').value
    pword = document.getElementById('input2').value

    # Nested Ifelse

    if len(uname) >= 7: 
        display(f"Your username, {uname}, has been authenticated!", target ="output")  # If username passes all requirements this will display 
    else: 
        display(f'Your username must have seven characters or more', target='output')  # Checking for username length

# Checking for letetrs within the password
    if len(pword) >= 10:
        if not pword.isalpha():
            if pword.isdigit():
                display(f"Your password must contain letters and numbers.", target='output')
            # If all passwords checks pass, this will display
            else:
                display(f'Your password has been authenticated!', target='output')
        # Checking for numbers within password
        elif pword.isalpha():
            display(f'Your password must contain letters and numbers. Try Again', target='output')
    # Checking for password length
    elif not len(pword) >= 10:
        display(f'Your password must have a minimum of 10 characaters. Try again', target="output")
   
    # Checking if username and password passses all checks 

    has_letter = False
    has_number = False
  # Looping all requirements together
    for char in pword:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True
            

    if len(uname) >= 7 and len(pword) >= 10 and has_letter == True and has_number == True:
        display(f'Username and Password passes all required checks! Account has been authenticated.', target='output')  # If username and password pass all required checks this will display 
    else:
        display(f'Username or Password does not pass all required checks.', target='output')  # If username and password are missing one requirement this will display 

# Creating team checker 
def intrams_form(e):
    document.getElementById("output").innerHTML = ""
    is_registered = document.getElementById("reg_Yes").checked
    is_medical = document.getElementById("cer_Yes").checked

    grade = int(document.getElementById("gradelvl").value)


    if is_registered == False:
        display("Please fill out the form.", target="output")

    elif is_medical == False:
        display("Please verify your medical certificate.", target="output")
    
    else:
        if grade == 7:
            team = "Blue Bears"
        elif grade == 8:
            team = "Red Bulldogs"
        elif grade == 9:
            team = "Yellow Tigers"
        else:
            team = "Green Hornets"

        display("Your intramurals team is " + team, target="output")



# Creating player list and linking button to function 
def player_list(e): 
    document.getElementById('output').innerHTML = ''  # Clear previous output 
    players = ['Abdullah', 'Abeleda', 'Arce', 'Arias', 'Bonzon', 'Cajucom', 'Catimbang', 'Cotioco', 'Choi', 'Daradal', 'Enriquez', 'Escobar', 'Espina', 'Gano', 'Garcia', 'Kaur', 'Ong', 'Rufo', 'Sanchez', 'Santos', 'Tan', 'Vilale', 'Yao', 'Zosa'
]

    for player in players:
        display(f'{player}', target='output')  # Looping the list to dislay when clicked 