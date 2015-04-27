import record

oanhInvitation = "oanhInvitation.md"

def putFileIntoAnArray(fileName):
    with open(fileName, 'r') as f:
        content = f.readlines()
#       print ''.join(content)
    return content

def makeArrayOfRecord(strRecordArray):
    for x in strRecordArray:
        pieces = x.split(":")
        print pieces[0]

strRecordArray = putFileIntoAnArray(oanhInvitation)
makeArrayOfRecord(strRecordArray)

