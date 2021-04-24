import StringIO

allText = editor.getText() #getSelText
contextList = allText
contextList += "\n\n"

for line in StringIO.StringIO(allText):
    if line.find('\t') != 0: # not start with TAB
        contextList += line
    else:
        tail=line.lstrip('\t')
        tmp=""
        i=1
        while line.rfind('\t', i) == i:
            tmp ="    " + tmp
            i+=1
        if i == 1:
            tmp = "|---"
        else:
            tmp += "|---"
        #print("line=%s,tmp=%s,tail=%s" % (line, tmp, tail))
        contextList += tmp + tail

editor.setText(contextList)
