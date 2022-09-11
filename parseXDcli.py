import sys
from parseXD import XMLParse

def printUsage(_program_name):
    print(f'Usage: {_program_name} <xml-file> <--option> <[arg1 arg2 ...]> <--saveXML filename.xml> ')

def printOptions(_options):
    print('Options:')
    for key in _options.keys():
        print('\t'+key)

def printHelp(_program_name, _options):
    printUsage(_program_name)
    printOptions(_options)

def printRoot(repo, arguments):
    repo.printRoot()

def printFirstsChilds(repo, arguments):
    repo.printFirstsChilds()

def printTagsANDAtributes(repo, arguments):
    repo.printTagsANDAtributes()

def findAll(repo, arguments):
    nodes = repo.findAll(arguments[0])
    repo.printXMLs(nodes)

def setAttributeIfTextMatch(repo, arguments):
    node = repo.setAttributeIfTextMatch(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])
    if(len(arguments)>1):
        if 'saveXML' in arguments[-2]:
            repo.saveXML(arguments[-1])
    else:
        repo.printXML(node)

def addTag(repo, arguments):
    node = repo.addTag(arguments[0], arguments[1])
    if(len(arguments)>1):
        if 'saveXML' in arguments[-2]:
            repo.saveXML(arguments[-1])
    else:
        repo.printXML(node)

def addAttribute(repo, arguments):
    node = repo.addAttribute(arguments[0], arguments[1], arguments[2])
    if(len(arguments)>1):
        if 'saveXML' in arguments[-2]:
            repo.saveXML(arguments[-1])
    else:
        repo.printXML(node)

def removeByXpath(repo, arguments):
    node = repo.removeByXpath(arguments[0])
    if(len(arguments)>1):
        if 'saveXML' in arguments[-2]:
            repo.saveXML(arguments[-1])
    else:
        repo.printXML(node)

def removeAll(repo, arguments):
    node = repo.removeAll(arguments[0])
    if(len(arguments)>1):
        if 'saveXML' in arguments[-2]:
            repo.saveXML(arguments[-1])
    else:
        repo.printXMLs(node)  

def getKeys(repo, arguments):
    repo.getKeys(arguments[0])

def getValues(repo, arguments):
    repo.getValues(arguments[0])

def __main__():
    program_name = sys.argv[0]
    arguments = []
    try:
        xmlfile = sys.argv[1]
        if(len(sys.argv)>2):
            option = sys.argv[2]
        if(len(sys.argv)>3):
            arguments = sys.argv[3:]
        xmalo = XMLParse(xmlfile)
        options = {
            '--printRoot': printRoot,
            '--printFirstsChilds': printFirstsChilds,
            '--printTagsANDAtributes': printTagsANDAtributes,
            '--findAll': findAll,
            '--setAttributeIfTextMatch': setAttributeIfTextMatch,
            '--addTag': addTag,
            '--addAttribute': addAttribute,
            '--removeByXpath': removeByXpath,
            '--removeAll': removeAll,
            '--getKeys': getKeys,
            '--getValues': getValues
        }
        try:
            options[option](xmalo,arguments)
        except Exception as e:
            print(e)
            printHelp(program_name,options)
    except Exception as e:
            print(e)
            printUsage(program_name)

if __main__:
    __main__()
