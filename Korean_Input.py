# -*- coding: utf-8 -*-
#translate -f zh -t ja 我是谁
from translate import Translator
translator= Translator(to_lang="en")
translation = translator.translate("유학을 가려는데 정보를 알려주셔요.")
print(translation)
