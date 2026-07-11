from zipline.api import order_target, record, symbol
import random

def initialize(context):
    context.asset = symbol("AAPL")

def handle_data(context, data):
    if random.random() > 0.5:
        order_target(context.asset, 100)
    else:
        order_target(context.asset, 0)

    record(AAPL=data.current(context.asset, "price"))
