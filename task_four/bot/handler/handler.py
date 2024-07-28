from collections import namedtuple

from task_four.bot.decorator.decorators import operations_decorator, command_decorator
from task_four.bot.exceptions.exceptions import ContactNameAlreadyExist

contacts = {}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@command_decorator
def handle_command(command, args):
    if command in operations:
        record = create_record(args, command)
        if record is None:
            return
        apply_operation(operations[command], record)
    else:
        print("Invalid command.")


def create_record(args, command):
    if len(args) == 2 and command not in {"all", "phone"}:
        Record = namedtuple("Record", ["name", "phone"])
        name, phone = args
        record = Record(name, phone)
        return record
    elif len(args) == 1 and command == "phone":
        return args[0]
    elif command in {"all", "hello", "close", "exit"}:
        return True
    else:
        print("Invalid arguments.")
        return None


def apply_operation(command, record):
    command(record)


def greeting(_=None):
    print("How can I help you?")


@operations_decorator
def add_contact(record):
    if record.name not in contacts:
        contacts[record.name] = record.phone
        print(f"Contact with name {record.name} added.")
    else:
        raise ContactNameAlreadyExist


@operations_decorator
def change_phone(record: namedtuple("Record", ["name", "phone"])):
    if record.name in contacts:
        contacts[record.name] = record.phone
        print(f"Contact with name {record.name} updated.")
    else:
        raise KeyError


@operations_decorator
def get_by_name(record):
    if record in contacts:
        print(f"{contacts[record]}")
    else:
        raise KeyError


def get_all_contacts(_=None):
    if len(contacts) > 0:
        for name, phone in contacts.items():
            print(f"name:{name} - phone:{phone}")


def close(_=None):
    print("Good bye!")
    exit()


operations = {
    "hello": greeting,
    "add": add_contact,
    "change": change_phone,
    "phone": get_by_name,
    "all": get_all_contacts,
    "close": close,
    "exit": close
}
