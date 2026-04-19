def shutdown(user_input):
    if user_input == "Yes":
        return "shutting down"
    elif user_input == "no":
        return "abort shut down"
    else:
        return "sorry"


user_text = input("Enter Yes or no: ")
print(shutdown(user_text))
