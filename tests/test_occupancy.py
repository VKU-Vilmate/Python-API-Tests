from driver import driver
from conftest import login
from django.django_page import DjangoPage
from utilities.requestUtility import RequestUtility
from data import endpoints as ep
from data import payloads as pl
from data import date as d


def remove_project(driver):
    django = DjangoPage(driver,
                        ep.DJANGO_ADMIN)

    django.open()
    return django.remove_dev_project()


def check_statuses_and_delete(driver):
    django = DjangoPage(driver,
                        ep.DJANGO_ADMIN)

    django.open()
    return django.check_dates_and_remove()


class TestOccupancy:

    def test_change_occupancy_in_previous_month(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="true",
                month=d.past_date(6)[0],
                year=d.past_date(6)[1],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(create_project[0]["is_full_time"]) == "True"

        user_id = create_project[0]["user"]["id"]
        dev_project_id = create_project[0]["id"]

        change_occupancy_three_months_back = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.update_dev_project(
                is_full_time='false',
                month=d.past_date(3)[0],
                year=d.past_date(3)[1],
                is_active='true'
            ),
            headers=pl.authorization(key),
            expected_status_code=200)
        assert str(change_occupancy_three_months_back["is_full_time"]) == "False"

        check_occupancy_current_month = req.get(endpoint=ep.dev_project_get(
            year=d.current_year(),
            month=d.current_month(),
            user_id=user_id
        ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(check_occupancy_current_month["items"]["reports"][0]["is_full_time"]) == "False"

        check_occupancy_six_months_back = req.get(endpoint=ep.dev_project_get(
            year=d.past_date(6)[1],
            month=d.past_date(6)[0],
            user_id=user_id
        ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(check_occupancy_six_months_back["items"]["reports"][0]["is_full_time"]) == "True"

        remove_project(driver)

    def test_check_statuses_dates(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="true",
                year=d.past_date(6)[1],
                month=d.past_date(6)[0],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )
        assert str(create_project[0]["is_full_time"]) == "True"

        dev_project_id = create_project[0]["id"]

        change_occupancy_3_month_back = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.update_dev_project(
                is_full_time="false",
                month=d.past_date(3)[0],
                year=d.past_date(3)[1],
                is_active="true"
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )

        assert str(change_occupancy_3_month_back["is_full_time"]) == "False"

        change_occupancy_2_month_back = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.update_dev_project(
                is_full_time="true",
                month=d.past_date(2)[0],
                year=d.past_date(2)[1],
                is_active="true"
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(change_occupancy_2_month_back["is_full_time"]) == "True"

        day_1, day_2, day_3 = check_statuses_and_delete(driver)
        assert day_1 == '01'
        assert day_2 == '01'
        assert day_3 == '01'

    def test_check_salary_hours(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(endpoint=ep.CREATE_DEV_PROJECT,
                                  payload=pl.create_dev_project(
                                      is_full_time="true",
                                      year=d.current_year(),
                                      month=d.current_month(),
                                      date=d.string_date(0)
                                  ),
                                  headers=pl.authorization(key),
                                  expected_status_code=200)

        assert str(create_project[0]["is_full_time"]) == 'True'

        dev_project_id = create_project[0]["id"]
        project_id = create_project[0]["project"]["id"]

        create_work_item = req.post(endpoint=ep.CREATE_WORK_ITEM,
                                    payload=pl.create_work_item(dev_project_id,
                                                                d.string_date(0)),
                                    headers=pl.authorization(key),
                                    expected_status_code=201
                                    )

        get_consolidated_report = req.get(endpoint=ep.consolidated_report_get(
            year=d.current_year(),
            month=d.current_month(),
            project_id=project_id
        ),
            headers=pl.authorization(key),
            expected_status_code=200
        )
        print(str(get_consolidated_report))
        assert str(get_consolidated_report["items"][0]["total_minutes"]) == '180'
        assert str(get_consolidated_report["items"][0]["full_time_minutes"]) == '180'
        assert str(get_consolidated_report["items"][0]["overtime_minutes"]) == '0'

        remove_project(driver)

    def test_check_hourly_hours(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(endpoint=ep.CREATE_DEV_PROJECT,
                                  payload=pl.create_dev_project(
                                      is_full_time="false",
                                      year=d.current_year(),
                                      month=d.current_month(),
                                      date=d.string_date(0)
                                  ),
                                  headers=pl.authorization(key),
                                  expected_status_code=200)

        dev_project_id = create_project[0]["id"]
        project_id = create_project[0]["project"]["id"]

        create_work_item = req.post(endpoint=ep.CREATE_WORK_ITEM,
                                    payload=pl.create_work_item(dev_project_id,
                                                                d.string_date(0)),
                                    headers=pl.authorization(key),
                                    expected_status_code=201
                                    )

        get_consolidated_report = req.get(endpoint=ep.consolidated_report_get(
            year=d.current_year(),
            month=d.current_month(),
            project_id=project_id
        ),
            headers=pl.authorization(key),
            expected_status_code=200
        )
        print(str(get_consolidated_report))
        assert str(get_consolidated_report["items"][0]["total_minutes"]) == '180'
        assert str(get_consolidated_report["items"][0]["full_time_minutes"]) == '0'
        assert str(get_consolidated_report["items"][0]["overtime_minutes"]) == '180'

        remove_project(driver)

    def test_check_user_appearance(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="false",
                month=d.past_date(6)[0],
                year=d.past_date(6)[1],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        user_id = create_project[0]["user"]["id"]
        dev_project_id = create_project[0]["id"]

        delete_user_from_project = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.add_delete_user_from_project(
                month=d.past_date(4)[0],
                year=d.past_date(4)[1],
                is_active='false'
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(delete_user_from_project["is_active"]) == "False"

        create_project = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="true",
                month=d.past_date(2)[0],
                year=d.past_date(2)[1],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        check_dev_project_3_month_back = req.get(
            endpoint=ep.dev_project_get(
                year=d.past_date(3)[1],
                month=d.past_date(3)[0],
                user_id=user_id
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )

        assert int(check_dev_project_3_month_back["count_results"]) == 0

        check_dev_project_current_month = req.get(
            endpoint=ep.dev_project_get(
                year=d.current_year(),
                month=d.current_month(),
                user_id=user_id
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )

        assert str(check_dev_project_current_month["items"]["reports"][0]["is_full_time"]) == "True"

        remove_project(driver)

    def test_user_appearance_when_changing_occupancy(self, login, driver):
        key = login["token"]["key"]
        req = RequestUtility()

        create_project = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="true",
                month=d.past_date(6)[0],
                year=d.past_date(6)[1],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(create_project[0]["is_full_time"]) == "True"
        user_id = create_project[0]["user"]["id"]
        dev_project_id = create_project[0]["id"]

        delete_user_from_project = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.add_delete_user_from_project(
                month=d.past_date(4)[0],
                year=d.past_date(4)[1],
                is_active='false'
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(delete_user_from_project["is_active"]) == "False"

        add_user_back = req.post(
            endpoint=ep.CREATE_DEV_PROJECT,
            payload=pl.create_dev_project(
                is_full_time="true",
                month=d.past_date(2)[0],
                year=d.past_date(2)[1],
                date=d.string_date(0)
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(add_user_back[0]["is_full_time"]) == "True"

        change_occupancy_in_initial_month = req.patch(
            endpoint=ep.dev_project_patch(dev_project_id),
            payload=pl.update_dev_project(
                is_full_time='false',
                month=d.past_date(6)[0],
                year=d.past_date(6)[1],
                is_active='true'
            ),
            headers=pl.authorization(key),
            expected_status_code=200)

        assert str(change_occupancy_in_initial_month["is_full_time"]) == "False"

        check_dev_project_current_month = req.get(
            endpoint=ep.dev_project_get(
                year=d.current_year(),
                month=d.current_month(),
                user_id=user_id
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )

        assert str(check_dev_project_current_month["items"]["reports"][0]["is_full_time"]) == "False"

        check_occupancy_3_month_back = req.get(
            endpoint=ep.dev_project_get(
                month=d.past_date(3)[0],
                year=d.past_date(3)[1],
                user_id=user_id
            ),
            headers=pl.authorization(key),
            expected_status_code=200
        )

        assert int(check_occupancy_3_month_back["count_results"]) == 0

        remove_project(driver)
