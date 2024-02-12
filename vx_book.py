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
		if (tTrigger&Trigger.Trades)	:
			
			if self.fTrigRows == 1000	:
				print("Trades: aggressor:%(aggressor)d,entry:%(entry)5.2f,exit:%(exit)5.2f,levels:%(levels)d,orders:%(orders)d,quantity:%(quantity)d"%pData) 				
				#print("BookErro {}".format(self.BookErro()))				
				print("BookRows SideType.Ask {}".format(self.BookRows(SideType.Ask)))
				print("BookRows SideType.Bid {}".format(self.BookRows(SideType.Bid)))

				tBookA = self.BookItem(SideType.Ask,1)
				print (tBookA)			
				tBookB = self.BookItem(SideType.Bid,1)
				print (tBookB)
			
		
		self.fTrigRows	=	self.fTrigRows+1
		
	#def onIdle(self,pData):
		#print ('onIdle')
		#print (pData)

def test():

	myFeed = MyFeed()

	myFeed.request ({
		'email'				:	'ed@vertex-analytics.com',
		'password'			:	'Utopia',	#//V3rt3xV3!		
		'symbol'			:	'ZC',		
		'startDate'			:	Session.Previous,
		'endDate'			:	Session.Previous,
		'triggers'			:	Trigger.Trades,
		'weekends'			:	False,
		'realtime'			:	True,
		'buildBooks'		:	True,
		'fids'				:	'kFidsTrds',
		'cachePath'			:	"E:\\_vx",
		'cacheRead'			:	True	
	})
	
	
if __name__ == "__main__":   
	test()
	
