with open("C:/Users/AUWAL/Desktop/Harsuna Ai/hausa_word.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")
        word = parts[0]
        meaning = parts[1]
        print(word + " means " + meaning)