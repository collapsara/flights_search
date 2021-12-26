from app.core.crud import get_rate_value_by_currency_name


def set_price_by_currency(db, search_response, currency):

    for i in range(len(search_response)):
        current_currency = search_response[i]["pricing"]["currency"]
        total_price = float(search_response[i]["pricing"]["total"])
        rate = get_rate_value_by_currency_name(db, currency)
        currency_price = rate.description if rate else None
        current_rate = get_rate_value_by_currency_name(db, current_currency)
        current_currency_price = current_rate.description if current_rate else None
        
        if current_currency == currency:
            price_amount = total_price
        elif currency == 'KZT':
            price_amount = f"{(total_price * current_currency_price):.2f}"          
        else:
            if current_currency == "KZT":
                price_amount = f"{(total_price / currency_price):.2f}"
            else:
                price_amount = f"{(total_price / current_currency_price) * currency_price:.2f}"

        price = {
            "price":{
                "amount": price_amount,
                "currency": currency,
            }
        }
        search_response[i].update(price)
    return sorted(search_response, key=lambda k: float(k["price"]["amount"]))
