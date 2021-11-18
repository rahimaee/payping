def Bearer(token=''):
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return header
