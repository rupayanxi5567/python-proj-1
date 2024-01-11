import qrcode as qr

the_img = qr.make("https://www.youtube.com/@VaktiGyans-/shorts")
the_img.save("channel.png")
