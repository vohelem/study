from decimal import Decimal
from datetime import datetime, timedelta

DATE_FORMAT = '%Y-%m-%d'

goods = {
    'Пельмени Универсальные': 
    [
        {'amount': Decimal('0.5'), 'expiration_date': datetime(2023, 7, 15).date()},
        {'amount': Decimal('2'), 'expiration_date': datetime(2023, 8, 1).date()}
    ],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': datetime(2024, 4, 8).date()}],
    'Воsdfsdfsdfда': [{'amount': Decimal('1.5'), 'expiration_date': datetime(2024, 4, 9).date()}],
    'Ракушка': [{'amount': Decimal('1.5'), 'expiration_date': datetime(2024, 8, 4).date()}]
} 

def add(items, title, amount, expiration_date=None):
    date = datetime.strptime(expiration_date, DATE_FORMAT).date() if expiration_date != None else None
    (items[title].append({'amount': amount, 'expiration_date': date})
    if title in items.keys()
    else items.update({title: [{'amount': amount, 'expiration_date': date}]}))
    return items

def add_by_note(items, note):
    title = ''
    amount = 0
    expiration_date = None
    parse_string = note.split(' ')
    if note[-3] == '-':
        expiration_date = parse_string[-1]
        del parse_string[-1]
    amount = Decimal(parse_string[-1])
    del parse_string[-1]
    title = ' '.join(parse_string)
        
    add(items, title=title, amount=amount, expiration_date=expiration_date)


def find(items, needle):
    result = []
    for item in items.keys():
        if str.lower(needle) in str.lower(item):
            result.append(item)
    return result


def amount(items, needle):
    all_amount = Decimal('0')
    all_find_items = find(items, needle)
    for one_items in all_find_items:
        for item in items[one_items]:
            all_amount += item['amount']
    return all_amount


def expire(items, in_advance_days=0):
    result = []
    now = datetime.today().date()
    expire_date = now + timedelta(days=in_advance_days)
    for item in items:
        amount = Decimal('0')
        for it in items[item]:
            if it['expiration_date'] is None:
                continue
            if it['expiration_date'] <= expire_date:
                amount += it['amount']
        if amount > 0:
            result.append((item, amount))
    return result
    
print(expire(goods))