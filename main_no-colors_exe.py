"""
Code by hhamzaa#9803
join the discord  https://discord.gg/PMk4DstVka
"""

import subprocess



# run the netsh wlan show profiles command which gets the saved network profiles and save the output in a variable
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# create a list to store the wifi profiles
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# loop through the profiles and print them
for name in profiles:
    # run the netsh wlan show profile command for each profile to get the password
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
    # save the password after the : in the results 
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # try to print the password ( if there isnt one then print nothing )
    try:
        print ("{:<30}|  {:<}".format(name, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(name, ""))

# wait for the user to press q to close or e to save
inn = input("Press q to close or e to save the passwords to a file: ")

# if the user presses e
if inn == "e":
    # open a file to save the passwords
     code
        # loop through the profiles and write them to the file
       code
            # same code as above
           code
            # try to write the password to the file
         code
    # close the file
  code


# if the user presses q
if inn == "q":
    # exit the script
    print("Closing")
    exit()
