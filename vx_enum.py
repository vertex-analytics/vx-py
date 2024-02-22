
from enum import IntEnum, Enum

#--------------------------------------------------------
# Field Identification
#--------------------------------------------------------

Fids = [

	"header.instrumentID",				# Unique ID given by the exchange used to Identify the contract 
	"header.sequence", 
	"header.time",						# Time in with nanosecond precision
	"header.channelSequence",			# Packet level sequence number per channel multiple instrumentSequence #'s for multiple contracts can have the same ChannelSequence #
	"header.instrumentSequence",		# Unique ID given by the exchange to each Market event a contract has. These sequentially get larger. 
	"header.unionID",
	"header.eventIndicator",
	"header.flag",
	"header.baseExponent",

	"transactionMarker.type",

	"channelReset.type",

	"tradeSummary.price",				# Price at which the event occurred
	"tradeSummary.quantity",			# Quantity matched for this event
	"tradeSummary.matches",				# Identifies the total number of non-implied orders that participated in this trade event
	"tradeSummary.aggressor",			# The side of the aggressor: 1=Buy, 2=Sell and 0=Implied
	"tradeSummary.isImplied", 
	"tradeSummary.isSnapshot",
	"tradeSummary.volume",

	"tradeMatch.isAggressor",
	"tradeMatch.number",				# The order of this match if example if value of 2 this is the second order matched
	"tradeMatch.price",					# The price the match occurred at
	"tradeMatch.orderID",				# The Order ID only available when trader ops in
	"tradeMatch.auxillaryID",
	"tradeMatch.quantity",				# The amount filled in this match
	"tradeMatch.flags",

	"volumeUpdate.volume",				# Represents cumulative traded volume of the Daily Trade session	
	"volumeUpdate.vwap",				# No value for CME data

	# bookLevel represent quote messages for messages within the first 10 levels of the book and give details about the type of book event that occured and the make up of the book at that price level
	"bookLevel.price",					# Price at which the quote event occurred
	"bookLevel.quantity",				# Total quantity at this book level after this event
	"bookLevel.orders",					# Number of orders at this book level after this event
	"bookLevel.impliedQuantity",
	"bookLevel.impliedOrders",
	"bookLevel.level",					# The number of price levels away from the market at which the event occurred
	"bookLevel.action",					# What occurred in the book.  It can be New, Delete or Change 
	"bookLevel.type",					# Is it a Bid or an Offer.
	"bookLevel.isEndEvent",				# EOE (end-of-Event) appears when more than one book update comes on the same message and is used to announce the end of book updates for the message.

	# orderBook represent quote messages at all price levels and give only details about that specific quote message
	"orderBook.orderID",				# Identification number of the order can be used to trace the life cycle of the order
	"orderBook.auxilaryID",				# Not in use for CME data
	"orderBook.priorityID",				# Order priority for execution on the order book. A lower value is a higher priority
	"orderBook.price",					# Price where the event occurred
	"orderBook.previousID",				# Not in use for CME data
	"orderBook.quantity",				# Visible quantity of an order to the market
	"orderBook.action",					# What occurred in the book. It can be overlay, new, delete, or change
	"orderBook.type",					# Side of the book. 0 = Bid And 1 = Offer
	"orderBook.isSnapshot",

	"securityStatus.group",				# Root symbol of the asset. EX: If pulling an option this will have the root of the option
	"securityStatus.asset",				# Unique instrument ID
	"securityStatus.sessionDate",		# Indicates the date of the trade session
	"securityStatus.type",				# 2 = Trading Halt, 4 = Close, 15 = New Price Indication, 17 = Ready to trade (Start of Session), 18 = Not available for trading, 20 = Unknown or Invalid, 21 = Pre-Open, 24 = Pre-Cross, 25 = Cross, 26 = Post Cross,103 = No Change
	"securityStatus.haltReason",		# 0 = Group schedule, 1 = Surveillance intervention, 2 = Market event, 3 = Instrument activation, 4 = Instrument expiration, 5 = Unknown, 6 = Recovery in Process
	"securityStatus.event",				# 0 = No Event (default), 1 = No Cancel, 4 = Change of trading session (reset statistics), 5 = Implied matching ON, 6 = Implied matching OFF
		
	"dailyStatistics.instrumentID",		# Unique ID given by the exchange used to Identify the contract 
	"dailyStatistics.price",			# for Settlement messages - Price of the product Settlement
	"dailyStatistics.size",				# for Open Interest messages - The total Open Interest, For Cleared Volumne - New The total volume
	"dailyStatistics.sessionDate",		# Date of trade session corresponding to the statistic entry
	"dailyStatistics.settleType",		# for settlement messages - Which type of settle price.
	"dailyStatistics.type",				# type of Statistice can be: Settlement, Open Interest, Fixed Price or Cleared Volume

	"sessionStatistics.instrumentID",	# Unique ID given by the exchange used to Identify the contract 
	"sessionStatistics.price",			# Price at which the statistic is referencing
	"sessionStatistics.stateType",		# Identifies Session Statisitc type: Opening Price, New High Bid or Low Ask, Session High or Low 
	"sessionStatistics.action",
	"sessionStatistics.type",			# Is this the opening price.  0=Daily Open Price, 5=Indicative Opening 
	"sessionStatistics.size",

	"limitsBanding.highLimit",			# the Limit High price for the current session 
	"limitsBanding.lowLimit",			# the Limit Low price for the current session 
	"limitsBanding.maxVariation",

	"clearingPrice.price",
	"clearingPrice.quantity"	
]
#--------------------------------------------------------


