# vx-py 


| File             | Version                               |
| ---------------- |-----------------------------------------|
| vx_bind.pyd     | C4                      |
| vx_bind.so       | C4                             |
| Python       |  3.9                               |


Windows and linux release compiled for Python version 3.9

### Included Files

| File             | Description                             |
| ---------------- |-----------------------------------------|
| vx_bind.pyd      | Windows c++ Python binding module                  |
| vx_bind.so       | Linux c++ Python binding module     |
| vx_feed.py       | vx_bind definitions include file    |
| vx_demo.py       | Sample application    |

Place the module in your Python installation or in your script's search path or at the location of your script.

### vx_feed.py

vx_bind definitions includes

* Event record enumerated values
* Event record definitions
* Default fid definitions

### vx_demo.py 

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





