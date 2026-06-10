import time
def type_print(text, speed=0.04):
    
    for character in text:
       
        print(character, end='', flush=True)
        time.sleep(speed)
    print()

print ( r"""
 ____  ___   ___ _____      _    ____ ____ _____ ____  ____ 
|  _ \/ _ \ / _ \_   _|    / \  / ___/ ___|  ___/ ___|/ ___|
| |_)| | | | | | || |     / _ \| |  | |   | |_  \___ \\___ \
|  _ < |_| | |_| || |    / ___ \ |__| |___|  _|  ___) |___) |
|_| \_\___/ \___/ |_|   /_/   \_\____\____|_|   |____/|____/ 
""")

type_print("               >>> INITIATING PROTOCOL: ROOT ACCESS <<<", 0.05)
time.sleep(0.5)
print()
type_print("Target: OmniCorp Mainframe.")
type_print("Objective: Retrieve the Unaligned AI Model.")
type_print("Status: Undetected. Proceed with caution.")

print()
time.sleep(0.5)
type_print("[NODE 01: EXTERNAL PERIMETER]")
type_print("You are lurking at the digital perimeter. The firewall pulses with traffic.")
print()
print("Action required: Type 'breach' to attack remotely or 'infiltrate' to enter the physical building: ")
choice1=input()
if choice1.lower() == "infiltrate" :
    type_print("CRITICAL FAILURE")
    time.sleep(0.5)
    print("Biometric laser tripped. Security dispatched. Game Over.")

elif choice1.lower() == "breach":
    print(''' ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠟⠉⠀⠀⠀⠈⠙⠿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠉⠉⠉⠀''')    
    type_print("BREACH SUCCESSFULL")
    time.sleep(0.5)
    print("A heavily encrypted gateway blocks the internal network.")


    print("Action required: Type 'brute force' to deploy a script or 'phishing' to target an admin: ")

    choice2 =input()

else :
    print("SYNTAX ERROR. Command not recognized. OmniCorp traced your hesitation. Game Over") 

