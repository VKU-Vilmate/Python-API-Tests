def create_dev_project(is_full_time: str, year: int, month: int, date: str):
    return {
        "project": "dd75523f-a69d-4fac-80ab-158e55be798a",
        "users": [
            {
                "user_id": "d10d23b2-59b2-42fc-b13b-c8e05e4c2461",
                "is_full_time": is_full_time,
                "is_active": "true",
                "is_project_manager": "false",
                "date": date
            }
        ],
        "month": month,
        "year": year
    }


def update_dev_project(is_full_time: str, month: int, year: int, is_active: str):
    return {
        'is_full_time': is_full_time,
        'is_project_manager': 'false',
        'is_active': is_active,
        'month': month,
        'year': year
    }


def add_delete_user_from_project(month: int, year: int, is_active: str):
    return {
        'is_project_manager': 'false',
        'is_active': is_active,
        'month': month,
        'year': year
    }


def create_work_item(dev_project: str, date: str):
    return {
        "developer_project": dev_project,
        "title": "Autotest",
        "date": date,
        "duration": 180,
        "is_active": "true"
    }


def authorization(key):
    return {
        "Authorization": f"Bearer {key}"
    }
