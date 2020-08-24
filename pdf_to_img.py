#%%
from pdf2image import convert_from_path
import os
import time

print("***PDF解析中***")

input_dir = 'pdf'
save_dir = 'img'

def pdf_conv_img(input_dir, save_dir):
    pdf_files = os.listdir(input_dir)
    for pdf_name in pdf_files:
        input_path = input_dir + '/' + pdf_name
        try:
            img_num = pdf_img(input_path, save_dir)
        except:
            None

# Convert PDF to image
def pdf_img(input_path, save_path):
    pdf_name = input_path.split('/')[-1]
    img_name = pdf_name.split('.')[0]
    try:
        # Image conversion
        images = convert_from_path(input_path)
        i = 1
        for image in images:
            # Image conversion
            image.save(save_path + '/{}_{}.png'.format(img_name, i), 'png')
            i += 1
        return len(images)
    except Exception:
        raise Exception("このPDFは画像変換できませんでした。")


pdf_conv_img(input_dir, save_dir)
print("PDFファイル内を全て画像として保存しました。")