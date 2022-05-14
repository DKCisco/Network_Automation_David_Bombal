from datetime import datetime
from unittest import result
from scrapli.driver.core import IOSXEDriver

my_time = datetime.now().strftime("%H:%M:%S")

command_to_send = input("Enter the command you wish to send: ")

MY_DEVICE = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username" : "developer",
    "auth_password" : "C1sco12345",
    "port" : 22,
    "auth_strict_key" : False,
    "transport_options": {"open_cmd": ["-o", "KexAlgorithms=+diffie-hellman-group14-sha1"]}
}

with IOSXEDriver(**MY_DEVICE) as conn:
    result = conn.send_command(command_to_send)

my_list = (result.result.splitlines())

with open(f"{command_to_send}-{my_time}.txt", "x") as f:
    for line in my_list:
        f.write(line + "\n")