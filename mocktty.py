import os
import pty
import serial
import codecs
import binascii
import threading as mt

def main():
    master, slave = pty.openpty()
    s_name = os.ttyname(slave)

    print('mock serial port: {}'.format(s_name))

    ser = serial.Serial(s_name)

    def fix_escape(s):
        return codecs.decode(s, 'unicode_escape')

    def to_bytes(s):
        return s.encode('ISO-8859-1')

    def reader_func():
        while True:
            r = os.read(master, 256)

            if (len(r)):
                print('Bytes received: {}'.format(binascii.hexlify(r)))

    reader_thread = mt.Thread(target=reader_func)
    reader_thread.start()

    while True:
        msg = input()
        bytes_to_send = to_bytes(fix_escape(msg))
        os.write(master, bytes_to_send)

if __name__ == '__main__':
    main()
