import hashlib

def cracked_Hash(input_password):
    try:
        password_file = open("list.txt", "r")
    except:
        print("Unable to find the file")

    for password in password_file:
        encoded_password = password.encode("utf-8")
        digest = hashlib.md5(encoded_password.strip()).hexdigest()
        if digest == input_password:
            print("Password Found: " + password)

if __name__ == "__main__":
    cracked_Hash("1jksd0sdkmsdfd3")