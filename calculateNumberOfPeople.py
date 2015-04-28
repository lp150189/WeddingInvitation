import record
import re

oanhInvitation = "oanhInvitation.md"
hoangInvitation = "HoangInvitationList.md"
hoiNgocInvitation = "hoiNgocInvitationList.md"
huyFriendInvitaion = "huyFriendInvitationList.md"
oanhFamilyInvitation = "oanhFamilyInvitationList.md"

def putFileIntoAnArray(fileName):
    with open(fileName, 'r') as f:
        content = f.readlines()
#       print ''.join(content)
    return content

def makeArrayOfRecord(strRecordArray):
    for x in range (1,len(strRecordArray)):
        # print x
        pieces = re.split(":", strRecordArray[x])
        print pieces[0]
        print pieces[1]
        # print len(pieces)

strRecordArray = putFileIntoAnArray(oanhFamilyInvitation)
makeArrayOfRecord(strRecordArray)