#--------------------------------------------------------
# Enums
#--------------------------------------------------------

class Trigger(IntEnum):
	IcebergOrders				= 1
	TradeSweeps					= 2
	StopOrders					= 4
	Trades						= 8
	Summary						= 16

class Bucket(IntEnum):
	Summary						= 1

class Session(IntEnum):
	Current						= 0
	Previous					= 1  
      
class SideType(IntEnum):
	Ask							= 0
	Bid							= 1

class Aggressor(IntEnum):
	NoAggressor					= 0
	Buy							= 1
	Sell						= 2

class HaltReason(IntEnum):
	NotSet						= 255
	GroupSchedule				= 0
	SurveillanceIntervention	= 1
	MarketEvent					= 2
	InstrumentActivation		= 3
	InstrumentExpiration		= 4
	Unknown						= 5
	RecoveryInProcess			= 6

class SecurityType(IntEnum):
	NotSet						= 0
	TradingHalt					= 2
	Close						= 4
	NewPriceIndication			= 15
	ReadyToTrade				= 17
	NotAvailableForTrading		= 18
	UnknownorInvalid			= 20
	PreOpen						= 21
	PreCross					= 24
	Cross						= 25
	PostClose					= 26
	NoChange					= 103
	# ICE
	PreClose					= 150
	# Eurex
	Restricted					= 200
	Freeze						= 201

class SecurityEvent(IntEnum):
	NoEvent						= 0
	NoCancel					= 1
	ResetStatistics				= 4
	ImpliedMatchingON			= 5
	ImpliedMatchingOFF			= 6

class BookType(Enum):
	NotSet						= 'U'
	Bid							= 'B'
	Ask							= 'S'
	ImpliedBid					= 'b'
	ImpliedAsk					= 's'
	BookReset					= 'R'

class DailyStatisticsType(Enum):
    SettlementPrice				= '6'
    ClearedVolume				= 'B'
    OpenInterest				= 'C'
    FixingPrice					= 'W'

class SessionStatisticsType(IntEnum):
    NotSet						= 127
    OpenPrice					= 0
    HighTrade					= 1
    LowTrade					= 2
    LastTrade					= 3
    HighestBid					= 4
    LowestAsk					= 5
    ClosePrice					= 6

class BookAction(IntEnum):
    NotSet						= 255
    New							= 0
    Change						= 1
    Delete						= 2
    DeleteThru					= 3
    DeleteFrom					= 4
    Overlay						= 5
    Replace						= 6

class StateType(IntEnum):
    NotSet						= 255
    DailyOpenPrice				= 0
    IndicativeOpeningPrice		= 5
    DailyClosePrice				= 10

class PutOrCall(IntEnum):
    NotSet						= 255
    Put							= 0
    Call						= 1

class SettleType(IntEnum):
    Final						= 0x01
    Actual						= 0x02
    Rounded						= 0x04
    Intraday					= 0x08
    ReservedBits				= 0x10
    NullValue					= 0x80

class TransactionType(IntEnum):
    NotSet						= 255
    TransactionStart			= 0
    TransactionEnd				= 1

class EventIndicator(IntEnum):
    NotSet						= 0x0
    LastOfType					= 1
    EndOfEvent					= 0x80

