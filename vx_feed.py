
from enum import IntEnum, Enum

#--------------------------------------------------------
# Enums
#--------------------------------------------------------

class Aggressor(IntEnum):
	NoAggressor 				= 0
	buy 					= 1
	Sell 					= 2


class HaltReason(IntEnum):
	NotSet					= 255
	GroupSchedule				= 0
	SurveillanceIntervention		= 1
	MarketEvent				= 2
	InstrumentActivation			= 3
	InstrumentExpiration			= 4
	Unknown					= 5
	RecoveryInProcess			= 6


class SecurityType(IntEnum):
	NotSet					= 0
	TradingHalt				= 2
	Close					= 4
	NewPriceIndication			= 15
	ReadyToTrade				= 17
	NotAvailableForTrading			= 18
	UnknownorInvalid			= 20
	PreOpen					= 21
	PreCross				= 24
	Cross					= 25
	PostClose				= 26
	NoChange				= 103
	# ICE
	PreClose				= 150
	# Eurex
	Restricted				= 200
	Freeze					= 201


class SecurityEvent(IntEnum):
	NoEvent					= 0
	NoCancel				= 1
	ResetStatistics				= 4
	ImpliedMatchingON			= 5
	ImpliedMatchingOFF			= 6


class BookType(Enum):
	NotSet					= 'U'
	Bid					= 'B'
	Ask					= 'S'
	ImpliedBid				= 'b'
	ImpliedAsk				= 's'
	BookReset				= 'R'


class DailyStatisticsType(Enum):

    SettlementPrice				= '6'
    ClearedVolume				= 'B'
    OpenInterest				= 'C'
    FixingPrice					= 'W'


class SessionStatisticsType(IntEnum):

    NotSet					= 127
    OpenPrice					= 0
    HighTrade					= 1
    LowTrade					= 2
    LastTrade					= 3
    HighestBid					= 4
    LowestAsk					= 5
    ClosePrice					= 6


class BookAction(IntEnum):

    NotSet					= 255
    New						= 0
    Change					= 1
    Delete					= 2
    DeleteThru					= 3
    DeleteFrom					= 4
    Overlay					= 5
    Replace					= 6


class StateType(IntEnum):

    NotSet					= 255
    DailyOpenPrice				= 0
    IndicativeOpeningPrice			= 5
    DailyClosePrice				= 10


class PutOrCall(IntEnum):

    NotSet					= 255
    Put						= 0
    Call					= 1


class SettleType(IntEnum):

    Final					= 0x01
    Actual					= 0x02
    Rounded					= 0x04
    Intraday					= 0x08
    ReservedBits				= 0x10
    NullValue					= 0x80


class TransactionType(IntEnum):

    NotSet					= 255
    TransactionStart				= 0
    TransactionEnd				= 1


class EventIndicator(IntEnum):

    NotSet					= 0x0
    LastOfType					= 1
    EndOfEvent					= 0x80


class InvestigateStatus(IntEnum):

    NotSet					= 0x0
    UnderInvestigation				= 1
    InvestigationCompleted			= 2


class UnionID(IntEnum):

	NotSet					= 255
	NotMapped				= 250
	TradeSummary				= 0
	TradeMatch				= 1
	VolumeUpdate				= 2
	BookLevel				= 3
	OrderBook				= 4
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
//-----------------------------------------------------------------------------------------------------------=
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
//-----------------------------------------------------------------------------------------------------------=

//-----------------------------------------------------------------------------------------------------------=
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
//-----------------------------------------------------------------------------------------------------------=

//-----------------------------------------------------------------------------------------------------------=
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
//-----------------------------------------------------------------------------------------------------------=

"""


#--------------------------------------------------------
# c++ Structs Reference
#--------------------------------------------------------

"""

struct TransactionMarker
{
    uint8_t					type;
};

struct ChannelReset
{
    uint8_t					type;
};

struct TradeSummary
{
    double					price;
    int32_t					quantity;
    uint32_t					matches;
    uint8_t					aggressor;
    bool					isImplied;
    bool					isSnapshot;
    uint32_t					volume; // sometimes trades contain volume;
};

struct TradeMatch
{
    bool					isAggressor;
    uint16_t					number;
    double					price;
    uint64_t					orderID;
    uint64_t					auxillaryID; // ice secondary, originating order
    int32_t					quantity;
    int32_t					flags;
};

struct VolumeUpdate
{
    uint32_t					volume;
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
    uint64_t					orderID;
    uint64_t					auxilaryID; // needed for ice, eurex
    uint64_t					priorityID;
    double					price;
    uint64_t					previousID;  // eurex only
    int32_t					quantity;
    uint8_t					action;
    uint8_t					type;
    bool					isSnapshot;
};

struct SecurityStatus
{
    char					group[10];
    char					asset[10];
    uint16_t					sessionDate;
    uint8_t					type;
    uint8_t					haltReason;
    uint8_t					event;
};

struct DailyStatistics
{
    uint32_t					instrumentID; 
    double					price;
    int32_t					size;
    uint16_t					sessionDate;  // Reference for the date it occured
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
    uint32_t					instrumentID; 
    double	               			 price;
    uint8_t					stateType;
    uint8_t					action;
    uint8_t					type;
    int32_t                 			size;
};

struct ClearingPrice   // eurex
{
    double					price;
    uint32_t					quantity;
};

struct Header
{
	uint32_t				instrumentID		= 0;
	uint32_t				sequence		= 0;
	uint64_t				time			= 0;
	uint32_t				channelSequence		= 0;
	uint32_t				instrumentSequence	= 0;
	uint8_t					unionID			= 0;
	uint8_t					eventIndicator		= 0;
	bool					flag			= false;
	uint8_t					baseExponent		= 0;
};
//-----------------------------------------------------------------------------------------------------------=

//-----------------------------------------------------------------------------------------------------------=
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
    SessionStatistics			sessionStatistics;
    ChannelReset			channelReset;
    TransactionMarker			transactionMarker;
    ClearingPrice			clearingPrice;

};
//-----------------------------------------------------------------------------------------------------------=

"""
