# HPS_Watch_Team1
The program is the Python/microPython code for Google HPS project 2023

### The file structure tree is as follows:  
-- Computer/                      => run on computer; 用不到/說明用途  
------ Image_RGB_File2PixelRGB.py => 將圖片轉成.txt，非.bmp輸入需用此  
------ Bt_RPI.py                  => 電腦端傳藍芽訊號程式 (需merge至其他電腦程式, a.k.a. 帽子端的程式)  
-- Device/                        => run on RP2040; 需使用Thonny編輯  
---- fonts/  
---- images/                      => 要顯示的圖放這  
---- lib/  
---- code/                        => RP2040 上要跑的程式  
------ Show.py                    => 顯示程式(可以顯示圖、字、填補色) (僅能顯示 **16色點陣圖** .bmp)  

### How to run?
- codes in Computer/              => upload to RPI, run Python on it
- codes in Device/                => upload to RP2040 by **Thonny** editor, run microPython on it
                                  => without connecting to the computer, please change the  targeted filename to ***main.py***
