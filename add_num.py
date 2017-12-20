

#思路
#1、创建画布对象（接受打开的图片资源对象）
#2、定义字体颜色
#3、定义画布的宽和高
#4、使用对象的text方法在画布上写字
#5、保存图片
#6、使用到的库 Image ImageFont ImageDraw
from PIL import Image , ImageFont, ImageDraw
def add_num(img):
    draw = ImageDraw.Draw(img)
    fontstyle = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
    fontcolour = '#ff0000'
    width,height = img.size
    draw.text((width-40,0),'01',font=fontstyle,fill=fontcolour)
    img.save('meinv.jpg','jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('./img/mei.jpg')
    add_num(image)

