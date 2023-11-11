# PYrevDNS

PYrevDNS is a simple tool for performing reverse DNS lookups on IP addresses. It can be used to perform lookup on a single IP address
or on a list of IP addresses.

## Installation Through PIP
To install dependencies, use the following command:

```bash
pip3 install -r requirements.txt
```

To import certify as module, install it using the following command:
```bash
pip3 install pyrevdns
```

## Installation with Docker
This tool can also be used with [Docker](https://www.docker.com/). To set up the Docker environment, follow these steps (trying using with sudo, if you get any error):

```bash
docker build -t pyrevdns:latest .
```

OR

Pull directly from [Docker Hub](https://hub.docker.com/r/shivamsaraswat/pyrevdns):

```bash
docker pull shivamsaraswat/pyrevdns:latest
```

## Using the PYrevDNS as command-line tool

To run the PYrevDNS on an IP address, provide the IP address with the -ip flag:

```bash
python3 pyrevdns -ip 216.58.196.110
```

For an overview of all commands use the following command:

```bash
python3 pyrevdns -h
```

The output shown below are the latest supported commands.

```bash
usage: pyrevdns [-h] [-v] [-ip IP] [-l LIST] [-d] [-t THREADS] [-r RESOLVER] [-o OUTPUT] [-sr] [-silent]

PYrevDNS (Reverse DNS lookup tool)

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

INPUT:
  -ip IP                Input IP address
  -l LIST, --list LIST  Input list of IP addresses
  -d, --domain          Output only domains

CONFIGURATION:
  -t THREADS, --threads THREADS
                        Number of threads to use
  -r RESOLVER, --resolver RESOLVER
                        IP of the DNS resolver to use for lookups (default: 8.8.8.8)

OUTPUT:
  -o OUTPUT, --output OUTPUT
                        Output file
  -sr, --success        display only successful results
  -silent               display silent output

Example: python3 pyrevdns -ip 216.58.196.110
```

### Examples

#### Example 1:
Reverse DNS on the IP address 216.58.196.110 with the help of 1.1.1.1 DNS Resolver.

```bash
> python3 pyrevdns -ip 216.58.196.110 -r 1.1.1.1

██████╗ ██╗   ██╗██████╗ ███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ██║   ██║██║  ██║██╔██╗ ██║███████╗
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║  ██║██║╚██╗██║╚════██║
██║        ██║   ██║  ██║███████╗ ╚████╔╝ ██████╔╝██║ ╚████║███████║
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝

     Coded with Love by Shivam Saraswat (@cybersapien)

# 216.58.196.110  maa03s19-in-f110.1e100.net
```

#### Example 2:
Reverse DNS on the list of IP addresses with the help of 1.1.1.1 DNS Resolver.

```bash
> python3 pyrevdns --list test.txt -r 1.1.1.1

██████╗ ██╗   ██╗██████╗ ███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ██║   ██║██║  ██║██╔██╗ ██║███████╗
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║  ██║██║╚██╗██║╚════██║
██║        ██║   ██║  ██║███████╗ ╚████╔╝ ██████╔╝██║ ╚████║███████║
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝

     Coded with Love by Shivam Saraswat (@cybersapien)

# 216.58.196.110  maa03s19-in-f110.1e100.net
# 173.0.84.203    m.paypal.com
# 185.199.109.153 cdn-185-199-109-153.github.com
```

## Using the PYrevDNS as module

### Examples

#### Example 1

```bash
from pyrevdns import Pyrevdns

print(Pyrevdns.lookup('216.58.196.110', only_domain=True))

# maa03s19-in-f110.1e100.net
```

#### Example 2

```bash
from pyrevdns import Pyrevdns

print(Pyrevdns.lookup('216.58.196.110', resolver_ip='1.1.1.1'))

# 216.58.196.110  maa03s19-in-f110.1e100.net
```

## Using the Docker Container

A typical run through Docker would look as follows:

```bash
docker run -it --rm pyrevdns -ip 216.58.196.110
```
