"""
this plugin replace starting TABs to "|   ".
open plugin>python script>show console to debug this script.

sample doc:
aaaa
	bbbbbbb
		ccccc
			dddd
				111111
					111111
						222222
							33333
								444444
		eeeee
	ffffff

output result:
aaaa
|   bbbbbbb
|   |   ccccc
|   |   |   dddd
|   |   |   |   111111
|   |   |   |   |   111111
|   |   |   |   |   |   222222
|   |   |   |   |   |   |   33333
|   |   |   |   |   |   |   |   444444
|   |   eeeee
|   ffffff

"""
import StringIO

allText = editor.getText() #getSelText
contextList = allText
contextList += "\n"

for line in StringIO.StringIO(allText):
    if line.find('\t') != 0: # not start with TAB
        contextList += line
    else:
        # start with tab, replace TAB to "|   "
        tail=line.lstrip('\t')
        tmp=""
        i=0
        while line.find('\t', i) == i:
            tmp ="|   " + tmp
            i+=1
        #print("line=%s,tmp=%s,tail=%s" % (line, tmp, tail))
        contextList += tmp + tail

editor.setText(contextList)
