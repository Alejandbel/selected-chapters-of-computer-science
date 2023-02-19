from cli import CLI
from storage_controller import StorageController


def main():
    controller = StorageController()

    cli = CLI()
    cli.add_command('add', controller.add)
    cli.add_command('list', controller.list)
    cli.add_command('remove', controller.remove)
    cli.add_command('find', controller.find)
    cli.add_command('grep', controller.grep)
    
    cli.start_application()


if __name__ == "__main__":
    main()
