import unittest
import body




class TestBody(unittest.TestCase):
    
    def setUp(self):
        self.map = 10
        self.body = body.Body(0, 0, None, self.map,self.map)
        for l in range(1,4):
            self.body = body.Body(0,l, self.body, self.map, self.map)


    def test_body(self):
        self.assertEqual([(0,0),(0,1),(0,2),(0,3)], self.body.getList())

    def test_inv_moveSnake(self):
        # self.assertRaises(Exception, self.body.movesnake(3, 3),'Invalid new Position')
        self.body.movesnake(3, 3)
        self.assertEqual([(0,0),(0,1),(0,2),(0,3)], self.body.getList())

    def test_directMove_eat(self):
        self.body.direct_move("n", True)
        self.assertEqual([(0,0),(0,1),(0,2),(0,3),(0,4)], self.body.getList())

    def test_directMove_hungry(self):
        self.body.direct_move("n", False)
        self.assertEqual([(0,1),(0,2),(0,3),(0,4)], self.body.getList())

    # def test_directmove_colision(self):
    #     self.assertRaises(Exception('colision',), self.body.direct_move("s", False))



    






if __name__ == '__main__':
    unittest.main(verbosity=2)