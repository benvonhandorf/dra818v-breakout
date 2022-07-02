import serial

serial = serial.Serial('/dev/ttyUSB2', timeout=1)

def command(cmd):
  serial.write(cmd + b'\r\n')
  result = serial.read(100)
  print(f"{cmd} => {result}")


command(b'AT+DMOCONNECT')
command(b'AT+DMOSETGROUP=1,147.4900,147.4900,0000,8,0000')
command(b'S+147.4900')
