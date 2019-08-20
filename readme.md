## Introduction
Mock tty device by using pyserial

## Usage
 - `pip install -r requirements.txt`
 - `python3 mocktty.py`

 console will print the name of created tty device, and then you can 
  - send bytes to client via stdin, e.g. `'\xF0\x00\xF7'`
  - `$ hexdump < <path_of_mock_tty_device>` to get the buffered data in client
  - `$ echo -n -e <bytes> > <path_of_mock_tty_device>` to send bytes to master
  - data sent to master will output via stdout
