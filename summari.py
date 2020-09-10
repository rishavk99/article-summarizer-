from newspaper import Article
article=Article('https://www.firstpost.com/health/narendra-modis-speech-on-coronavirus-pm-announces-total-lockdown-for-three-weeks-but-essential-services-to-remain-open-key-takeways-8185551.html',language='en')
article.download()
article.parse()
article.nlp()
print(article.summary)
