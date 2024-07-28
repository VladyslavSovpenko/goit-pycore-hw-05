from functools import wraps

import task_four.bot.exceptions as exceptions


def operations_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Contact name already exist.")
        except KeyError:
            print("Contact name does not exist.")
        except IndexError:
            print("Exactly 1 argument (name) is required.")
        except exceptions.ContactNameAlreadyExist:
            print("Contact name already exist.")

    return inner


def command_decorator(func):
    @wraps(func)
    def inner(command, *args, **kwargs):
        if (0 < len(args[0]) < 3 and (command in ["add", "change"]) or
                (command == "phone" and len(args[0]) == 1) or
                (len(args[0]) == 0 and command in ["hello", "all", "close", "exit"])):
            return func(command, *args, **kwargs)
        else:
            print("Wrong number of arguments.")
            return None

    return inner
