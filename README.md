# vx-py 

| File             | Version                               |
| ---------------- |-----------------------------------------|
| vx_bind.pyd     | C7                     |
| vx_bind.so       | C4                             |
| Python       |  3.9                               |

Windows and linux release compiled for Python version 3.9

### Included Files

| File             | Description                             |
| ---------------- |-----------------------------------------|
| vx_bind.pyd      | Windows c++ Python binding module                  |
| vx_bind.so       | Linux c++ Python binding module     |
| vx_feed.py       | vx_bind definitions include file    |
| demo_events.py       | Sample application    |
| demo_icebergOrders.py      | Demonstrates the iceberg trigger    |
| demo_stopOrders.py			| Demonstrates the stopOrder trigger    |
| demo_trades.py				| Demonstrates the trade trigger    |
| demo_tradeSweeps.py		| Demonstrates the tradeSweeps trigger    |
| demo_book.py				| Demonstrates the book building functions     |
| demo_fix.py				| Demonstrates the fix REST api     |
| demo_summary.py				| Demonstrates the summary trigger     |
| demo_buckets.py				| Demonstrates the summary buckets     |

Place the module in your Python installation or in your script's search path or at the location of your script.

### Version C7 Changes

Added a new trigger type Trigger.Summary. Unlike the trigger Trigger.Trades which combine trade summery sweeps, each trade summary will be triggered individually.

The Trigger.Summary record has the following fields:

{
'aggBuyers': 161, 
'aggSellers': 133, 
'bucket': 1, 
'high': 1437.0, 
'low': 1434.75, 
'midPoint': 1435.875, 
'midPoint_above': 179, 
'midPoint_below': 121, 
'time': 1683014400000, 
'total': 300, 
'volume': 641, 
'vwap': 1435.9079563182527, 
'vwap_above': 179, 
'vwap_below': 121
}

Add a new bucket trigger Bucket.Summary.

Buckets are return via the callback 'onBucket.'

the parameter _interval is the bucket isze in milliseconds.

The Bucket.Summary record has the following fields:

{
'aggressor': 2, 
'orders': 1, 
'price': 1163, 
'px2vwap_max': 1163.8111413043478, 
'px2vwap_min': 1163.0, 
'px2vwap_time': 1.7080452015879542e+18, 
'quantity': 1, 
'time': 1708045201695212677, 
'trigger': 16, 
'volume': 554, 
'vwap': 1163.8109205776173
}


### vx_feed.py

vx_bind definitions includes

* Event record enumerated values
* Event record definitions
* Default fid definitions

### demo_events.py 

Application overview:

#### 1. Derive a class from   vx.feed

	myFeed = MyFeed()

#### 2. Call 'request' with a dictionary of request parameters.

	myFeed.request ({
		'symbol'		:	'ES',		
		'startDate'		:	20230321,
		'endDate'		:	20230322,
		'weekends'		:	False,
		'fids'			:	'kFidsTrds',
		'cachePath'		:	"E:\\_vx"	
		})
	
	Notes:

	The api will select the appropriate server based on the request (Historical, RT or RT options).
	For RT options, the 'symbol' must be qualified with (OPT:, OCH: or OCU:)
	fids can use the three default FID definitions (kFidsTrds, kFidsNorm, kFidsFull) or define your own.

	Set 'startDate' or 'endDate' to zero for RT.
	
	'cachePath' is optional and if defined the api will save compressed archives of historical files.
	'cacheRead' is optional and defaults to True, Set to False to recreate the archive
	'cacheName' is optional and defaults to name of the fids, Custom cache file name

#### 3. Override the following  functions:

##### def onInit(self,pData):
	Called when the script starts
	pData unused
##### def onExit(self,pData):	
	Called at the script is finished
	pData unused
##### def onOpen(self,pData):
	Called at the start of each session of data
	pData will contain a diction of meta data
##### def onShut(self,pData):
	Called at the start of each session of data
	pData unused
##### def onEvent(self,pData,pEvent):
	Called with retrieved event records
	pData will contain meta data
	pEvent will contain a diction of Event fids (see vx_feed.py)
##### def onProgress(self,pData):
	Called during the reading of the request
	pData progress info
##### def onError(self,pData):
	Called if an error has occurred
	pData error info
##### def onIdle(self,pData):
	Called during idle for RT queries
	pData unused