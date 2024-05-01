from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday


class bdHolidayCalendar(AbstractHolidayCalendar):

    rules = [

        # USMartinLutherKingJr,
        # USPresidentsDay,
        # USMemorialDay,
        Holiday(
            "Fathers day",
            month=3,
            day=17,
            start_date="2021-03-17",
            observance=nearest_workday,
        ),
        Holiday("Independence Day", month=3,
                day=26, observance=nearest_workday),
        Holiday("Christmas Day", month=12, day=25, observance=nearest_workday)
    ]
