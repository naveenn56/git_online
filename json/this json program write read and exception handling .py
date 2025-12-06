import json
def whole():

    choose = input("Save(S) or Read(R): ").upper()

    # ---------- SAVE ----------
    if choose == "S":
        platform = input("Enter platform name to save = ").upper()
        user = input("Username: ")
        password = input("Password: ")

        data = {user: password}

        with open(f"{platform}.json", "w") as file:
            json.dump(data, file, indent=4)
            print("Successfully saved ✔")

    # ---------- READ ----------
    elif choose == "R":
        platform = input("Which platform detail you want = ").upper()
        try:
            with open(f"{platform}.json", "r") as file:
                data = json.load(file)
                print("Saved details =", data)
        except:
            print("❌ File not found — check spelling")

    else:
        print("❌ Invalid choice")
        whole()


whole()


