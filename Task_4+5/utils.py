from requests import get, utils


def currency_rates(cur_name):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    cur_name_index = content.find(cur_name.upper())  # Здесь приводим к заглавным буквам
    if cur_name_index != -1:
        tag1_index = content.find("<Value>", cur_name_index)  # Ищем <Value>, начиная от найденного имени валюты
        tag1_length = 7
        tag2_index = content.find("</Value>", tag1_index + tag1_length)  # Неизвестно общее кол-во цифр в курсе валюты, только точность - 4 цифры, поэтому поиск
        currency = float(content[tag1_index + tag1_length: tag2_index].replace(",", "."))
        # Можно использовать Decimal, если нам нужна максимальная точно значений после запятой(если после запятой много значений)
        return currency
    else:
        return None

if __name__ == '__main__':
    print(currency_rates("USd"))
    print(currency_rates("CAD"))
    print(currency_rates("HKD"))
    print(currency_rates("SeK"))
    print(currency_rates("JPY"))
    print(currency_rates("Че такой кислый? Арбуз будешь?"))
    print(currency_rates("ZAR"))
    print(currency_rates("CZK"))
