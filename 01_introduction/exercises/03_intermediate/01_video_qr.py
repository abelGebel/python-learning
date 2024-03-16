import qrcode
png = qrcode.make("https://www.youtube.com/watch?v=YmtIva6SsVk")
png.save('ejemplo.png')