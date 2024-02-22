from vx_enum import *

import vx_bind as  vx

from datetime import datetime
import time

class MyFeed(vx.feed):
	
	def __init__(self):
		super(MyFeed, self).__init__()
		self.fBuckRows	=	0
		
	def onInit(self,pData):
		print ('onInit')
		print (pData)

	def onConnect(self,pData):
		print ('onConnect')

	def onExit(self,pData):
		print ('onExit')

	def onOpen(self,pData):
		print ('onOpen')
		print (pData)

	def onShut(self,pData):
		print ('onShut')
		print ("Total Buckets {}".format(self.fBuckRows))

	#def onEvent(self,pData,pEvent):
		#print ('onEvent')
		
	#def onProgress(self,pData):
		# print ('onProgress')
		# print (pData)

	def onError(self,pData):
		#print ('onError')
		print (pData)

	def onWarning(self,pData):
		#print ('onWarning')	
		print (pData)
	
	def onMessage(self,pData):
		print ('onMessage')
		print (pData)

	def onBucket(self,pData):
		
		tBucket = pData["bucket"]	
		print (pData);
		
		if (tBucket==Bucket.Summary)	:
			
			tTime = datetime.fromtimestamp (pData['time']/1000);
			tDate = tTime.isoformat(sep=' ', timespec='milliseconds')
			print(tDate)
		
			print(	"Trades: "
					"time:%(time)s,"
					"total:%(total)d,"
					"volume:%(volume)d,"
					"high:%(high)5.2f,"
					"low:%(low)5.2f,"
					"aggSellers:%(aggSellers)d,"
					"aggBuyers:%(aggBuyers)d,"
					"midPoint:%(midPoint)5.2f,"
					"midPoint_above:%(midPoint_above)d,"
					"midPoint_below:%(midPoint_below)d,"
					"vwap:%(vwap)5.2f,"
					"vwap_above:%(vwap_above)d,"
					"vwap_below:%(vwap_below)d"
					%pData) 

	
		self.fBuckRows	=	self.fBuckRows+1
		
	#def onIdle(self,pData):
		#print ('onIdle')
		#print (pData)

def test():

	myFeed = MyFeed()

	myFeed.request ({
		'email'				:	'xx@zz.com',
		'password'			:	'password',		
		'symbol'			:	'ZS',		
		'startDate'			:	20230501,
		'endDate'			:	20230501,
		'buckets'			:	Bucket.Summary,
		'interval'			:	1000*60*60,	#one hour
		'weekends'			:	False,
		'realtime'			:	True,
		'fids'				:	'kFidsTrds',
		'cachePath'			:	'E:\\_vx',
		'cacheRead'			:	True	
	})
	
	
if __name__ == "__main__":   
	test()
	