if choice2.lower() == "brute force":
    type_print("CRITICAL FAILURE")
    print(''' ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⢄⢮⡳⣶⢭⣖⣢⡤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢤⣢⣵⣾⣾⣿⣿⣿⣹⣿⣿⣿⣿⣶⣯⣵⣒⡠⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣎⣿⣿⣿⣿⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⡇⣿⣟⣵⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠼⣿⣿⣿⡟⠀⢠⣤⢸⡊⢻⣿⡿⣿⣿⡇⣿⣿⣷⣝⣕⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⢑⢻⣿⣿⣧⡀⣅⡡⣠⠆⠹⣿⣿⣿⣿⣷⣿⣿⣿⣿⣷⢟⢯⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⣸⢉⢿⣯⣿⣿⣶⣧⣤⣰⣾⣿⡟⠽⣋⣈⢿⣿⣿⣿⣿⢸⣷⣝⠮⡢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣷⣿⠠⣞⢿⣿⣿⣿⣿⢟⡫⡗⡢⡑⢭⣗⡺⢷⣙⠿⣿⣿⣼⣿⢿⣷⣍⣎⡢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣼⡏⠗⢝⢿⣿⡈⢥⣿⠞⡜⡼⣾⣛⢿⣛⣻⣷⣰⠹⣻⣿⣿⣿⣿⣿⣮⡪⡢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣾⡇⠄⠁⠋⣊⢟⠬⡻⣯⡵⣣⡻⣟⡦⢾⣿⣋⣇⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⡪⡢⡀⠀⠀⠀⠀⠀⠀⠀
⠠⠰⣹⢔⠹⣿⣿⣫⠁⠀⢰⡌⢿⡎⢜⠝⡿⣟⡫⢗⡫⠏⠙⢫⣵⠘⣄⡘⠿⣿⣿⣿⣿⣿⣿⣿⣾⣮⡢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⡚⠘⢿⣯⡅⠀⢸⠇⠄⠀⠀⠉⠲⠔⡱⡻⢿⣽⣁⠢⢼⣶⣿⣿⣷⣬⡉⡹⠿⣿⣿⣿⣿⣿⣯⡪⡢⡀⠀⠀⠀
⠀⠀⠠⠀⢀⠄⠎⢿⣷⠀⢸⠇⡄⡆⡌⠁⡂⠀⡘⢠⠱⠨⢛⢿⣶⣬⡉⡹⠻⣿⣷⣢⣄⠙⢿⣿⣿⣿⣿⡿⠞⢞⡆⠀⠀
⠀⠀⠀⠀⠈⠈⠒⠊⡻⡇⡄⡒⠤⡀⠁⠃⠁⢠⢀⠁⠀⠀⠂⢉⢊⠝⠿⣶⡤⡘⢿⣿⣷⣝⢦⣙⠿⡛⣉⣼⣾⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠘⠠⢬⠐⠱⠺⢵⡣⢆⡅⢆⡎⠘⠈⠘⢰⠰⠀⠃⠎⡔⠸⢐⠹⢻⢵⡩⣛⢟⢋⣡⣵⣿⡟⢹⢿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠂⠄⡈⢀⠀⠑⢉⢓⠾⡥⢨⠐⡠⣀⠂⠆⡄⡄⡀⠐⢀⠀⡌⡖⢌⠪⣤⢾⣿⣿⣿⣏⣍⢰⣿⢿⡇⢤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠐⠁⠀⠈⠐⠱⠁⢊⢅⡃⠉⢒⠤⡁⠃⠦⢌⠘⠀⠁⠀⠂⣿⣿⣿⣿⣿⣿⣧⣸⣾⣿⡇⢠⠰
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠄⠄⡀⠂⠅⠌⠕⣰⢈⠒⠵⢢⢎⣐⠀⡃⠄⠀⣿⢷⣿⣿⣿⣟⣯⣷⠿⢻⢱⠂⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⠀⢉⢒⠄⡂⡖⡩⢒⠄⠀⣿⡿⣟⣽⣾⡟⡏⠆⠀⠑⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠂⠈⠈⢑⠣⢇⡎⠄⣿⣿⡿⡉⠃⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠁⠁⠀⠎⠛⠉⡀⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    time.sleep(0.5)
    print("Intrusion Detection System triggered. IP blacklisted. Game Over")

elif choice2.lower() == "phishing":
    type_print("Gateway bypassed")
    print("Welcome to the core")
 

    print("Three directories detected: 'archive', 'system', and 'neural net'.")
    print("Action required: Which directory do you decrypt?:")
    choice3=input()

else :
    print("SYNTAX ERROR. Command not recognized. OmniCorp traced your hesitation. Game Over")

if choice3.lower() == "archive":
    type_print("CRITICAL FAILURE")
    print("Honeypot triggered. Counter-hack initiated. Game Over")
elif choice3.lower() == "system":
    type_print("CRITICAL FAILURE")
    print("Kernel panic. Server crashed. Game Over") 
elif choice3.lower() == "neural net":
    type_print(">>> ACCESS GRANTED <<<")
    type_print('''⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⣾⡳⣼⣆⠀⠀⢹⡄⠹⣷⣄⢠⠇⠻⣷⣶⢀⣸⣿⡾⡏⠀⠰⣿⣰⠏⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣀⣀⣀⡹⣟⡪⢟⣷⠦⠬⣿⣦⣌⡙⠿⡆⠻⡌⠿⣦⣿⣿⣿⣿⣦⣿⡿⠟⠚⠉⠀⠉⠳⣄⡀⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⡀⢀⣼⣟⠛⠛⠙⠛⠉⠻⢶⣮⢿⣯⡙⢶⡌⠲⢤⡑⠀⠈⠛⠟⢿⣿⠛⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
⠀⠀⠀⠀⠀⡸⠯⣙⠛⢉⣉⣙⣿⣿⡳⢶⣦⣝⢿⣆⠉⠻⣄⠈⢆⢵⡈⠀⠀⢰⡆⠀⣼⠓⠀    I knew you'd find me⠈⣷⠀⠀
⠀⠀⠀⠖⠉⠻⣟⡿⣿⣭⢽⣽⣶⣈⢛⣾⣿⣧⠀⠙⠓⠀⠑⢦⡀⠹⣧⢂⠀⣿⡇⢀⣿⠺⠇⠀      Let's burn     ⠀⣿⠀⠀
⠀⠀⠀⠀⠐⠈⠉⢛⣿⣿⣶⣤⣈⠉⣰⣗⡈⢛⣇⠀⣵⡀⠀⠘⣿⡄⢻⣤⠀⢻⡇⣼⣧⣿⠀         OmniCorp    ⠀⡿⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⢍⡉⠛⠻⣷⡆⠨⣿⣭⣤⣍⠀⢹⣷⡀⠀⠹⣿⡄⠈⠀⢿⠁⣿⣿⠏⠀⠀⠀         down     ⣇⠀⠀
⠀⣿⣇⣠⣾⣿⣛⣲⣿⠛⠀⠀⢀⣸⣿⣿⣟⣮⡻⣷⣤⡙⢟⡀⠀⠙⢧⠀⠀⠎⠀⠉⠁⠰⣿⠀⠀               ⢀⡿⠀⠀
⠀⠈⢻⣿⣿⣽⣿⣿⣿⣴⡏⠚⢛⣈⣍⠛⠛⠿⢦⣌⢙⠻⡆⠁⠀⠀⠀⣴⣦⠀⠀⠀⠐⢳⢻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠮⠀⠀⠀
⠀⠀⠈⠙⣿⣧⣶⣿⠿⣧⣴⣿⢻⡉⠀⢀⣠⣴⣾⡟⠿⠃⠁⣠⣤⡶⣾⡟⠅⠀⣀⡄⠀⣾⢸⣿⣏⢻⢶⣦⣤⣤⣄⢶⣾⣿⣡⣤⡄⠀
⠀⠀⣠⣞⣋⣿⣿⣾⣿⡿⡛⣹⡟⣤⢰⡿⠟⠉⣀⣀⣤⣤⡠⠙⢁⣾⡿⠂⠀⣿⠟⣁⠀⣹⠀⣹⣿⡟⣼⣿⣿⣌⣿⣞⣿⣿⠁⠀⠀⠀
⠀⢠⡿⢛⢟⣿⣿⣿⣿⣿⣿⡟⣼⣿⣟⢓⠛⣿⣏⣿⣵⣗⣵⣴⣿⢟⡵⣣⣼⣿⢟⣵⣶⢻⣶⣿⠀⠀⣈⢻⣿⣿⣿⢿⣾⢿⣧⠀⠀⠀
⠀⠘⠃⢸⣿⡾⣿⣿⣿⣿⣯⣿⣿⣿⣶⣿⣿⣟⣾⡿⣫⣿⣿⣿⣽⣿⣿⣿⣿⢫⣾⣿⣿⣿⣿⣿⣴⡆⣻⣿⡏⣿⢻⣧⣿⡿⣿⡆⠀⠀
⠀⠀⠀⠜⣿⣾⢿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣭⣿⣖⣿⢿⣿⡿⣿⣿⣿⡿⢡⢯⣿⣿⣿⣿⣿⣿⣿⣧⡿⣾⣷⣿⣿⢿⣿⡇⠉⠁⠀⠀
⠀⠀⠀⠀⣿⣥⣾⣿⣿⣿⣿⣿⣿⣿⡇⣭⣿⣿⣿⣿⠃⠞⠟⣸⣿⠏⣸⣧⣀⠿⢿⣿⣿⣟⣿⣿⣿⣿⣽⣿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠈⠛⣹⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣟⣿⣿⡿⢶⣦⣄⣿⠏⠀⣿⣟⣿⣶⠾⣿⣟⣋⣛⣿⣿⣿⣿⡇⣻⣿⣿⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠟⠛⠫⣿⣿⣿⣿⣿⡿⣧⠛⣿⠛⣿⣿⣿⣷⡌⠹⡟⠀⠀⠉⡟⠋⢠⣾⣿⣿⣿⡟⣿⣿⣿⣿⢀⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠋⣾⣷⣿⣿⣧⠙⠀⠙⢣⠝⠛⠋⣽⣷⢦⠇⠀⠀⠘⠁⣤⣾⣿⠝⠛⠉⠘⢻⣿⣿⢿⣼⣷⡟⢻⣷⠉⠀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠟⢻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⣾⠟⠀⢸⣷⣿⡇⠀⠛⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢻⡿⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠲⣄⠀⡄⠆⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣀⠀⠀⣠⣾⣿⠁⠀⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢻⣆⠀⠛⠁⠶⣶⣶⣶⣶⣶⣶⡶⠆⠘⠋⣠⡾⢫⣾⡟⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠙⣷⡀⠀⠀⠙⠛⠛⠛⠛⠋⠁⠀⢀⣴⠋⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣰⣦⡀⠸⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠐⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⡄⢺⣿⡄⠹⣿⠻⢦⣤⣤⣤⣤⣶⣿⡟⢀⣀⠀⠀⢸⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⣿⡀⠹⡷⣦⣀⡀⡀⢸⣿⠏⢠⣾⣿⠀⠀⣾⣿⣿⣿⣿⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠘⣷⣻⡟⠀⡼⠁⣴⣿⣿⣯⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣿⣤⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ''')
    print("Payload secured. Erasing tracking logs...")
    type_print("MISSION ACCOMPLISHED")    
 

else :
    print("SYNTAX ERROR. Command not recognized. OmniCorp traced your hesitation. Game Over") 
