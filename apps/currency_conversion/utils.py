import requests
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup


def create_currency(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    amount = serializer.validated_data.get('amount')
    currency = serializer.validated_data.get('currency')

    BANK = "https://www.nbkr.kg/index.jsp?lang=RUS"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(BANK, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        convert = soup.find_all("td", {"class": "excurr", "class": "exrate"})
        usd = float(convert[0].text.replace(',', '.'))
        eur = float(convert[2].text.replace(',', '.'))
        rub = float(convert[4].text.replace(',', '.'))
        kzt = float(convert[6].text.replace(',', '.'))

        if currency == 'USD':
            result = amount / usd
        elif currency == 'EUR':
            result = amount / eur
        elif currency == 'RUB':
            result = amount / rub
        elif currency == 'KZT':
            result = amount / kzt
        else:
            result = 0.0

        data = {
            'amount': amount,
            'currency': currency,
            'result': result
        }
        return Response(data, status=status.HTTP_200_OK)

    except requests.RequestException:
        return Response({'error': 'Failed to fetch currency rates'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
