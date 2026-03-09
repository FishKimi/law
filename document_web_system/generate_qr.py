import qrcode

url="http://你的服务器IP:5000"

img=qrcode.make(url)

img.save("qr.png")

print("二维码已生成")