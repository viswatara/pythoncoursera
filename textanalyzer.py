class TextAnalyzer(object):
    def __init__(self,text):
        fmtText=text.lower()
        fmtText=fmtText.replace('.','').replace('!','').replace('?','').replace(',','')
        self.fmtText=fmtText
    def freqAll(self):
        Dict={}
        words=[]
        words=self.fmtText.split(' ')
    
        for key in set(words):
            Dict[key]=words.count(key)
        return Dict
    def freqOf(self,word):
        Dict=self.freqAll()
        if word in Dict:
            return Dict[word]
        else:
            return 0

sentence=TextAnalyzer("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
sentence.fmtText
sentence.freqAll()
sentence.freqOf('et')
