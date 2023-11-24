#PDF

import re
from pdfminer.high_level import extract_text
text = extract_text(r"C:\Users\kavin\Desktop\sample.pdf")
print(text)

#SUMMARIZER

#pip install transformers
from transformers import pipeline
summarizer = pipeline('summarization')
article = ''' '''
summary = summarizer(article,max_length=150,min_length=50,do_sample=False)
summary[0]['summary_text']


#TRANSLATOR

#pip install googletrans==4.0.0rc1
from googletrans import Translator
translator = Translator()
text = " "
trnsltd = translator.translate(summary[0]['summary_text'], dest='ta')
print(trnsltd.text)