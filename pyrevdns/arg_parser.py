import argparse


def parse_arguments() -> argparse.Namespace:
    """
    This function parses the command line arguments.

    :return: The parsed command line arguments
    :rtype: argparse.Namespace
    """

    parser = argparse.ArgumentParser(prog='pyrevdns', description='PYrevDNS (Reverse DNS lookup tool)', epilog='Example: python3 pyrevdns -ip 216.58.196.110')
    parser.add_argument('-v', '--version', action='version', version='Current version: v1.0')

    group1 = parser.add_argument_group('INPUT')
    group1.add_argument('-ip', help='Input IP address')
    group1.add_argument('-l', '--list', help='Input list of IP addresses')
    group1.add_argument('-d', '--domain', action='store_true', help='Output only domains')

    group2 = parser.add_argument_group('CONFIGURATION')
    group2.add_argument('-t', '--threads', default=8, type=int, help='Number of threads to use')
    group2.add_argument('-r', '--resolver', default='8.8.8.8', type=str, help='IP of the DNS resolver to use for lookups (default: 8.8.8.8)')

    group3 = parser.add_argument_group('OUTPUT')
    group3.add_argument('-o', '--output', help='Output file')
    group3.add_argument('-silent', action='store_true', help='display silent output')

    args = parser.parse_args()

    return args
