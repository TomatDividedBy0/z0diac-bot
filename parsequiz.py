import xml.etree.ElementTree as ET
tree = ET.parse('quiz.xml')
root = tree.getroot()

def getValue(dictionary):
    return (next(iter(dictionary.attrib.values())))
def check(x):
        result=input(x)
        if result == 'yes':
            iteration(True)
        elif result == 'no':
            iteration(False)
        else:
            print('you have to answer yes or no')
            check(x)
def label(labelname):
    print('You are a '+labelname+".")
question=root[0]
def iteration(answer):
    if answer == 'first':
        check(getValue(question))
    elif answer:
        if question[0][0].tag=='label':
            label(getValue(question[0][0]))
        else:
            def change():
                global question
                question=question[0][0]
            change()
            check(getValue(question))
    elif answer==False:
        if question[1][0].tag=='label':
            label(getValue(question[1][0]))
        else:
            def change2():
                global question
                question=question[1][0]
            change2()
            check(getValue(question))
    else:
        print('error')
iteration('first')
