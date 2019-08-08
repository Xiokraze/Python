# return a dictionary of the number lines, characters, and words in a file

def statistics(file):
    with open(file) as f:
        lines = f.readlines()   
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }