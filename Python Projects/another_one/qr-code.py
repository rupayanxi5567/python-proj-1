import qrcode as qr

img = qr.make("https://www.youtube.com/results?search_query=taipy+projects")

img.save("taipy_mal.png")