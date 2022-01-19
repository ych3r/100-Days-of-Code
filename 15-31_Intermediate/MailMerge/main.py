with open("Input/Letters/starting_letter.txt") as f:
    letter_content = f.read()

with open("Input/Names/invited_names.txt") as f:
    for name in f.readlines():
        name = name.strip("\n")
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(letter_content.replace("[name]", name))
