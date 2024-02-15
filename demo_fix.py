
import vx_bind as  vx
from threading import Event
import logging
import threading
import time

gUserName			=	'<name>@vertex-analytics.com'
gAccount			=	'<accountid>'
gSymbol				=	'NQU2'		
gSecurityExchange	=	'CME'
gSecurityType		=	'FUTURE'

class MyFix(vx.fix):
	
	def __init__(self):
		super(MyFix, self).__init__()
		self.sequ	=	int(time.time())
		
	def MakeID (self):
	
		self.sequ	=	self.sequ+1
		return "SEQU_:{}".format (self.sequ)	
		
	def Messages (self):
		
		messages = self.request ({
			'UserName'			:	gUserName,
			'Request'			:	'Messages'
			})
			
		print (messages)

	def SendNewOrderSingleMarket (self):
		
		self.NewOrderSingleID	=	self.MakeID()
		print ("NewOrderSingleID: {}".format(self.NewOrderSingleID));
		
		tResponse = self.request ({
			'ID'				:	self.NewOrderSingleID,
			'Request'			: 	'NewOrderSingle',
			'OrdType'			: 	'MARKET',
			'Side'				: 	'BUY',
			'TimeInForce'		: 	'DAY',
			'OrderQty'			:	1,
			'Symbol'			:	gSymbol,
			'SecurityExchange'	:	gSecurityExchange,
			'SecurityType'		:	gSecurityType
			});
			
		print (tResponse)
		

def test():

	myFix = MyFix()
	myFix.SendNewOrderSingleMarket()
	
	event = threading.Event()
	
	while not event.isSet():
		try:
			myFix.Messages()
			event.wait(1)
		except KeyboardInterrupt:
			event.set()
			break
				   
if __name__ == "__main__":   
	test()