class InvestigateStatus(IntEnum):
    NotSet						= 0x0
    UnderInvestigation			= 1
    InvestigationCompleted		= 2

class UnionID(IntEnum):
	NotSet						= 255
	NotMapped					= 250
	TradeSummary				= 0
	TradeMatch					= 1
	VolumeUpdate				= 2
	BookLevel					= 3
	OrderBook					= 4
	SecurityStatus				= 5
	DailyStatistics				= 6
	SessionStatistics			= 7
	LimitsBanding				= 8
	ChannelReset				= 9
	TransactionMarker			= 10
	ClearingPrice				= 12 

#--------------------------------------------------------
# Predefined FID definitions
#--------------------------------------------------------

"""

const static std::string   kFidsFull	=	R"xxxx(
{
	"CodeFids":[

		"header.instrumentID",
		"header.sequence",
		"header.time",
		"header.channelSequence",
		"header.instrumentSequence",
		"header.unionID",
		"header.eventIndicator",
		"header.flag",
		"header.baseExponent",

		"transactionMarker.type",

		"channelReset.type",

		"tradeSummary.price",
		"tradeSummary.quantity",
		"tradeSummary.matches",
		"tradeSummary.aggressor",
		"tradeSummary.isImplied",
		"tradeSummary.isSnapshot",
		"tradeSummary.volume",

		"tradeMatch.isAggressor",
		"tradeMatch.number",
		"tradeMatch.price",
		"tradeMatch.orderID",
		"tradeMatch.auxillaryID",
		"tradeMatch.quantity",
		"tradeMatch.flags",

		"volumeUpdate.volume",	
		"volumeUpdate.vwap",

		"bookLevel.price",
		"bookLevel.quantity",
		"bookLevel.orders",
		"bookLevel.impliedQuantity",
		"bookLevel.impliedOrders",
		"bookLevel.level",
		"bookLevel.action",
		"bookLevel.type",
		"bookLevel.isEndEvent",

		"orderBook.orderID",
		"orderBook.auxilaryID",
		"orderBook.priorityID",
		"orderBook.price",
		"orderBook.previousID",
		"orderBook.quantity",
		"orderBook.action",
		"orderBook.type",
		"orderBook.isSnapshot",

		"securityStatus.group",
		"securityStatus.asset",
		"securityStatus.sessionDate",
		"securityStatus.type",	
		"securityStatus.haltReason",
		"securityStatus.event",	

		"dailyStatistics.instrumentID",
		"dailyStatistics.price",
		"dailyStatistics.size",
		"dailyStatistics.sessionDate",
		"dailyStatistics.settleType",
		"dailyStatistics.type",	

		"sessionStatistics.instrumentID", 
		"sessionStatistics.price",
		"sessionStatistics.stateType",
		"sessionStatistics.action",
		"sessionStatistics.type",
		"sessionStatistics.size",

		"limitsBanding.highLimit",
		"limitsBanding.lowLimit",
		"limitsBanding.maxVariation",

		"clearingPrice.price",
		"clearingPrice.quantity"		

	]
}

)xxxx";



const static  std::string   kFidsNorm	=	R"xxxx(
{
	"CodeFids":[

		"header.instrumentID",
		"header.sequence",
		"header.time",
		"header.channelSequence",
		"header.instrumentSequence",
		"header.unionID",
		"header.eventIndicator",
		"header.flag",
		"header.baseExponent",

		"transactionMarker.type",

		"channelReset.type",

		"tradeSummary.price",
		"tradeSummary.quantity",
		"tradeSummary.matches",
		"tradeSummary.aggressor",
		"tradeSummary.isImplied",
		"tradeSummary.isSnapshot",
		"tradeSummary.volume",

		"tradeMatch.isAggressor",
		"tradeMatch.number",
		"tradeMatch.price",
		"tradeMatch.orderID",
		"tradeMatch.auxillaryID",
		"tradeMatch.quantity",
		"tradeMatch.flags",

		"volumeUpdate.volume",	
		"volumeUpdate.vwap",

		"orderBook.orderID",
		"orderBook.auxilaryID",
		"orderBook.priorityID",
		"orderBook.price",
		"orderBook.previousID",
		"orderBook.quantity",
		"orderBook.action",
		"orderBook.type",
		"orderBook.isSnapshot",

		"securityStatus.group",
		"securityStatus.asset",
		"securityStatus.sessionDate",
		"securityStatus.type",	
		"securityStatus.haltReason",
		"securityStatus.event",	

		"dailyStatistics.instrumentID",
		"dailyStatistics.price",
		"dailyStatistics.size",
		"dailyStatistics.sessionDate",
		"dailyStatistics.settleType",
		"dailyStatistics.type",	

		"sessionStatistics.instrumentID", 
		"sessionStatistics.price",
		"sessionStatistics.stateType",
		"sessionStatistics.action",
		"sessionStatistics.type",
		"sessionStatistics.size",

		"limitsBanding.highLimit",
		"limitsBanding.lowLimit",
		"limitsBanding.maxVariation",

		"clearingPrice.price",
		"clearingPrice.quantity"		

	]
}

)xxxx";



const static  std::string   kFidsTrds	=	R"xxxx(
{
	"CodeFids":[

		"header.instrumentID",
		"header.sequence",
		"header.time",
		"header.unionID",

		"tradeSummary.price",
		"tradeSummary.quantity",
		"tradeSummary.matches",
		"tradeSummary.aggressor",
		"tradeSummary.isImplied",
		"tradeSummary.isSnapshot",
		"tradeSummary.volume"
	
	]
}

)xxxx";


"""


