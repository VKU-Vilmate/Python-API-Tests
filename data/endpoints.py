DJANGO_ADMIN = 'https://dev-api-timetracking.vilmate.com/3MJBEYC80LHTDG9CDIPKORRZ5TDQ178A95E87UWV/'
CREATE_DEV_PROJECT = 'developer-projects/create-list/'
CREATE_WORK_ITEM = 'work_items/'


def dev_project_patch(dev_project_id):
    return 'developer-projects/' + str(dev_project_id) + '/'


def dev_project_get(year: int, month: int, user_id: str):
    return 'developer-projects/report/' + str(year) + '/' + str(month) + '/' + f'?user_id={user_id}'


def consolidated_report_get(year: int, month: int, project_id: str):
    return 'users-report/consolidated-report/' + str(year) + '/' + str(month) + '/' + f'?project_id={project_id}'
