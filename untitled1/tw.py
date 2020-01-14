from konlpy.tag import Okt
import jpype
import os

okt = Okt()
text ="자연어는 처리가 필요합니다."
print(okt.morphs(text))
print(okt.pos(text))
print(okt.nouns(text))