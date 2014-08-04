import output
import requests
import json

class Tinamous(output.Output):
	requiredData = ["AccountName", "Username","Password"]
	optionalData = []
	def __init__(self,data):
		self.AccountName=data["AccountName"]
		self.Username=data["Username"]
		self.Password=data["Password"]
	def outputData(self,dataPoints):
		measurement = {}
		fieldId = 1;
		for i in dataPoints:
			measurement["Field" + str(fieldId)] = i["value"]
			fieldId = fieldId +1;

		#measurement["Channel"] = 0
		measurement["Lite"]="true"
		measurementJson = json.dumps(measurement)

		try:
			headers = {'content-type': 'application/json'}
			auth=(self.Username, self.Password)
			url = "https://" + self.AccountName + ".tinamous.com/api/v1/measurements"
			
			r = requests.post(url,auth=auth, headers=headers, data = measurementJson)

			if r.status_code!=requests.codes.created: 
				#print ("Tinamous Error: "+ r.text)
				print "Tinamous Error: "+ r.text
				return False
		except Exception:
			return False
		return True


