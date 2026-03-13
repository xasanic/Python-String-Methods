email = input("Email kiriting: ")

natija = not email.startswith("@") and email.endswith(".com")

print(natija)