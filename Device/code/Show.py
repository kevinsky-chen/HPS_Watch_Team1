import utime as time
from machine import Pin, UART
from MyKit_GC9A01 import myGC9A01, color # 自製的顯示模組

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
    time.sleep(1)

# show字: 因為能顯示的圖片太小，所以需以字輔助
def showText(text):
    textList = text.split()
    
    print(textList)
    # only shows the first two images
    display.write_text(textList[0], 64, 64, 2, RED) # first line
    if(len(textList)>1): display.write_text(textList[1],64,120,3,BLACK) # second line

    display.show()
    time.sleep(1)
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
    time.sleep(1)

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
    x = 96
    y = 96
    BMP_W = 48
    BMP_H = 48  # size
    mypath = "/images/"  #圖檔的位置

    #showColor("black") 
    showImage(mypath + "UI_start.bmp", x, y)  # reset畫面

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
                    if data== b'1':  #訊號 == 1 # direction up
                        #showColor("black")
                        showImage(mypath + "icon_16x16.bmp", x, y) # show圖片: 只能是.bmp format
                        print("mode 1!")
                    elif data== b'2': #訊號 == 2 # direction down
                        #showColor("red")
                        showImage(mypath + "icon8-down-30.bmp", x, y) # show圖片: 只能是.bmp format
                        print("mode 2!")
                    elif data== b'3': #訊號 == 3 # fire warning
                        vibrator.value(1)
                        showColor("white")
                        showImage(mypath + "warning.bmp", x, y) # show圖片: 只能是.bmp format
                        time.sleep(1)
                        vibrator.value(0)
                        print("mode 3!")
                    elif data== b'4': #訊號 == 4 # car hone
                        showText("Google HPS")
                        print("mode 4!")
                    # else:
                    #     pass # 還有很多case，可以有對應的文字與icon
                    else:
                        print("Error BT signal!")
                                     
                
        # refresh 畫面
        if isActive:
            showColor("white")
