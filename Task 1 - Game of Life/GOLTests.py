import numpy as np
import GOL
import pickle
import unittest

class TestGameOfLife(unittest.TestCase):
    #Tests the next generation of a five by five grid
    def testFiveByFiveSquareGridOneGeneration(self):
        test_grid = np.array([[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])
        received_Value = GOL.playGame(1, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests five generations ahead of a five by five grid
    def testFiveByFiveSquareFiveGenerations(self):
        test_grid  = np.array([[1, 0, 1, 1, 0], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.zeros((5, 5))
        received_Value = GOL.playGame(5, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests three generations ahead of a ten by five grid
    def testTenByFiveThreeGenerations(self):
        test_grid  = np.array([[1, 0, 1, 1, 0], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 0, 1],
                                [1, 1, 1, 1, 1], [0, 1, 0, 0, 1]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]])
        received_Value = GOL.playGame(3, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests common glider pattern on a five by five grid for three generations
    def testGliderFiveByFive(self):
        test_grid  = np.array([[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0]])
        received_Value = GOL.playGame(3, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests 100 generations ahead of a diamond pattern on a four by four grid
    def testDiamondPatternFourByFour(self):
        test_grid  = np.array([[0, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]])
        received_Value = GOL.playGame(100, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests three generations ahead of a seven by four grid
    def testSevenByFourSixGenerations(self):
        test_grid  = np.array([[1, 0, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0]])
        received_Value = GOL.playGame(3, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests two generations ahead of a thirty by thirty grid
    def testThirtyByThirtySquareFiveGenerations(self):
        test_grid  = np.ones((30, 30))
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.zeros((30, 30))
        received_Value = GOL.playGame(2, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        

    #Tests six generations ahead of a spaceship pattern on a five by five grid
    def testFiveByFiveSquareSixGenerations(self):
        test_grid  = np.array([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
        received_Value = GOL.playGame(6, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests four generations ahead of a four by four grid with all edges filled
    def testEdgesFilled(self):
        test_grid  = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])
        received_Value = GOL.playGame(4, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        
    
    #Tests 58 generations ahead of a four by five grid with the middle filled
    def testMiddleFilledFiveByFour(self):
        test_grid  = np.array([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
        with open('example.pkl', 'wb') as outfile:
            pickle.dump(test_grid, outfile)
            outfile.close()
        expected_Value = np.array([[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 0]])
        received_Value = GOL.playGame(58, 'example.pkl')
        np.testing.assert_array_equal(received_Value, expected_Value)
        

    

if __name__ == '__main__':
    unittest.main()
