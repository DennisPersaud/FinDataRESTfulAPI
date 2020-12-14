# FinDataRESTfulAPI
This is a stock market RESTful API that I developed using Python's bottle library &amp; MongoDB. This API allows the user to perform simple CRUD operations on a MongoDB database containing financial data. It also provides endpoints for the user to generate simple reports using the fiancial information stored in the database.

## Create
In the stock_API.py file, I created a function called “createStock” to handle the POST request for the URI path /stocks/api/v1.0/industryReport/<ticker>. This endpoint function allows the user to create a new document in the database by passing the ticker name at the end of the path and json data specified by the user. In the example below I passed TEST as the ticker name at the end of the post request, and included some JSON data in the body of the request. In this example I set the Sector for this new ticker to “TEST’. The document that was created is then returned to the user.
![Create](https://i.imgur.com/uvZbK2I.jpg)

## Read
In the stock_API.py file, I create a function called “getStock” to handle the GET request for the URI path /stocks/api/v1.0/ getStock/<ticker>. This endpoint function allows the user to get a document for a ticker by specifying a ticker symbol at the end of the path. The ticker is then passed to the function which retrieves the associated document from the database and displays it to the user. In the example below “AAPL” is added to the end of the path and it’s associated document is returned from the database.
![Read](https://i.imgur.com/UsMc56m.jpg)

## Update
In the stock_API.py file, I created a function called “updateStock” to handle the GET request for the URI path /stocks/api/v1.0/ updateStock/<ticker>. This endpoint function allows the user to update a document in the database by specifying a ticker symbol at the end of the URI path. When this function is called it updates the “Volume” with a predefined value in the specified ticker’s document, the updated document is then returned to the user. 
![Update](https://i.imgur.com/7jqdIHg.jpg)

## Delete
In the stock_API.py file, I created a function named “deleteStock” to handle the delete request for the URI path /stocks/api/v1.0/ updateStock/<ticker>. This endpoint function allows the user to delete a document in the database by passing a ticker symbol at the end of the URI path. The function then deletes the ticker from the database and prints a list of all the remaining documents in the database. In the example below “TESTNAME” is passed a path parameter and the function deletes the document with the Ticker “TESTNAME” from the database.
![Delete](https://i.imgur.com/MVodTvE.jpg)
  
## Stock Report
In the stock_API.py file, I created a function named “stockReport” to handle the GET request for the URI path /stocks/api/v1.0/stockReport. This endpoint function takes a query parameter as an argument, the query parameter used for this function requires that the user send a list for tickers that they would like to receive a report for. When the specified tickers are passed as a query parameter the function formats the string and converts into a list. The list of ticker symbols is then used by the function to retrieve the reports related to those ticker symbols in the database. In example below SPY and QQQ are passed as a query parameter in the request and the function returns the reports for the requested tickers.
![StockReport](https://i.imgur.com/klEx1ds.jpg)

## Industry Report
In the stock_API.py file, I created a function called “industryReport” to handle the GET request for the URI path /stocks/api/v1.0/industryReport/<industry>. This endpoint function takes a path parameter as an argument, the path parameter for this function requires that the user specify the industry that they would like to receive a report of stocks for. In the example below I specified the “Shipping” industry at the end of the path and the function returned a report of all of the data for all of the tickers in that industry.
![IndustryReport](https://i.imgur.com/RI9vejc.jpg)

## Stock Portfolio
In the stock_API.py file, I created a function called portfolio to handle the GET request for the URI path /stocks/api/v1.0/portfolio/<name>. This endpoint function takes a path parameter as an argument, the user is required to specify the company name that they would like to receive a report for. In the example below I specified the company name at the end of the path as “Apple Inc.” and the function returned a report for that company name.
![StockPortfolio](https://i.imgur.com/bB01TZZ.jpg)
