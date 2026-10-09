from datetime import datetime


def generate_member_id():
    return datetime.now().strftime("member-%Y%m%d-%H%M%S")
