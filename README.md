# HPS_Watch_Team1
The program is the Python/microPython code for Google HPS project 2023

### The file structure tree is as follows:  (除了粗體之外的檔案均已經裝在裝置內，只有粗體的 code 儲存在此 repository內) 
-- Computer/                      => run on computer 
------ **Image_RGB_File2PixelRGB.py** <p align="right">將圖片轉成.txt，非.bmp輸入需用此 (***用不太到/說明用途 ***) </p>
------ Bt_RPI.py                  => 電腦端傳藍芽訊號程式 (需merge至其他電腦程式, a.k.a. 帽子端的程式)  
-- Device/                        => run on RP2040; 需使用Thonny編輯  
---- fonts/  
---- images/                      => 要顯示的圖放這  
---- lib/  
---- code/                        => RP2040 上要跑的程式  
------ **Show.py**                => 顯示程式(可以顯示圖、字、填補色) (僅能顯示 **16色點陣圖** .bmp)  

### How to run?
- codes in Computer/              => upload to RPI, run Python on it
- codes in Device/                => upload to RP2040 by **Thonny** editor, run microPython on it
                                  => without connecting to the computer, please change th  targeted filename to ***main.py***


## The file structure of RP2040 in Thonny
![image](https://github.com/kevinsky-chen/HPS_Watch_Team1/assets/56266480/28dc7ed8-a96a-4544-bb36-0f25ae761aed)
Please note that:  
- All the codes that runs on device put to the same folder (home directory)
- Folders including fonts/, images/, lib/ are all contained in the device already, don't change it!
