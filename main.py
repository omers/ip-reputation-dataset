import requests
import csv
from loguru import logger

url = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"

class IPReputation:
    
    def __init__(self, url: str):
        self.url = url    
    
    def get_proofpoint_ip_reputation(self, url: str):
        logger.info(f"Getting IP reputation from {url}")
        response = requests.get(url)
        lines = response.text.split('\n')
        # Filter out lines that start with '#' and empty lines
        filtered_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
        return filtered_lines

    def save_to_csv(self, ips, filename: str):
        logger.info(f"Saving IP reputation to {filename}")
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for ip in ips:
                writer.writerow([ip, 1])

if __name__ == "__main__":
    ip_reputation = IPReputation(url)
    ips = ip_reputation.get_proofpoint_ip_reputation(url)
    ip_reputation.save_to_csv(ips, 'proofpoint_ip_reputation.csv')
