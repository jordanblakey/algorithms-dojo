def justify(text, width):
#     print('args:', text, width)
    print(text)
    text = text.split(' ')
    print(text)
    count = [len(word) for word in text]
    runningcount = 0
    line = []
    linepad = ''
    formatted = ''
    breakindex = 0
#     print('characters per word:'count)
#     print('total:',reduce(lambda x,y: x+y, count))
    for i, word in enumerate(text):
        print('current word:', word)
        runningcount += len(word)
        if runningcount <= (int(width) - (i - breakindex)):
            line.append(word)
            print('line:',line)
#             print(i-breakindex)
#             print('runningcount:',runningcount)
            print('text word count:', len(text), 'current word index:', i + 1)
        
            if len(line) > 1 : space = (width - runningcount)/(len(line)-1)
            else: space = 0

        elif len(text) <= i + 1:
            print('THE END')
            line = []
            line.append(word)
            linepad += ' '.join(line)
            print('final linepad:', linepad)
            formatted += linepad

        else: 
            spaces = space * ' '
#             print('spaces:' + spaces + '|')
#             print('spaces allocated to each:', space)
            linepad += spaces.join(line) + '\n'
            print('linepad1:' + str(len(list(linepad))))
            print(list(linepad))
            if len(list(linepad)) == 15: 
                print('space index:', linepad.index(' '))
                linepad = linepad[:linepad.index(' ')] + ' ' + linepad[linepad.index(' '):]
                print('linepad2:' + str(len(list(linepad))))
            if len(list(linepad)) < 15: 
                space = width - len(list(linepad)) + 1
                spaces = space * ' '
                linepad = spaces + linepad
                               
            formatted += linepad
            breakindex = i
            runningcount = 0
            line = []
            linepad = ''
#         print('index:', i, 'word:', word, 'char count:', len(word))
#         print('current line:', line)
#         print('line char count:', runningcount)
#         print('width - runningcount:', width-runningcount)
#         print('minimum spaces necessary:', len(line)-1)
    print(formatted)
    return formatted 

# More succinctly
def justify2(text, width):
  length = text.rfind(' ', 0, width+1)
  if length == -1 or len(text) <= width: return text
  line = text[:length]
  spaces = line.count(' ')
  if spaces != 0:
    expand = (width - length) / spaces + 1
    extra = (width - length) % spaces
    line = line.replace(' ', ' '*expand)
    line = line.replace(' '*expand, ' '*(expand+1), extra)
  return line + '\n' + justify(text[length+1:], width)
