# MySQL DB
MYSQL_DB_NAME = 'cointreau'
MYSQL_HOST = '127.0.0.1'
BANKROLL_TABLE = 'bankroll'
BANKROLL_CURRENCY = 'currency'
BANKROLL_AMOUNT = 'amount'
BANKROLL_USD = 'USD'
BANKROLL_ETH = 'ETH'
BANKROLL_BTC = 'BTC'
TRANSACTIONS_TABLE = 'transactions'
PENDING_ORDERS_TABLE = 'pending_orders'
PENDING_ORDERS_ORDER_ID = 'order_id'

# InfluxDB
INFLUXDB_DB_NAME = 'cointreau'
INFLUXDB_HOST = '127.0.0.1'
INFLUXDB_PORT = 8086
INFLUXDB_USER = 'root'
INFLUXDB_PASS = 'root'
INFLUXDB_MEASUREMENT = 'measurement'
INFLUXDB_TAGS = 'tags'
INFLUXDB_FIELDS = 'fields'
INFLUXDB_MEASUREMENT_BANKROLL = 'bankroll'
INFLUXDB_MEASUREMENT_PREDICTIONS = 'predictions'
INFLUXDB_TAGS_CURRENCY = 'currency'
INFLUXDB_TAGS_TYPE = 'type'
INFLUXDB_TAGS_PREDICTED = 'predicted'
INFLUXDB_TAGS_ACTUAL = 'actual'
INFLUXDB_TAGS_ERROR = 'error'
INFLUXDB_FIELDS_AMOUNT = 'amount'
INFLUXDB_FIELDS_VALUE = 'value'

# GDAX
GDAX_MESSAGE = 'message'
GDAX_ASK = 'ask'
GDAX_BID = 'bid'
GDAX_ID = 'id'
GDAX_SIZE = 'size'
GDAX_PRODUCT_ID = 'product_id'
GDAX_SIDE = 'side'
GDAX_TYPE = 'type'
GDAX_CREATED_AT = 'created_at'
GDAX_DONE_AT = 'done_at'
GDAX_DONE_REASON = 'done_reason'
GDAX_FILL_FEES = 'fill_fees'
GDAX_FILLED_SIZE = 'filled_size'
GDAX_EXECUTED_VALUE = 'executed_value'
ORDER_BUY = 'buy'
ORDER_SELL = 'sell'
ORDER_LIMIT = 'limit'
