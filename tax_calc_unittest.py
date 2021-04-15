import unittest
import taxcalcv15

class TestCase(unittest.TestCase):
    def test_MPF(self):
        print("testing mpf")
        result=taxcalcv15.MPF(180000)
        self.assertEqual(result,9000.0)
        self.assertRaises(ValueError,taxcalcv15.MPF,-180000)

    def test_SalaryTax(self):
        print("testing salary tax")
        print("testing normal case in salary tax")
        result=taxcalcv15.SalaryTax(200000)
        self.assertEqual(result,1480)
        result = taxcalcv15.SalaryTax(250000)
        self.assertEqual(result,4550)
        result = taxcalcv15.SalaryTax(300000)
        self.assertEqual(result, 9420)
        result = taxcalcv15.SalaryTax(350000)
        self.assertEqual(result, 16085)
        result = taxcalcv15.SalaryTax(400000)
        self.assertEqual(result, 24500)
        result = taxcalcv15.SalaryTax(800000)
        self.assertEqual(result, 92500)
        result = taxcalcv15.SalaryTax(2000000)
        self.assertEqual(result, 296500)
        result = taxcalcv15.SalaryTax(3500000)
        self.assertEqual(result, 522300)


    def test_StandardTax(self):
        print("Testing Standard Tax")
        print("testing normal cases")
        result = taxcalcv15.StandardTax(750000)
        self.assertEqual(result,109800)
        result = taxcalcv15.StandardTax(10000)
        self.assertEqual(result, 0)
        result = taxcalcv15.StandardTax(150000)
        self.assertEqual(result, 19800)
        result = taxcalcv15.StandardTax(1000000)
        self.assertEqual(result, 147300)
        result = taxcalcv15.StandardTax(2000000)
        self.assertEqual(result, 297300)
        result = taxcalcv15.StandardTax(5000000)
        self.assertEqual(result, 747300)

    def test_TotalSalaryTax(self):
        print("testing joint assessment")
        print("testing normal cases")
        result=taxcalcv15.TotalSalarytax(240560,109440)
        self.assertEqual(result, 2110)
        result=taxcalcv15.TotalSalarytax(250000,120000)
        self.assertEqual(result, 3250)
        result=taxcalcv15.TotalSalarytax(250000,250000)
        self.assertEqual(result, 17870)
        result = taxcalcv15.TotalSalarytax(250000,2500000)
        self.assertEqual(result, 399435)
        result = taxcalcv15.TotalSalarytax(3000000, 1800000)
        self.assertEqual(result, 714600)
        result = taxcalcv15.TotalSalarytax(3062470, 3062470)
        self.assertEqual(result, 91341)


        self.assertRaises(ValueError, taxcalcv15.TotalSalarytax, -180000,-20000)

    def test_SeparateTotal(self):
        print("Testing Separate tax Total")
        print("testing normal cases")
        result = taxcalcv15.SeparateTotal(240560,109440)
        self.assertEqual(result,3791.92)
        result = taxcalcv15.SeparateTotal(250000,120000)
        self.assertEqual(result,4550)
        result = taxcalcv15.SeparateTotal(250000,250000)
        self.assertEqual(result,9100)
        result = taxcalcv15.SeparateTotal(250000,2500000)
        self.assertEqual(result,376850)
        result = taxcalcv15.SeparateTotal(3000000, 1800000)
        self.assertEqual(result,709800)
        result = taxcalcv15.SeparateTotal(3062470, 3062470)
        self.assertEqual(result, 913341.0)

if __name__ == '__main__':
    unittest.main()
