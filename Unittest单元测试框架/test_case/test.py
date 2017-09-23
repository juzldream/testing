import unittest



class MyTestCase(unittest.TestCase):
     def setUp(self):
         print("start test ...")
 
     def clear(self):
         #some cleanup code
         pass
        
     def actions(self, arg1, arg2):
         print(arg1,arg2)
         self.assertFalse(arg1, msg="登录失败了！")

        
     @staticmethod   
     def getTestFunc(arg1, arg2):
         def func(self):
             self.actions(arg1, arg2)
         return func
       
     def tearDown(self):
         print("test end ...")
 
def generateTestCases():
     arglists = [('jhadmin', 'jhadmin'), ('user1', 'user1'), ('user2', 'user2')]
     for args in arglists:
         setattr(MyTestCase, 'test_func_%s_%s'%(args[0], args[1]),
             MyTestCase.getTestFunc(*args) )
generateTestCases()
    
if __name__ =='__main__':
    unittest.main() 
