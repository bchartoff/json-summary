import collections
import os
import sys
import binascii
from pprint import pprint
import json


jsonIsList = False
tempListKey = ""
listThreshold = 5

def setTempListKey():
  return "json-summary-temporary-key%s"%binascii.b2a_hex(os.urandom(15))

def openJson(fileName):
  global jsonIsList
  global tempListKey
  with open(fileName) as inFile:
    while True:
      char = inFile.read(1)
      if not char:
        raise Exception("Malformed JSON, does not begin with { or [")
        break
      if char == "[":
        jsonIsList = True
        tempListKey = setTempListKey()
        inFile.seek(0,0)
        tempFileString = "{\"%s\":%s}"%(tempListKey,inFile.read())
        jsonData = json.loads(tempFileString, object_pairs_hook=collections.OrderedDict)
        break
      if char == "{":
        inFile.seek(0,0)
        jsonData = json.load(inFile, object_pairs_hook=collections.OrderedDict)
        break
  return jsonData
      #elif char == "{"
# def summarize(inJson):


# def summarizeList(inList):
#   for item in inList:
    


#out = {}
#A
#func of dict, 
#for key,val in dict
  #if val is nothing
    #dict[key] = val
  #if val is dict
    #func(val)
  #if val is list
    #if val[0] is nothing
      #dict[key] = val[0]
    #if val[0] is dict
      #dict[key] = func(val[0])

def comment(commentType,num=0):
  if commentType == "endList":
    return "******* List contains %i total entries *******"%num

def summarizeList(inList):

def summarizeDict(inDict):
  for key in inDict:
    val = inDict[key]
    if isinstance(val, dict):
      summarizeDict(val)
    elif isinstance(val,list):
      if isinstance(val[0], dict):
        inDict[key] = summarizeDict(val[0])
      else:
        #inDict[key] = [val[0]]
        inDict[key] = val
    else:
      inDict[key] = val
  return inDict





# def get_all(data):
#     sub_iter = []
#     if isinstance(data, dict):
#         sub_iter = data.iteritems()
#     if isinstance(data, list):
#         sub_iter = data[0]
#         yield sub_iter
#     for x in sub_iter:
#         for y in get_all(x):
#             yield x





#jsonFileLarge = open('sf-city-lots-json/citylots.json')
jsonFileSample = 'jsonsample.json'
jsonFileComplex = 'cakejson.json'

jsonFile = jsonFileSample

#jsonData = None
#try:
jsonData = openJson(jsonFile)
#except ValueError as e:
 # print "Malformed JSON?"

# with open('outFile2.json','w') as out:
#     json.dump(jsonData, out, indent=2)
#  openJson('jsonsample.json')

#print f1(jsonData)
# def f1(values):




with open('outFile.json','w') as out:
  outData = summarizeDict(jsonData)
  if jsonIsList:
    outData = [outData[tempListKey]]
  json.dump(outData, out, indent=2)


#   if isinstance(value,dict):
#     print "dict"
#     return f1(value.iteritems())
#   if isinstance(value,list):
#     print "list"
#     return f1(value[0])
#   else:
#     print "other"
#     return value

# outdata = {}

# #print f1(jsonData.iteritems())
# for key,value in jsonData.iteritems():
#   for key, value in f1(value.iteritems()):
#     print key
#     print value

# print outdata


#data = json.load(jsonData)

# for i in  get_all(jsonData):
#   print(i)
# for key in jsonData['items']['item']:
#   print key


