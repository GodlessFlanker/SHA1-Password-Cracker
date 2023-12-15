import hashlib


def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()

    return digest

def main():
    try:
        user_sha1 = input("Enter the SHA1 to Crack: ")
        cleaned_user_sha1 = user_sha1.strip().lower()

        if not cleaned_user_sha1.isalnum():
            raise ValueError("SHA1 hash should only contain alphanumeric characters")

        with open('./passwords.txt') as f:
            for line in f:
                password = line.strip()
                converted_sha1 = convert_text_to_sha1(password)

                if cleaned_user_sha1 == converted_sha1:
                    print(f"Password Found: {password}")
                    return 
    
        print("Could not find the password")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()