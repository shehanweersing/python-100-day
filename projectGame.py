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
type_print()