# NOTE: works only in Python < 3.8

import ipaddress


BLACK_LIST = {
    '0.0.0.0',
    '1.2.3.4',
    '10.0.0.4',
}


def send_request(ip):
    try:
        if ip in BLACK_LIST:
            print(f"{ip} is not allowed!")
            return
        ip = str(ipaddress.IPv4Address(ip))
    except ipaddress.AddressValueError:
        print(f"Error at validation: {ip}")
        return
    print(f'https://{ip}')
    print("Request send!")


if __name__ == '__main__':
    valid_ip = '10.11.12.13'
    invalid_ip = '500.500.500.500'
    blacked_ip = '1.2.3.4'
    hacked_ip = '01.02.03.04'

    send_request(valid_ip)
    send_request(invalid_ip)
    send_request(blacked_ip)
    send_request(hacked_ip)
