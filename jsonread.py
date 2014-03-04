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
listThreshold = 5

def f1(inDict):
	for key in inDict:
		val = inDict[key]
		if isinstance(val, dict):
			f1(val)
		elif isinstance(val,list):
			if isinstance(val[0], dict):
				inDict[key] = f1(val[0])
			else:
				inDict[key] = [val[0]]
		else:
			inDict[key] = val
	return inDict



import json


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





jsonFileLarge = open('sf-city-lots-json/citylots.json')
jsonFileSample = open('jsonsample.json')
jsonFileComplex = open('cakejson.json')

jsonFile = jsonFileSample
jsonData = json.load(jsonFile)

test = {
	"top":
		{
			"cat1":
				[
					{
						"cat1A": "val",
						"cat1B": "val",
						"cat1C":
							{
								"cat1CA":
									[
										{ "id": [1,2,3], "type": "Regular" },
										{ "id": [1,2,3], "type": "Regular" }
									]
							},
						"cat1D":
							[
								{ "id": "5001", "type": 
													{
														"bottom":
															[
																{"bottomest":"val"},
																{"bottomest2":"val"}
															]
													}
								}
							]
					}
				]
		}
}
print f1(jsonData)
# def f1(values):

# 	if isinstance(value,dict):
# 		print "dict"
# 		return f1(value.iteritems())
# 	if isinstance(value,list):
# 		print "list"
# 		return f1(value[0])
# 	else:
# 		print "other"
# 		return value

# outdata = {}

# #print f1(jsonData.iteritems())
# for key,value in jsonData.iteritems():
# 	for key, value in f1(value.iteritems()):
# 		print key
# 		print value

# print outdata


#data = json.load(jsonData)

# for i in  get_all(jsonData):
# 	print(i)
# for key in jsonData['items']['item']:
# 	print key


jsonFile.close()