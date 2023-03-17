def sender(n,datagram):
    print('\n\n\n-----Sender End-----')
    checksum = 0   
    for i in range(1,n):
        checksum = checksum + datagram[i]
    print('Checksum at sender End is',checksum)
    return checksum

def receiver(n,datagram,check):
    print('-----Receiver End-----')
    for i in range(1,n):
        check = check - datagram[i]
    if check != 0:
        print('The packet is collided')
        return False
    else:
        print('Checksum at receiver end is',check)
        return check
        
datagram = []
n = int(input("Enter number of packets: "))
print('Enter:')
for i in range(1,n+1):
    p = int(input('Packet: '))
    datagram.append(p)

check = sender(n,datagram)
print('\n\n\nPacket sending......\n\n\n')
res = receiver(n,datagram,check)
if res == 0:
    print('\n\n\nCommunication is Successful!!!')
