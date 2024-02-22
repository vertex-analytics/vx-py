from vx_enum import *

import vx_bind as  vx

class MyFeed(vx.feed):
	
	def __init__(self):
		super(MyFeed, self).__init__()
		self.fTrigRows	=	0
		
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
		self.fEvntRows	=	0

	def onShut(self,pData):
		print ('onShut')
		print("Total Triggers {}".format(self.fTrigRows))

	#def onEvent(self,pData,pEvent):
		#print ('onEvent')
		
	def onProgress(self,pData):
		print ('onProgress')
		print (pData)

	def onError(self,pData):
		#print ('onError')
		print (pData)

	def onWarning(self,pData):
		self.fEvntRows	=	0
		#print ('onWarning')	
		print (pData)
	
	def onMessage(self,pData):
		print ('onMessage')
		print (pData)

	def onTrigger(self,pData):
		
		#print ('onTrigger')
		#print (pData)

		tTrigger = pData["trigger"]	
			
		if (tTrigger==Trigger.Summary)	:
			if self.fTrigRows < 100	:
				print (pData)
				print(	"Summary: "
						"time:%(time)d,"
						"aggressor:%(aggressor)d,"
						"quantity:%(quantity)d,"
						"orders:%(orders)d,"
						"price:%(price)5.2f,"
						"volume:%(volume)d,"
						"vwap:%(vwap)5.2f,"
						"px2vwap_min:%(px2vwap_min)5.2f,"
						"px2vwap_max:%(px2vwap_max)5.2f"
						"px2vwap_time:%(px2vwap_time)5.2f"
						%pData) 
			
			self.fTrigRows	=	self.fTrigRows+1
		
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
		'triggers'			:	Trigger.Summary,
		'weekends'			:	False,
		'realtime'			:	True,
		'fids'				:	'kFidsTrds',
		'cachePath'			:	'E:\\_vx',
		'cacheRead'			:	True,	
		'progress'			:	1	
	})
	
	
if __name__ == "__main__":   
	test()
	
