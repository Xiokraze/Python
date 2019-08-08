def find_and_replace(file, word, replacement):
    with open(file, "r+") as file:
        text = file.read()
        new_text = text.replace(word, replacement)
        file.seek(0)
        file.write(new_text)
        file.truncate()