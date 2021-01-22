from wordcloud import WordCloud
from PIL import Image
import numpy as np

# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!")
# f.close()

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[3:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅜ','').replace('이모티콘\n','').replace('사진\n','').replace('ㅠ','').replace('ㅎ','')

print(text)

# C:\Windows\Fonts\malgunbd.ttf
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

# wc = WordCloud(font_path='C:/Windows/Fonts/malgunbd.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/malgunbd.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")