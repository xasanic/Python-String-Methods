file = input("file ; ") 

mail = file.endswith(".txt") or file.endswith(".docx") or file.endswith("pdf")

print(mail)