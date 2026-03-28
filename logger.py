def log_to_file(data):
    with open("log.txt", "a") as file:
        file.write(data + "\n")