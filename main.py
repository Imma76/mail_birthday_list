with open('./mail_letter/input/letters/starting_letter.txt', mode='r') as file:
    letter = file.read()
    new_list = letter.split()
    # print(new_list)
    for name in new_list:
        with open('./mail_letter/input/Names/invited_names.txt', mode="r") as files:
            names = files.read()
            names_list = names.split()
            new_list[1] = names_list
    for i in new_list[1]:
        new_list[1] = i
        print(new_list[1])
        message = " ".join(new_list)
        print(message)
        with open(f"./mail_letter/output/ReadyToSend/letter_for_{new_list[1]}.txt", mode="w") as file_letter:
            file_letter.write(message)
