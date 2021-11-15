from dataclasses import dataclass
from typing import List

@dataclass
class Profile:
    Realname: str
    user_name: str
    wordbio: str
    age: str


def create_profile(profiles: List[Profile]) -> None:
    Realname = input("Real Name: ")
    user_name = input("UserName: ")
    wordbio = input("3 word bio: ")
    age = input("Age: ")
    new = Profile(Realname, user_name, wordbio, age)
    profiles.append(new)

def all_accounts(profiles: List[Profile]) -> None:
     for new in profiles:
         print(new.Realname, "-", new.user_name, "-", new.wordbio, "-", new.age)

def change_profile(profiles: List[Profile]) -> None:
        name = input("Real Name: ")
        for profile in profiles:
            if profile.Realname == name:
                user_name = input("UserName: ")
                wordbio = input("3 word bio: ")
                age = input("Age: ")
                profile.user_name = user_name
                profile.wordbio = wordbio
                profile.age = age
                return
        print("That account is not in the system!!")

def delete_account(profiles: List[Profile]) -> None:
    p = 0 
    delete_account = input("Real Name: ")
    for profile in profiles:
        if profile.Realname == delete_account:
            profiles.pop(p)
            return
        else:
            p += 1
    print("That account is not in the system!!")


def main() -> None:
    profiles: List[Profile] = []
    print("Welcome to Snapchat, please make as many profiles that's needed ")
    while True:
        user_input = input("""(create), (all) accounts, (change), (delete) or (quit)
- """)
        if user_input == "create":
            create_profile(profiles)
        elif user_input == "all":
            all_accounts(profiles)
        elif user_input == "change":
            change_profile(profiles)
        elif user_input == "delete":
            delete_account(profiles)
        elif user_input == "quit":
            break
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
