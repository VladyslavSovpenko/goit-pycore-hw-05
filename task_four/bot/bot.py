import handler


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = handler.parse_input(user_input)
        handler.handle_command(command, args)


if __name__ == "__main__":
    main()
