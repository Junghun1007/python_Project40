import qrcode

qrlist_path = r'subdata/qrlist.txt'
with open(qrlist_path, 'rt',encoding = 'UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        qr_img = qrcode.make(line)
        save_path = line + '.png'
        qr_img.save(save_path)