import re
from collections import Counter

def parse_log_file(filename):
    status_code_count = {200: 0, 404: 0, 500: 0}
    ip_addresses = []
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] ".*" (\d{3}) \d+')

    with open(filename, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip = match.group(1)
                status_code = int(match.group(2))
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                ip_addresses.append(ip)

    return status_code_count, ip_addresses

def write_summary_to_file(filename, status_code_count, common_ips):
    with open(filename, 'w') as file:
        total_requests = sum(status_code_count.values())
        file.write(f"Total requests: {total_requests}\n")
        for code in [200, 404, 500]:
            file.write(f"Requests with status code {code}: {status_code_count[code]}\n")
        file.write("\nThree most common IP addresses:\n")
        for ip, count in common_ips:
            file.write(f"{ip}: {count}\n")

def main():
    log_file = r'C:\Users\5308-2\Desktop\New folder (3)\tt219\server_log.txt'
    output_file = r'C:\Users\5308-2\Desktop\New folder (3)\tt219\log_summary.txt'
    status_code_count, ip_addresses = parse_log_file(log_file)
    ip_counter = Counter(ip_addresses)
    common_ips = ip_counter.most_common(3)
    write_summary_to_file(output_file, status_code_count, common_ips)
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()

import os
import re
from collections import Counter

def parse_log_file(filename):
    status_code_count = {200: 0, 404: 0, 500: 0}
    ip_addresses = []
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] ".*" (\d{3}) \d+')

    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return None, None

    with open(filename, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip = match.group(1)
                status_code = int(match.group(2))
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                ip_addresses.append(ip)

    return status_code_count, ip_addresses

def write_summary_to_file(filename, status_code_count, common_ips):
    with open(filename, 'w') as file:
        total_requests = sum(status_code_count.values())
        file.write(f"Total requests: {total_requests}\n")
        for code in [200, 404, 500]:
            file.write(f"Requests with status code {code}: {status_code_count[code]}\n")
        file.write("\nThree most common IP addresses:\n")
        for ip, count in common_ips:
            file.write(f"{ip}: {count}\n")

def main():
    log_file = r'C:\Users\5308-2\Desktop\New folder (3)\tt219\server_log.txt'
    output_file = r'C:\Users\5308-2\Desktop\New folder (3)\tt219\log_summary.txt'
    status_code_count, ip_addresses = parse_log_file(log_file)

    if status_code_count is None or ip_addresses is None:
        return

    ip_counter = Counter(ip_addresses)
    common_ips = ip_counter.most_common(3)
    write_summary_to_file(output_file, status_code_count, common_ips)
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()