#!/usr/bin/python
import json
from bson import json_util
from bottle import route, run, request, abort
from pymongo import MongoClient

# Establish database and collection for new document
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']
docs = collection.find({})

# Get all stocks in the collection
stock_list = []
for document in docs:
    stock_list.append(document)
stocks = json.loads(json_util.dumps(stock_list))


# http://localhost:8080/stocks/api/v1.0/createStock/
@route('/stocks/api/v1.0/createStock/<ticker>', method='POST')
def createStock(ticker):
    try:
        # Create new document for stock in path parameter
        new_stock = {'Ticker': ticker, 'Sector': request.json.get('Sector')}
        collection.insert_one(new_stock)
        stocks.append(new_stock)
        found_stock = collection.find_one(new_stock)
        return json_util.dumps(found_stock, indent=4)
    except Exception as e:
        abort(400, e)


# http://localhost:8080/stocks/api/v1.0/getStock/
@route('/stocks/api/v1.0/getStock/<ticker>', method='GET')
def getStock(ticker):
    try:
        # Get stock from path parameter
        the_stock = [stock for stock in stocks if stock['Ticker'] == ticker]
        if the_stock != '':
            found_stock = collection.find_one({"Ticker": the_stock[0]['Ticker']})
            return json_util.dumps(found_stock, indent=4)
        else:
            abort(404, 'No data for ticker symbol %s' % ticker)
    except Exception as e:
        abort(400, e)


# http://localhost:8080/stocks/api/v1.0/updateStock/
@route('/stocks/api/v1.0/updateStock/<ticker>', method='GET')
def updateStock(ticker):
    try:
        # Get stock from path parameter and update the volume
        query = {'Ticker': ticker}
        new_vol = {"$set": {"Volume": 999999999999999999}}
        collection.update_one(query, new_vol)
        updated_stock = collection.find_one(query)
        return json_util.dumps(updated_stock, indent=4)
    except Exception as e:
        abort(400, e)


# http://localhost:8080/stocks/api/v1.0/deleteStock/
@route('/stocks/api/v1.0/deleteStock/<ticker>', method='delete')
def deleteStock(ticker):
    try:
        # Get stock from path and delete the stock data in list & db
        the_stock = [stock for stock in stocks if stock['Ticker'] == ticker]
        if the_stock != '':
            collection.delete_one({"Ticker": the_stock[0]['Ticker']})
            stocks.remove(the_stock[0])
            return json_util.dumps(stocks, indent=4)
        else:
            abort(404, 'The ticker does not exist in the system.')
    except Exception as e:
        abort(400, e)
        return False


# http://localhost:8080/stocks/api/v1.0/stockReport?tickers=['AAPL','BA']
@route('/stocks/api/v1.0/stockReport', method='GET')
def stockReport():
    try:
        # Get tickers from query parameters & format
        tickers = request.query.tickers
        symbols = list(tickers.strip("][").replace(',', ' ').replace("'", '').split(' '))
        findStr = {"Ticker": {"$in": symbols}}
        print(findStr)
        result = collection.find(findStr)
        return json_util.dumps(list(result), indent=4)
    except Exception as e:
        abort(400, e)
        return False


# http://localhost:8080/stocks/api/v1.0/industryReport/Shipping
@route('/stocks/api/v1.0/industryReport/<industry>', method='GET')
def industryReport(industry):
    try:
        # Get list of stocks for specified industry in path parameter
        industries = {"Industry": industry}
        tickers = collection.find(industries)
        return json_util.dumps(list(tickers), indent=4)
    except Exception as e:
        abort(400, e)
        return False


# http://localhost:8080/stocks/api/v1.0/portfolio/Apple Inc.
@route('/stocks/api/v1.0/portfolio/<name>', method='GET')
def portfolio(name):
    try:
        # Get stock portfolio for company name
        findStr = {"Company": name}
        result = collection.find(findStr, {"Ticker": 1, "Industry": 2, "Shares Outstanding": 3, "50-Day Simple Moving Average": 4, "Sector": 5, "_id": 0}).limit(5)
        return json_util.dumps(list(result), indent=4)
    except Exception as e:
        abort(400, e)
        return False


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True, debug=True)
