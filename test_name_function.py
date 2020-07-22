import unittest
from name_function import formatted_name
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("giorno","giovanna")
        self.assertEqual(result,"Giorno Giovanna")
      
    def test_other_first_last_name(self):
        result = formatted_name("jotaro","kujo")
        self.assertEqual(result,"Jotaro Kujo")

    def test_first_middle_last_ame(self):
        result = formatted_name("kono","dio","da")
        self.assertEqual(result,"Kono Da Dio")    
      

if __name__==  "__main__":
    unittest.main()