import qrcode as qc

image = qc.make("https://www.youtube.com/@casetooop")

image.save("casetoo_channel.png")