# https://adventofcode.com/2021/day/16


hexDict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def decodeRecursive(binStr):
    print("String: ", binStr)
    versions = 0

    version = int(binStr[0:3],2) # first 3 bits
    print("version:", version)
    versions += version

    packetTypeId = int(binStr[3:6],2) # second 3 bits
    print("packet type id:", packetTypeId)

    if packetTypeId == 4:
        literalValue = ""
        for i in range(6, len(binStr)-1, 5):
            group = binStr[i:i+5]
            literalValue += group[1:]
            if group[0] == '0':
                break
        print(literalValue)
        print('literal value: ', int(literalValue,2))
    else:
        # op type
        lengthTypeId = int(binStr[6])
        print("length type id:", lengthTypeId)

        length = 0
        if lengthTypeId == 0:            
            length = int(binStr[7:22],2)
            print("length sub packets:", length)

            #subpackets, 11 and 16
            print(binStr[22:22+11])
            packet1 = binStr[22:22+11] # packet A
            print(binStr[33:33+length-11])
            packet2 = binStr[33:33+length-11] # packet B

            if packet1:
                versions += decodeRecursive(packet1)
            if packet2:
                versions += decodeRecursive(packet2)
        else:
            num = int(binStr[7:18],2) # 11 bits num of sub packets
            print("num sub packets:", num)

            # ignore trailing zeros
            subpacketLen = len(binStr[18:].rstrip('0')) // num
            print("subpacket length: ", subpacketLen)

            if subpacketLen == 0:
                return 0

            print("subpackets:")
            subpackets =[]

            for i in range(0,num):
                print(binStr[18+i*subpacketLen: 18+i*subpacketLen + subpacketLen], int(binStr[18+i*11: 18*i+subpacketLen + subpacketLen], 2))
                subpackets.append(binStr[18+i*subpacketLen: 18+i*subpacketLen + subpacketLen])

            for p in subpackets:
                versions += decodeRecursive(p)
    
    return versions




def decode(str):
    pos = 0

    print("String: ", str)
    binStr = "".join(hexDict[s] for s in str)
    print(binStr)

    sumVersions = 0
    
    while int(binStr[pos:],2) != 0:
        version = int(binStr[pos:pos+3],2) # first 3 bits
        sumVersions += version
        print("version:", version)
        pos += 3

        packetTypeId = int(binStr[pos:pos+3],2) # second 3 bits
        print("packet type id:", packetTypeId)
        pos += 3

        if packetTypeId == 4:
            packet = ''
            end = False
            for i in range(pos, len(binStr)-1, 5):
                group = binStr[i:i+5]
                packet += group[1:]
                pos += 5
                if group[0] == '0':
                    end = True
                    break
            if end:
                break

            print("packet:", packet)
        else:
            # op type
            lengthTypeId = int(binStr[pos])
            pos += 1
            print("length type id:", lengthTypeId)

            length = 0
            if lengthTypeId == 0:
                packet = ''
                print("length sub packets:", int(binStr[pos:pos+15],2))
                length = int(binStr[pos:pos+15],2)
                pos += 15

                #subpackets
                packet = binStr[pos:pos+length]
                print("sub packet:", binStr[pos:pos+length])
                pos += length

            else: # 1 - #num of subpackets 11 bits
                packet = ''
                print("num sub packets:", binStr[pos:pos+11])
                num = int(binStr[pos:pos+11],2)
                pos += 11

                # ignore trailing zeros
                subpacketLen = len(binStr[pos:].rstrip('0')) // num
                print("subpacket length: ", subpacketLen)

                print("subpackets:")
                
                for i in range(0,num):
                    print(binStr[pos: pos+subpacketLen], int(binStr[pos: pos+subpacketLen], 2))
                    packet += binStr[pos: pos+subpacketLen]
                    pos += subpacketLen

        print('endpos: ', pos)
        
        # if int(binStr[pos:],2) == 0: # extra zeros at end
        #     print('end of packet')
        #     break
        
        binStr = packet
        print(binStr)
        pos = 0
        

    print(sumVersions)
    return sumVersions

def part1():
    # inputStr = "D2FE28"
    # binStr = "".join(hexDict[s] for s in inputStr)
    # decodeRecursive(binStr)

    # inputStr = "38006F45291200"
    # binStr = "".join(hexDict[s] for s in inputStr)
    # decodeRecursive(binStr)

    # inputStr = "EE00D40C823060"
    # binStr = "".join(hexDict[s] for s in inputStr)
    # decodeRecursive(binStr)

    # inputStr = "8A004A801A8002F478"
    # binStr = "".join(hexDict[s] for s in inputStr)
    # sumVersions = decodeRecursive(binStr)
    # print("sum versions: ", sumVersions)
    
    inputStr = "620080001611562C8802118E34"
    binStr = "".join(hexDict[s] for s in inputStr)
    sumVersions = decodeRecursive(binStr)
    print("sum versions: ", sumVersions)
    

part1()