from record import Record 
import re

hoangInvitation = "HoangInvitationList.md"
hoiNgocInvitation = "hoiNgocInvitationList.md"
huyFriendInvitaion = "huyFriendInvitationList.md"
oanhFamilyInvitation = "oanhFamilyInvitationList.md"
oanhInvitation = "oanhInvitation.md"
thuInvitation = "ThuInvitationList.md"

recordArray =[]
def putFileIntoAnArray(fileName):
    with open(fileName, 'r') as f:
        content = f.readlines()
#       print ''.join(content)
    return content

def makeArrayOfRecord(strRecordArray, recordArray):
    for x in range (1,len(strRecordArray)):
        pieces = re.split(":", strRecordArray[x])
        # print pieces[0]
        # print pieces[1]
        if(len(pieces)== 2):
            record = Record(pieces[0],pieces[1],True)
            recordArray.append(record)
        else:
            record = Record(pieces[0],pieces[1],False)
            recordArray.append(record)
        printRecord(pieces)
    print "\n" 
    print "\n" 

def calculateMaxNumber():
    maxNumber = 0
    minNumber =  0
    recordArray = []
    updateRecordArray(hoangInvitation, recordArray)
    updateRecordArray(hoiNgocInvitation, recordArray)
    updateRecordArray(huyFriendInvitaion, recordArray)
    updateRecordArray(oanhFamilyInvitation, recordArray)
    updateRecordArray(oanhInvitation, recordArray)
    updateRecordArray(thuInvitation, recordArray)
    for x in recordArray:
        maxNumber = maxNumber + int(x.getNumPpl())
    
    for x in recordArray:
        if  (x.getMaybe() == True):
            minNumber = minNumber + int(x.getNumPpl())
    print len(recordArray)
    print "The maximum number that will join is : ", maxNumber
    print  "The maximum number that will join is : ", minNumber
    print "-------------------------------------------------------------------------------------------------------------"
    print "-------------------------------------------------------------------------------------------------------------"
    print "-------------------------------------------------------------------------------------------------------------"
    print "-------------------------------------------------------------------------------------------------------------"

def printRecord(pieces):
    ten = re.split("\)", pieces[0])
    print "Ten:", ten[1].lstrip(' ')
    print "So nguoi di: ", pieces[1]
    if(len(pieces)==3):
        print "Co The Ko Di: ", pieces[2]

def updateRecordArray (fileName, array):
    print "*************************************************"
    print fileName
    print "*************************************************"
    strRecordArray = putFileIntoAnArray(fileName)
    makeArrayOfRecord(strRecordArray, array)

calculateMaxNumber()
