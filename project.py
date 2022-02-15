import os

ip_list = ['8.8.8.8', '8.8.4.4']

def run():
  for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "recibidos = 4" in response:
      print(f"UP {ip} ping successful")
    else:
      print(f"Down {ip} Ping unsuccessful")

if __name__ == '__main__':
  run()
