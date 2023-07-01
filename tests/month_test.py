import unittest

from source import Month, MonthYear

class MonthTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ### Block of test methods

    @unittest.skip('Performance check')
    def test_performance(self):
        import datetime
        start = datetime.datetime.now()
        ## code here
        end = datetime.datetime.now() - start
        print(f'Done in {end} s.')

    def test_can_init_month(self):
        jan = Month(1)
        jan_str = Month("jan")

    def test_string_methods(self):
        awaited_ru = "янв"
        awaited_rufull = "январь"
        awaited_eng = "jan"
        awaited_engfull = "january"
        awaited_M = "M01"
        awaited_index = 1

        jan = Month(1)

        self.assertEqual(awaited_ru, jan.Ru())
        self.assertEqual(awaited_rufull, jan.RuFull())

        self.assertEqual(awaited_eng, jan.Eng())
        self.assertEqual(awaited_engfull, jan.EngFull())

        self.assertEqual(awaited_M, jan.M())
        self.assertEqual(awaited_index, jan.index())

    def test_can_compare_months(self):
        march = Month(3)
        november = Month("NOV")
        nov = Month(11)

        self.assertTrue(november > march)
        self.assertTrue(march < november)
        self.assertTrue(november == nov)

    def test_can_increase_decrease(self):
        awaited_march = "mar"
        awaited_september = "sep"

        june = Month("june")
        march = june - 3
        september = june + 3

        self.assertEqual(awaited_march, march.Eng())
        self.assertEqual(awaited_september, september.Eng())

    def test_eoy_december_not_equal_init_december(self):
        awaited_init = "M00"
        awaited_eoy = "M12"

        init = Month(0)
        eoy = Month(12)

        self.assertEqual("dec", init.Eng())
        self.assertEqual("dec", eoy.Eng())

        self.assertFalse(init == eoy)
        self.assertTrue(init != eoy)
        
        self.assertEqual(awaited_init, init.M())
        self.assertEqual(awaited_eoy, eoy.M())

class MonthYearTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ### Block of test methods

    @unittest.skip('Performance check')
    def test_performance(self):
        import datetime
        start = datetime.datetime.now()
        ## code here
        end = datetime.datetime.now() - start
        print(f'Done in {end} s.')

    def test_can_init_monthyear(self):
        awaited = "mar`23"
        awaited_2 = "jun 23"

        year = MonthYear(3, 2023, "`")
        year_2 = MonthYear(6, 2023, " ")

        self.assertEqual(awaited, year.Eng())
        self.assertEqual(awaited_2, year_2.Eng())