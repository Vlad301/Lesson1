with open("text.txt", "w") as s:
    while True:
        go = input("Text me: ")
        s.writelines(go + "\n")
        if not go:
            break
s = open("text.txt", "r")
k = s.readlines()
print(k)
s.close()





