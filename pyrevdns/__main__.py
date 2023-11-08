import pyrevdns
from termcolor import colored
from arg_parser import parse_arguments


def logo() -> None:
    print(colored("""
██████╗ ██╗   ██╗██████╗ ███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ██║   ██║██║  ██║██╔██╗ ██║███████╗
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║  ██║██║╚██╗██║╚════██║
██║        ██║   ██║  ██║███████╗ ╚████╔╝ ██████╔╝██║ ╚████║███████║
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
    """))
    print(colored('     Coded with Love by Shivam Saraswat (@cybersapien)\n', 'green', attrs=['bold']))


def main():
    args = parse_arguments()

    if not args.silent:
        logo()

    pyrevdns_object = pyrevdns.Pyrevdns()
    pyrevdns_object.do_dns_lookup(args.ip, args.list, args.resolver, args.domain, args.threads, args.output)


if __name__ == '__main__':
    main()
