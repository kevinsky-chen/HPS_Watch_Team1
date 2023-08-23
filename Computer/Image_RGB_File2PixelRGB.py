import io
from PIL import Image

def list2D(_1d, cols):
    return [_1d[i:i + cols] for i in range(0, len(_1d), cols)]

def str2list2D(_data='', _num=1, _sep=','):
    if _data == '':
        return list()
    else:
        _data = _data.strip().replace('\r', '').replace('\n', '')
        _list = _data.split(_sep)
        for i in range(len(_list)):
            _list[i] = _list[i].strip()
        return list2D(_list, _num)
    
def str2bytes(s=""):
    return s.encode() if isinstance(s, str) else s

def bytes2Str(b=b""):
    return bytes.decode(b) if isinstance(b, bytes) else b

def pixelHex(p, _header=''):
    if isinstance(p, int):
        p = hex(p)
    elif len(p) == 3:
        r, g, b = p
        p = '{}{:02x}{:02x}{:02x}'.format(_header, r, g, b)         # _header: 空白, '#', '0x', 或任何指定字元
    elif len(p) == 4:
        (r, g, b, a) = p
        p = '{}{:02x}{:02x}{:02x}{:02x}'.format(_header, r, g, b, a)      # a=0~255, alpha = a/255 = 0~1.0
    return p


#-------------------------
def imgStr(_img=None, _header=''):
    _rgb_bits = ''
    if _img is not None:
        (w, h) = _img.size
        _pixels = _img.load()
        for y in range(h):
            for x in range(w):
                _rgb_bits += (pixelHex(_pixels[x, y], _header) + ',')       # _header: 空白, '#', '0x', 或任何指定字元
    return _rgb_bits[:-1].strip()     # 去掉最後一個','字元, 為完整所有 pixels 的 RGB值 組成的字串


def imgList2D(_img=None, _header=''):
    if _img is not None:
        (w, h) = _img.size
        return str2list2D(imgStr(_img, _header), w)
    return list()


def imgList(_img=None, _header=''):
    _list = list()
    for _tmp in imgList2D(_img, _header):
        _list.append(','.join(_tmp))
    return _list

# Write every pixels RGB (000000~ffffff) to .txt file
def writeTXT(pix_rgb, _w=16, _file='image_rgb.txt', add_nl=True):
    items = pix_rgb.split(',')      # pix_rgb 是圖檔16進位的 rgb 字串
    # Opening the file in write mode
    with open(_file, 'w') as f:
        for i in range(0, len(items), _w):
            f.write(''.join(items[i:i+_w]))
            if add_nl:
                f.write('\n')
    f.close() 

def readTXT(_file='image_rgb.txt', to_list=False):
    lines = list() if to_list else ''
    # removing the new line characters
    with open(_file) as f:
        if to_list:
            lines = [line.rstrip() for line in f]
        else:
            while True:
                line = f.readline().rstrip()
                if not line:
                    break
                lines += line + ',' 
            lines = lines[:-1]
    f.close() 
    return lines

def readImage(_file='sample.jpg', wxh=(0,0), rotate=0):
    _img = Image.open(file_in)
    #if '.png' in IMAGE_FILE.lower():
    _img = _img.convert('RGB')        # PNG 需特殊處理, Convert RGBA to RGB

    if wxh != (0,0):
        _img = _img.resize((wxh[0], wxh[1]), Image.LANCZOS)
    if rotate != 0:
        _img = _img.rotate(rotate, expand=True)

    print('\n*** 圖檔資訊')
    print(type(_img), _img.format, _img.size, _img.mode, _img.palette)   # returns the colour palette table, if any.
    return _img.copy()

def img2bytes(_img, format='JPEG'):
    print('\n*** 原始的影像, 轉成 bytearray')
    img_byte_arr = io.BytesIO()
    _img.save(img_byte_arr, format=format)
    img_byte_arr = img_byte_arr.getvalue()
    print(len(img_byte_arr), type(img_byte_arr))
    print(img_byte_arr)


if __name__ == "__main__":
    import os
    #IMAGE_FILE = 'icon_16x16.jpg'       # 建議使用 JPG (RGB 格式)
    OUT_W = 64
    OUT_H = 64
    IMAGE_NAME = 'android'
    IMAGE_FILE = f'{IMAGE_NAME}_128x128.jpg'

    file_in = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_FILE)
    file_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{IMAGE_NAME}_{OUT_W}x{OUT_H}.txt')

    #img = readImage(file_in) 
    #img = readImage(file_in, (OUT_W, OUT_H)) # resize image
    img = readImage(file_in, (OUT_W, OUT_H), rotate=90) # rotate image by 90 degrees
    (img_width, img_height) = img.size
    img.show()

    """
    print('\n*** 原始的影像, 轉成 bytearray')
    IMAGE_FORMAT = IMAGE_FILE.split('.')[1].upper
    if IMAGE_FORMAT == 'JPG':
        IMAGE_FORMAT = 'JPEG'
    #img2bytes(img, format=IMAGE_FORMAT)
    """

    print('\n*** 原始的影像, 轉成 string')
    #pixels = imgStr(img, '#')  # 每個像素加上指定字元, 例如 # 或 0x ... 之類
    pixels = imgStr(img)
    #print(pixels)
    print(len(pixels), type(pixels))

    print('\n*** 寫入影像文字檔, 將圖檔的 RGB 字串, 等寬寫入')
    # Write string to file
    writeTXT(pixels, img_width, file_out)     # 預設 True, 加上分行字元 \n
    #writeTXT(pixels, OUT_W, file_out, False)       # 無分行字元 \n

    print('\n*** 讀取影像文字檔, 等寬存於 list 輸出')
    data = readTXT(file_out)    # 回傳字串
    #data = readTXT(file_out, True)      # 回傳 list
    print(data)
    print(len(data), type(data))


    """
    print('\n*** 轉換的 2D 的 RGB 陣列')
    pixels = imgList2D(img)
    print(len(pixels), type(pixels), pixels)

    print('\n*** 轉換的 1D 的 RGB 陣列')
    pixels = imgList(img)
    print(len(pixels), type(pixels), pixels)
    """
