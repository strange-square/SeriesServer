import requests
import argparse
import func as f

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 8000

def create_main_parser():
    parser = argparse.ArgumentParser(description='This is a service for tracking TV shows.')
    parser.add_argument('--host', default=DEFAULT_HOST)
    parser.add_argument('--port', default=DEFAULT_PORT, type=int)

    return parser

def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()

    while True:
        try:
            cmd = input('Enter command (or "help")>\n')
            if cmd == 'add series':
                f.add_series(main_args)
            elif cmd == 'add series to watched':
                f.add_to_watched(main_args)
            elif cmd == 'add series to to-see list':
                f.add_to_see(main_args)

            elif cmd == 'get episode':
                f.get_episode(main_args)
            elif cmd == 'set episode':
                f.set_episode(main_args)
            elif cmd == 'get raiting':
                f.get_raiting(main_args)
            elif cmd == 'set raiting':
                f.set_raiting(main_args)

            elif cmd == 'generate serias':
                f.gen_serias(main_args)
            elif cmd == 'series watched':
                f.get_watched(main_args)
            elif cmd == 'series to to-see list':
                f.get_to_see(main_args)

            elif cmd =='help':
                f.help()
            elif cmd == 'exit':
                f.graceful_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt:
            f.graceful_exit()


if __name__ == '__main__':
    main()
