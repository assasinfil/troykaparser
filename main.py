import json
from datetime import datetime, timedelta

f = open("data.json")

data = json.load(f)


def get_num(data):
    return int(data, 2)


def get_hex(data):
    return hex(get_num(data))


bitmap = {'0x1c5': {
    'start_year': 2019,
    'id': {'start': 20, 'end': 52},
    'valid_to_date': {'start': 61, 'end': 74},
    'travel_time': {'start': 129, 'end': 151},
    'validator': {'start': 186, 'end': 202},
    'balance': {'start': 167, 'end': 186}
}}


def parse_transport_block(block):
    binary_block = format(int(block, 16), '0' + str(len(block) * 4) + 'b')

    departament_app_id = get_hex(binary_block[0:10])
    if departament_app_id not in ["0x106", "0x108", "0x10a", "0x10e", "0x110", "0x117"]:
        return None

    bitmap_id = get_hex(binary_block[52:52 + 4])
    if bitmap_id == '0xe':
        bitmap_id = get_hex(binary_block[52:52 + 9])
    elif bitmap_id == '0xf':
        bitmap_id = get_hex(binary_block[52:52 + 14])
    selected_bitmap = bitmap[bitmap_id]
    card_number = get_num(binary_block[selected_bitmap['id']['start']:selected_bitmap['id']['end']])
    valid_to_days = get_num(
        binary_block[selected_bitmap['valid_to_date']['start']:selected_bitmap['valid_to_date']['end']])
    valid_to_date = datetime(selected_bitmap['start_year'], 1, 1, 0, 0) + timedelta(days=valid_to_days - 1)
    travel_from_minutes = get_num(
        binary_block[selected_bitmap['travel_time']['start']:selected_bitmap['travel_time']['end']])
    travel_from_time = datetime(selected_bitmap['start_year'], 1, 1, 0, 0) + timedelta(
        minutes=travel_from_minutes) - timedelta(days=1)

    validator_id = get_num(binary_block[selected_bitmap['validator']['start']:selected_bitmap['validator']['end']])
    balance = get_num(binary_block[selected_bitmap['balance']['start']:selected_bitmap['balance']['end']]) / 100

    print(f"Номер карты: {card_number} до {valid_to_date.strftime('%d.%m.%Y')}")
    print(f"Баланс: {balance}")
    print(f"Поездка с: {travel_from_time}, валидатор: {validator_id}")


parse_transport_block(data['blocks']['32'] + data['blocks']['34'] + data['blocks']['35'])
