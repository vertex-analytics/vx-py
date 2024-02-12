from vx_enum import *

import vx_bind as  vx

from time import perf_counter

class MyFeed(vx.feed):
	
	def __init__(self):
		super(MyFeed, self).__init__()
		self.fEvntRows	=	0
		self.fTrigRows	=	0
		
	def onInit(self,pData):
		print ('onInit')
		print (pData)
		self.last = {
		  "header.instrumentID": 0
		}

	def onConnect(self,pData):
		print ('onConnect')

	def onExit(self,pData):
		print ('onExit')

	def onOpen(self,pData):
		print ('onOpen')
		print (pData)
		self.fEvntRows	=	0

	def onShut(self,pData):
		print (self.fTrigRows)
		print ('onShut')

	def onEvent(self,pData,pEvent):
		
		# if hasattr(pEvent, "test"):
		# 	print ('test')
		# pEvent["test"]	=	1

		self.last["header.instrumentID"]
		
		self.last["header.instrumentID"]		=	pEvent["header.instrumentID"]
		self.last["header.sequence"]			=	pEvent["header.sequence"]
		self.last["header.time"]				=	pEvent["header.time"]
		self.last["header.channelSequence"]		=	pEvent["header.channelSequence"]
		self.last["header.instrumentSequence"]	=	pEvent["header.instrumentSequence"]
		self.last["header.unionID"]				=	pEvent["header.unionID"]
		self.last["header.eventIndicator"]		=	pEvent["header.eventIndicator"]
		self.last["header.flag"]				=	pEvent["header.flag"]
		self.last["header.baseExponent"]		=	pEvent["header.baseExponent"]

		#if self.fEvntRows < 20	:
		#	print ('onEvent')
		#	print(pData)

		if pEvent["header.unionID"] == UnionID.TradeSummary			:

			self.last["tradeSummary.price"]				=	pEvent["tradeSummary.price"]
			self.last["tradeSummary.quantity"]			=	pEvent["tradeSummary.quantity"]
			self.last["tradeSummary.matches"]			=	pEvent["tradeSummary.matches"]
			self.last["tradeSummary.aggressor"]			=	pEvent["tradeSummary.aggressor"]
			self.last["tradeSummary.isImplied"]			=	pEvent["tradeSummary.isImplied"]
			self.last["tradeSummary.isSnapshot"]		=	pEvent["tradeSummary.isSnapshot"]
			self.last["tradeSummary.volume"]			=   pEvent["tradeSummary.volume"]

			if self.fEvntRows < 20	:
				print('{} ID: {:d} PRICE: {:.3f} SIZE: {:d}'.format('TradeSummary', pEvent["header.instrumentID"],pEvent["tradeSummary.price"], pEvent["tradeSummary.quantity"]))
			
			# if ((self.fEvntRows % 1000)==0)	:
			# 	print('{} ID: {:d} PRICE: {:.3f} SIZE: {:d}'.format('TradeSummary', pEvent["header.instrumentID"],pEvent["tradeSummary.price"], pEvent["tradeSummary.quantity"]))

		#elif pEvent["header.unionID"] == UnionID.TradeMatch			:
		#	print ('TradeMatch')

		#elif pEvent["header.unionID"] == UnionID.VolumeUpdate			:
		#	print ('VolumeUpdate')

		#elif pEvent["header.unionID"] == UnionID.BookLevel				:
			#print ('BookLevel')

		elif pEvent["header.unionID"] == UnionID.OrderBook				:
			#print ('OrderBook')
			self.last["orderBook.orderID"]				=	pEvent["orderBook.orderID"]
			self.last["orderBook.auxilaryID"]			=	pEvent["orderBook.auxilaryID"]
			self.last["orderBook.priorityID"]			=	pEvent["orderBook.priorityID"]
			self.last["orderBook.price"]				=	pEvent["orderBook.price"]
			self.last["orderBook.previousID"]			=	pEvent["orderBook.previousID"]
			self.last["orderBook.quantity"]				=	pEvent["orderBook.quantity"]
			self.last["orderBook.action"]				=   pEvent["orderBook.action"]
			self.last["orderBook.type"]					=   pEvent["orderBook.type"]
			self.last["orderBook.isSnapshot"]			=   pEvent["orderBook.isSnapshot"]

		#elif pEvent["header.unionID"] == UnionID.SecurityStatus		:
		#	print ('SecurityStatus')

		#elif pEvent["header.unionID"] == UnionID.DailyStatistics		:
		#	print ('DailyStatistics')

		#elif pEvent["header.unionID"] == UnionID.SessionStatistics		:
		#	print ('SessionStatistics')

		#elif pEvent["header.unionID"] == UnionID.LimitsBanding			:
		#	print ('LimitsBanding')

		#elif pEvent["header.unionID"] == UnionID.ChannelReset			:
		#	print ('ChannelReset')

		#elif pEvent["header.unionID"] == UnionID.TransactionMarker		:
		#	print ('TransactionMarker')

		#elif pEvent["header.unionID"] == UnionID.ClearingPrice			:
		#	print ('ClearingPrice')

		self.fEvntRows	=	self.fEvntRows+1
	
	def onProgress(self,pData):
		#print ('onProgress')
		print (pData)

	def onError(self,pData):
		#print ('onError')
		print (pData)

	def onWarning(self,pData):
		self.fEvntRows	=	0
		#print ('onWarning')	
		print (pData)
	
	def onMessage(self,pData):
		#print ('onMessage')
		print (pData)

	def onTrigger(self,pData):
		#print ('onTrigger')
		#print (pData)

			
		if self.fTrigRows < 50	:
			tTrigger = pData["trigger"]	
			if (tTrigger&Trigger.IcebergOrders)	:
				print("IcebergOrders: orderID:%(orderID)d,priorityID:%(priorityID)d,price:%(price)5.2f,quantity:%(quantity)d,fills:%(fills)d"%pData) 
			if (tTrigger&Trigger.TradeSweeps)	:
				print("TradeSweeps: aggressor:%(aggressor)d,entry:%(entry)5.2f,exit:%(exit)5.2f,levels:%(levels)d,orders:%(orders)d,quantity:%(quantity)d"%pData) 
			if (tTrigger&Trigger.StopOrders)	:
				print("StopOrders: aggressor:%(aggressor)d,entry:%(entry)5.2f,exit:%(exit)5.2f,levels:%(levels)d,orders:%(orders)d,quantity:%(quantity)d"%pData) 
			
			#  Trigger=	pData["trigger"];
			# match 1:
			# 	case Trigger.IcebergOrders:
			# 		print("IcebergOrders:")
			# 	case Trigger.TradeSweeps:
			# 		print("TradeSweeps: aggressor:%(aggressor)d,entry:%(entry)5.2f,exit:%(exit)5.2f,levels:%(levels)d,orders:%(orders)d,quantity:%(quantity)d"%pData) 
			# 	case Trigger.StopOrders:
			# 		print("StopOrders: aggressor:%(aggressor)d,entry:%(entry)5.2f,exit:%(exit)5.2f,levels:%(levels)d,orders:%(orders)d,quantity:%(quantity)d"%pData) 
			# 	case _:
			# 		print("Undefined") 
	
		self.fTrigRows	=	self.fTrigRows+1
		
	#def onIdle(self,pData):
	#	print ('onIdle')
	#	print (pData)

def test():

	start = perf_counter()
	myFeed = MyFeed()

	myFeed.request ({
		'email'				:	'xx@zz.com',
		'password'			:	'password',		
		'symbol'			:	'NQ',		
		'startDate'			:	20230501,
		'endDate'			:	20230501,
		'weekends'			:	False,
		'realtime'			:	True,
		'fids'				:	'kFidsTrds',
		'cachePath'			:	"E:\\_vx",
		'cacheRead'			:	True	#Default to True, Set to False to recreate the archive
		#'cacheName'			:	'BLUE'	Default to name of the fids, Custom cache file name
	})
	duration = perf_counter() - start
	
	print('myFeed.request Seconds: {:.3f}  Events: {:.0f} Events/Sec: {:.3f} \n\n'.format(duration,myFeed.fEvntRows,myFeed.fEvntRows/duration))
	
if __name__ == "__main__":   
	test()
