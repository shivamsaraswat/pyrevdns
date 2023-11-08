import queue
import threading
import dns.resolver
import dns.exception


class Pyrevdns:

    def __init__(self) -> None:
        pass


    @staticmethod
    def lookup(ip_address:str, resolver_ip:str='8.8.8.8', only_domain:bool=False, output_file:str='') -> None:
        """
        This function performs a reverse DNS lookup on the specified IP address using the specified DNS resolver.

        :param ip_address: IP address to perform a reverse DNS lookup on
        :type ip_address: str
        :param resolver_ip: IP address of the DNS resolver to use for lookups
        :type resolver_ip: str
        :param only_domain: Whether or not to output only the domain
        :type only_domain: bool
        :param output_file: File to write the output to
        :type output_file: str

        :return: None
        :rtype: None
        """

        resolver = dns.resolver.Resolver()
        resolver.nameservers = [resolver_ip]

        try:
            dns.resolver.Cache.flush(dns.resolver.Cache())
            my_resolver = dns.resolver.Resolver()
            address = my_resolver.resolve_address(ip_address)
            strip_address = str(address[0]).rstrip('.')

            if not only_domain:
                output = f"{ip_address}\t{strip_address}"

                if output_file:
                    with open(output_file, 'a') as f:
                        f.write(output + '\n')

                return output

            else:
                output = strip_address

                if output_file:
                    with open(output_file, 'a') as f:
                        f.write(output + '\n')

                return output

        except dns.resolver.NoAnswer:
            return "No PTR record found"

        except dns.resolver.Timeout:
            return "DNS resolution timeout"

        except dns.exception.DNSException as e:
            return f"Unable to resolve {ip_address} [DNS Exception: {e}]"


    @classmethod
    def do_dns_lookup(self, single_ip:str, ip_list:list='', resolver_ip:str='8.8.8.8', only_domain:bool=False, number_of_threads:int=2, output_file:str='') -> None:
        """
        This function performs calls the lookup function for each IP address or IP addresses in the specified file.

        :param single_ip: IP address to perform a reverse DNS lookup on
        :type single_ip: str
        :param ip_list: File containing IP addresses to perform a reverse DNS lookup on
        :type ip_list: str
        :param resolver_ip: IP address of the DNS resolver to use for lookups
        :type resolver_ip: str
        :param only_domain: Whether or not to output only the domain
        :type only_domain: bool
        :param number_of_threads: Number of threads to use
        :type number_of_threads: int
        :param output_file: File to write the output to
        :type output_file: str

        :return: None
        :rtype: None
        """

        q = queue.Queue()

        if single_ip:
            q.put(single_ip)
        elif ip_list:
            try:
                with open(ip_list, 'r') as f:
                    for ip in f:
                        q.put(ip.rstrip('\n'))
            except FileNotFoundError:
                print(f"Unable to open {ip_list}")

        def worker():
            while True:
                ip = q.get()
                if ip is None:
                    break
                print(self.lookup(ip, resolver_ip, only_domain, output_file))
                q.task_done()

        threads = []
        for _ in range(number_of_threads):  # Define the number of worker threads here
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)

        q.join()  # Wait for all tasks to be completed

        # Stop workers
        for _ in range(number_of_threads):
            q.put(None)

        for t in threads:
            t.join()
