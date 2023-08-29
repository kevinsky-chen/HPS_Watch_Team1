import utime as time
from machine import Pin, UART
from MyKit_GC9A01 import myGC9A01, color # 自製的顯示模組
DEBUG = False

WHITE = color('white')
BLACK = color('black')
RED = color('red')
    
def tick(timer):
    global led
    led.toggle()

# show圖
def showImage(filePath, x, y):
    display.load_microBMP(filePath, x, y)
    display.show()
    #time.sleep(1)

# show字: 因為能顯示的圖片太小，所以需以字輔助
def showText(text, x=100, y_up=50, y_down=140):
    textList = text.split()

    # only shows the first two images
    display.write_text(textList[0], x, y_up, 2, RED) # first line
    if(len(textList)>1): display.write_text(textList[1],x,y_down,3,BLACK) # second line

    display.show()
    #time.sleep(0.05)
    #showColor("white")

# show背景色: 單一色，類似refresh 
def showColor(i):
    if i=='white':
        display.fill(WHITE)
    elif i=='black':
        display.fill(BLACK)
    else:
        display.fill(RED)

    display.show()
    #time.sleep(1)

#def BTselection():

#main
if __name__=='__main__':
    #device definition
    vibrator = Pin(28, Pin.OUT)
    uart = UART(0,38400, tx=Pin(16), rx=Pin(17))  # 藍芽傳訊:TX pin接GPIO16, RX pin接GPIO17
    uart.init(38400)    # 藍芽傳訊: 設定初始 baud rate
    #tim = Timer()
    display = myGC9A01()  # Display chip
    #led = Pin(LED_GPx, Pin.OUT)
    data = ""
    isActive = True      # Display on(True)/off(False)
    #tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
    
    # read files
    #img_list = []
    x_middle = 100
    y_middle = 100
    y_up = 50
    y_down = 140
    BMP_W = 40
    BMP_H = 40  # size
    mypath = "/images/"  #圖檔的位置

    #showColor("black") 
    showImage(mypath + "UI.bmp", x_middle, y_middle)  # reset畫面

    while True:
        if uart.any():
            time.sleep(0.01)
            data = uart.readline().strip()
            #print(data)
            #display.fill(WHITE)
            #display.clear(x, y, BMP_W, BMP_H, WHITE)
            
            if data== b'x':  #訊號 == x #關掉螢幕(沒在用省電)
                isActive = False
                display.off()
            elif data== b"o":  #訊號 == o #開啟螢幕(初始使用)
                isActive = True
                display.on()
            else:
                if isActive:
                    ### TODO
                    vibrator.value(1)
                    if b'd' in data:  #訊號 == 1 # direction 0~360 degree
                        #showColor("black")
                        showImage(mypath + "direction.bmp", x_middle, y_up) # show圖片: 只能是.bmp format
                        degree = data.split("b")[1]
                        showText(degree)
                        time.sleep(3)   # 震動3s
                        if(DEBUG): print("mode d!")
                    elif data== b'0': #訊號 == 0 # alarm
                        #showColor("red")
                        showImage(mypath + "alarm.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(3)   # 震動3s
                        if(DEBUG): print("mode 0!")
                    elif data== b'1': #訊號 == 3 # call name
                        showColor("white")
                        showImage(mypath + "name.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(1)   # 震動1s
                        
                        if(DEBUG): print("mode 1!")
                    elif data== b'2': #訊號 == 3 # police_car
                        showColor("red")
                        showImage(mypath + "police_car.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(3)   # 震動3s
                        
                        if(DEBUG): print("mode 2!")
                    elif data== b'3': #訊號 == 3 # emergency
                        showColor("red")
                        showImage(mypath + "emergency.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(5)   # 震動5s
                        if(DEBUG): print("mode 1!")
                    elif data== b'4': #訊號 == 3 # ambulence
                        showColor("red")
                        showImage(mypath + "ambulance.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(3)   # 震動3s

                        if(DEBUG): print("mode 4!")
                    elif data== b'5': #訊號 == 5 # plane
                        showColor("white")
                        showImage(mypath + "plane.bmp", x_middle, y_middle) # show圖片: 只能是.bmp format
                        time.sleep(2)   # 震動2s
                        if(DEBUG): print("mode 5!")
                    # else:
                    #     pass # 還有很多case，可以有對應的文字與icon
                    else:
                        print("Error BT signal!")
                    vibrator.value(0)
                                     
                
            # refresh 畫面
            if isActive:
                showColor("white")
                showImage(mypath + "UI.bmp", x_middle, y_middle)  # reset畫面
                time.sleep(0.05)
                showColor("white")

