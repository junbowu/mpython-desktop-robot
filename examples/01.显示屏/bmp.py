from mpython import *
import framebuf

bmp = bytearray([\
0X00,0X00,0X00,0X00,0X03,0XC7,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X1E,0XFF,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X31,0X70,0X3F,0XFC,0X00,0X00,0X00,0X03,0XE0,0X00,0X00,0X00,0X00,
0X00,0X00,0X01,0XC2,0XB8,0X1F,0XF8,0X00,0X00,0X00,0X1F,0XF9,0X00,0X00,0X00,0X00,
0X00,0X18,0X00,0XF2,0X7C,0X1F,0XF0,0X00,0X30,0X01,0XFF,0XFF,0XFF,0XE0,0X00,0X00,
0X00,0XFF,0XFF,0XEF,0XCE,0X3F,0X80,0X01,0XFE,0X3F,0XBF,0XFF,0XFF,0XFF,0XE0,0X00,
0X03,0XFF,0XFF,0XFF,0X1E,0X3E,0X1C,0X01,0XFC,0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0X00,
0X03,0XFF,0XFF,0XF8,0X0C,0X38,0X00,0X07,0XBF,0XFF,0XFF,0XFF,0XFF,0XFF,0XF8,0X00,
0X0F,0XFF,0XFF,0XF0,0X60,0X18,0X00,0X0F,0XBF,0XFF,0XFF,0XFF,0XFF,0XFE,0X70,0X00,
0X0C,0X0F,0XFF,0XE0,0XF8,0X00,0X00,0X07,0X9F,0XFF,0XFF,0XFF,0XFF,0XE0,0X40,0X00,
0X10,0X0F,0XFF,0XF0,0XF8,0X00,0X00,0XC7,0X3F,0XFF,0XFF,0XFF,0XFF,0XC0,0X60,0X00,
0X00,0X0F,0XFF,0XF9,0XFC,0X00,0X01,0X47,0XFF,0XFF,0XFF,0XFF,0XFF,0XE0,0X20,0X00,
0X00,0X0F,0XFF,0XFB,0XFC,0X00,0X01,0X6F,0XFF,0XFF,0XFF,0XFF,0XFF,0XF8,0X00,0X00,
0X00,0X0F,0XFF,0XFF,0XC4,0X00,0X00,0X3F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0X00,0X00,
0X00,0X0F,0XFF,0XFF,0XC6,0X00,0X00,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0X00,0X00,
0X00,0X0F,0XFF,0XFF,0XE0,0X00,0X00,0X3F,0XF9,0XF3,0XFF,0XFF,0XFF,0XFC,0X00,0X00,
0X00,0X1F,0XFF,0XFF,0X00,0X00,0X01,0XF2,0XF8,0X33,0XFF,0XFF,0XFF,0XF8,0X00,0X00,
0X00,0X3F,0XFF,0XFE,0X00,0X00,0X01,0XE1,0XBF,0XB9,0XFF,0XFF,0XFF,0XF0,0X00,0X00,
0X00,0X3F,0XFF,0XF8,0X00,0X00,0X03,0XC0,0XA7,0XF9,0XFF,0XFF,0XFF,0X10,0X00,0X00,
0X00,0X3F,0XFF,0XF0,0X00,0X00,0X01,0X8C,0X07,0XFD,0XFF,0XFF,0XFF,0XC8,0X00,0X00,
0X00,0X3F,0XFF,0XF0,0X00,0X00,0X00,0XFC,0X00,0XFF,0XFF,0XFF,0XFF,0XC8,0X00,0X00,
0X00,0X1F,0XFF,0XC0,0X00,0X00,0X03,0XFE,0X20,0XFF,0XFF,0XFF,0XFF,0XC0,0X00,0X00,
0X00,0X1F,0XFF,0X80,0X00,0X00,0X03,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XE0,0X00,0X00,
0X00,0X17,0XE0,0X80,0X00,0X00,0X07,0XFF,0XFF,0XFD,0XFF,0XFF,0XFF,0XE0,0X00,0X00,
0X00,0X07,0XC0,0X80,0X00,0X00,0X0F,0XFF,0XFF,0X7C,0X7F,0XFF,0XFF,0XE0,0X00,0X00,
0X00,0X0B,0XC0,0X00,0X00,0X00,0X0F,0XFF,0XFF,0X7F,0X83,0XFF,0XFF,0XD0,0X00,0X00,
0X00,0X01,0XC0,0X40,0X00,0X00,0X1F,0XFF,0XFF,0XBF,0XC3,0XFF,0XFF,0X80,0X00,0X00,
0X00,0X03,0XCC,0X28,0X00,0X00,0X1F,0XFF,0XFF,0X9F,0XC0,0XF8,0XFC,0X00,0X00,0X00,
0X00,0X00,0XF8,0X08,0X00,0X00,0X1F,0XFF,0XFF,0XDF,0X80,0XF0,0X7C,0X08,0X00,0X00,
0X00,0X00,0X1E,0X00,0X00,0X00,0X1F,0XFF,0XFF,0XCE,0X00,0XE0,0X3E,0X08,0X00,0X00,
0X00,0X00,0X0E,0X00,0X00,0X00,0X1F,0XFF,0XFF,0XF8,0X00,0X60,0X1E,0X08,0X00,0X00,
0X00,0X00,0X02,0X10,0X00,0X00,0X1F,0XFF,0XFF,0XF2,0X00,0X60,0X06,0X04,0X00,0X00,
0X00,0X00,0X03,0X3F,0X00,0X00,0X0F,0XFF,0XFF,0XFE,0X00,0X20,0X10,0X06,0X00,0X00,
0X00,0X00,0X00,0X7F,0X80,0X00,0X07,0XFF,0XFF,0XFE,0X00,0X10,0X10,0X02,0X00,0X00,
0X00,0X00,0X00,0X7F,0XF0,0X00,0X03,0XCF,0XFF,0XFC,0X00,0X00,0X08,0X30,0X00,0X00,
0X00,0X00,0X00,0X7F,0XF0,0X00,0X00,0X03,0XFF,0XF8,0X00,0X00,0X18,0X60,0X00,0X00,
0X00,0X00,0X00,0XFF,0XF8,0X00,0X00,0X03,0XFF,0XF0,0X00,0X00,0X18,0XE0,0X00,0X00,
0X00,0X00,0X00,0XFF,0XFE,0X00,0X00,0X03,0XFF,0XE0,0X00,0X00,0X0C,0XE8,0X40,0X00,
0X00,0X00,0X00,0XFF,0XFF,0X80,0X00,0X03,0XFF,0XE0,0X00,0X00,0X0C,0XE8,0X3C,0X00,
0X00,0X00,0X00,0XFF,0XFF,0XE0,0X00,0X01,0XFF,0XC0,0X00,0X00,0X04,0X00,0X0E,0X00,
0X00,0X00,0X00,0XFF,0XFF,0XE0,0X00,0X01,0XFF,0XC0,0X00,0X00,0X01,0XC0,0X0F,0X00,
0X00,0X00,0X00,0X7F,0XFF,0XE0,0X00,0X01,0XFF,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X3F,0XFF,0XC0,0X00,0X01,0XFF,0XE0,0X00,0X00,0X00,0X00,0X40,0X00,
0X00,0X00,0X00,0X3F,0XFF,0XC0,0X00,0X01,0XFF,0XE2,0X00,0X00,0X00,0X00,0XE4,0X00,
0X00,0X00,0X00,0X1F,0XFF,0XC0,0X00,0X01,0XFF,0XE6,0X00,0X00,0X00,0X07,0XE4,0X00,
0X00,0X00,0X00,0X0F,0XFF,0XC0,0X00,0X01,0XFF,0X8C,0X00,0X00,0X00,0X0F,0XFE,0X00,
0X00,0X00,0X00,0X07,0XFF,0X80,0X00,0X01,0XFF,0X0C,0X00,0X00,0X00,0X1F,0XFE,0X00,
0X00,0X00,0X00,0X07,0XFF,0X80,0X00,0X00,0XFF,0X8C,0X00,0X00,0X00,0X7F,0XFF,0X00,
0X00,0X00,0X00,0X07,0XFE,0X00,0X00,0X00,0XFF,0X08,0X00,0X00,0X00,0XFF,0XFF,0X00,
0X00,0X00,0X00,0X07,0XFC,0X00,0X00,0X00,0XFE,0X00,0X00,0X00,0X00,0XFF,0XFF,0X00,
0X00,0X00,0X00,0X07,0XFC,0X00,0X00,0X00,0X7E,0X00,0X00,0X00,0X00,0XFF,0XFF,0X00,
0X00,0X00,0X00,0X07,0XF8,0X00,0X00,0X00,0X7C,0X00,0X00,0X00,0X00,0XFF,0XFF,0X00,
0X00,0X00,0X00,0X07,0XF8,0X00,0X00,0X00,0X78,0X00,0X00,0X00,0X00,0XF1,0XFE,0X00,
0X00,0X00,0X00,0X07,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X80,0X7C,0X00,
0X00,0X00,0X00,0X07,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X78,0X02,
0X00,0X00,0X00,0X03,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X02,
0X00,0X00,0X00,0X03,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X20,0X08,
0X00,0X00,0X00,0X03,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X10,
0X00,0X00,0X00,0X03,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X40,
0X00,0X00,0X00,0X03,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X01,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X60,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
])



fb1 = framebuf.FrameBuffer(bmp,128,64, framebuf.MONO_HLSB)
#oled.invert(1)
oled.blit(fb1,0,0)
oled.show()