#--------------------------------------------------------
# c++ Structs Reference
#--------------------------------------------------------

"""

struct TransactionMarker
{
    uint8_t			type;
};

struct ChannelReset
{
    uint8_t				type;
};

struct TradeSummary
{
    double					price;
    int32_t					quantity;
    uint32_t				matches;
    uint8_t					aggressor;
    bool					isImplied;
    bool					isSnapshot;
    uint32_t				volume; // sometimes trades contain volume;
};

struct TradeMatch
{
    bool					isAggressor;
    uint16_t				number;
    double					price;
    uint64_t				orderID;
    uint64_t				auxillaryID; // ice secondary, originating order
    int32_t					quantity;
    int32_t					flags;
};

struct VolumeUpdate
{
    uint32_t				volume;
    double					vwap; // ice stat metric
};

struct BookLevel
{
    double					price;
    int32_t					quantity;
    int32_t					orders;
    int32_t					impliedQuantity;
    int32_t					impliedOrders;
    uint8_t					level;
    uint8_t					action;
    uint8_t					type;
    bool					isEndEvent;
};

struct OrderBook
{
    uint64_t				orderID;
    uint64_t				auxilaryID; // needed for ice, eurex
    uint64_t				priorityID;
    double					price;
    uint64_t				previousID;  // eurex only
    int32_t					quantity;
    uint8_t					action;
    uint8_t					type;
    bool					isSnapshot;
};

struct SecurityStatus
{
    char					group[10];
    char					asset[10];
    uint16_t				sessionDate;
    uint8_t					type;
    uint8_t					haltReason;
    uint8_t					event;
};

struct DailyStatistics
{
    uint32_t				instrumentID; 
    double					price;
    int32_t					size;
    uint16_t				sessionDate;  // Reference for the date it occured
    uint8_t					settleType;
    uint8_t					type;
};

struct LimitsBanding
{
    double					highLimit;
    double					lowLimit;
    double					maxVariation;
};

struct SessionStatistics
{
    uint32_t				instrumentID; 
    double	                price;
    uint8_t					stateType;
    uint8_t					action;
	uint8_t					type;
    int32_t                 size;
};

struct ClearingPrice   // eurex
{
    double					price;
    uint32_t				quantity;
};

struct Header
{
	uint32_t				instrumentID		= 0;
	uint32_t				sequence			= 0;
	uint64_t				time				= 0;
	uint32_t				channelSequence		= 0;
	uint32_t				instrumentSequence	= 0;
	uint8_t					unionID				= 0;
	uint8_t					eventIndicator		= 0;
	bool					flag				= false;
	uint8_t					baseExponent		= 0;
};

struct Event
{

	Header					header;

    TradeSummary			tradeSummary;
    TradeMatch				tradeMatch;
    VolumeUpdate			volumeUpdate;
    BookLevel				bookLevel;
    OrderBook				orderBook;
    SecurityStatus			securityStatus;
    DailyStatistics			dailyStatistics;
    LimitsBanding			limitsBanding;
    SessionStatistics		sessionStatistics;
    ChannelReset			channelReset;
    TransactionMarker		transactionMarker;
    ClearingPrice			clearingPrice;

};

"""