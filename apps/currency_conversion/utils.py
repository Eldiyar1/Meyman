from rest_framework import viewsets, status 
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup as bs
import re
from dateutil.parser import parse 
from .serializers import CurrencyConversionSerializer


class CurrencyiewSet(viewsets.ModelViewSet):
    serializer_class = CurrencyConversionSerializer

    # def get_queryset(self):
    #     return None  
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            currency_1 = serializer.validated_data['currency_1']
            currency_2 = serializer.validated_data['currency_2']
            amount = serializer.validated_data['amount']
            
            last_updated_datetime, exchange_rate = self.convert_currency_xe(currency_1, currency_2, amount)
            
            response_data = {
                "last_updated_datetime": last_updated_datetime,
                "exchange_rate": exchange_rate
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def convert_currency_xe(self, src, dst, amount):
        def get_digits(text):
            """Returns the digits and dots only from an input `text` as a float
            Args:
                text (str): Target text to parse
            """
            new_text = ""
            for c in text:
                if c.isdigit() or c == ".":
                    new_text += c
            return float(new_text)
        
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={src}&To={dst}"
        content = requests.get(url).content
        soup = bs(content, "html.parser")
        exchange_rate_html = soup.find_all("p")[2]
        # get the last updated datetime
        last_updated_datetime = parse(re.search(r"Last updated (.+)", exchange_rate_html.parent.parent.find_all("div")[-2].text).group()[12:])
        return last_updated_datetime, get_digits(exchange_rate_html.text) 


