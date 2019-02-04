
add_library('serial')


def setup():
    print Serial.list()
    portIndex = 3 
    print "Connecting to", Serial.list()[portIndex]
    global myPort
    myPort = Serial(this, Serial.list()[portIndex], 115200)
    global pixel_buffer
    pixel_buffer = [0 for i in range(64)]


def draw():
    global pixel_buffer

    while myPort.available() >= 130:
        if myPort.read() == 0x55:
            if myPort.read() == 0xaa:
                for i in range(64):
                    lo = myPort.read()
                    hi = myPort.read()
                    temp = (hi << 8) | lo
                    if temp > 200 :#this is to ignore shitty values 
                        break
                    pixel_buffer[i] = temp
                print create2d(pixel_buffer)
                break





def create2d(oned_lst):       
    w, h = 8, 8
    mx = [[1 for x in range(w)] for y in range(h)] 
    
    counter = 0 
    flag = 0 
    for i in range (64):
        if i%8 == 0 and i !=0:
            counter += 1 
            flag = 0 
            
        mx[counter][flag] = oned_lst[i]  
        flag+=1
    return mx

