import uuid
from data import parts


def validate_order(component_codes):
    categories = {
        "Screen": ["A", "B", "C"],
        "Camera": ["D", "E"],
        "Port": ["F", "G", "H"],
        "OS": ["I", "J"],
        "Body": ["K", "L"],
    }

    selected_categories = {category: False for category in categories}

    for code in component_codes:
        found = False
        for category, codes in categories.items():
            if code in codes:
                if selected_categories[category]:
                    return False
                selected_categories[category] = True
                found = True
                break
        if not found:
            return False

    return all(selected_categories.values())


def create_order(component_codes):
    if not validate_order(component_codes):
        raise ValueError("Invalid order configuration.")

    order_id = str(uuid.uuid4())
    total_price = 0.0
    parts_list = []

    for code in component_codes:
        part = parts[code]
        total_price += part["price"]
        parts_list.append(part["name"])

    return {
        "order_id": order_id,
        "total": total_price,
        "parts": parts_list
    }
