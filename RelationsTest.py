from __future__ import absolute_import, division, print_function
import unittest
from Relations import *
from BasicRelations import *

class TestRelations(unittest.TestCase):
    def setUp(self):
        pass
    
    def testNumberTransitiveMatrix(self):
        self.assertEqual(numberOfTransitive(1), 2) 
        self.assertEqual(numberOfTransitive(2), 13)
        self.assertEqual(numberOfTransitive(3), 171)
        self.assertEqual(numberOfTransitive(4), 3994)
        self.assertEqual(numberOfTransitive(0), -1)
        self.assertEqual(numberOfTransitive(99), -1)
        
    def testSterlingNumbers(self):
        self.assertEqual(1, calculateSterlingSecondKind(0, 0))
        self.assertEqual(0, calculateSterlingSecondKind(2, 0))
        self.assertEqual(7, calculateSterlingSecondKind(4, 2))
        self.assertEqual(42525, calculateSterlingSecondKind(10, 5))
    
    def testTestReflexive(self):
        correctMatrix = np.matrix('1 0; 0 1')
        incorrectMatrix = numpy.matrix('0 0; 0 0')
        wrongSize = numpy.matrix('1 0 1; 0 1 1')
        self.assertFalse(testReflexive(incorrectMatrix))
        self.assertFalse(testReflexive(wrongSize))
        self.assertTrue(testReflexive(correctMatrix))
    
    def testTestIrreflexive(self):
        correctMatrix = np.matrix('0 1 1; 0 0 1; 0 0 0')
        incorrect1 = np.matrix('1 0 0; 0 1 0; 0 0 1')
        incorrect2 = np.matrix('1 0 0; 1 1 0; 1 1 1')
        wrongSize = np.matrix('1 1 1; 0 0 0')
        self.assertTrue(testIrreflexive(correctMatrix))
        self.assertFalse(testIrreflexive(incorrect1))
        self.assertFalse(testIrreflexive(incorrect2))
        self.assertFalse(testIrreflexive(wrongSize))
    
    def testTestSymmetric(self):
        correctMatrix = np.matrix('1 1 1; 1 0 0; 1 0 0')
        incorrectMatrix = numpy.matrix('0 1 1; 0 0 0; 0 0 0')
        wrongSize = numpy.matrix('1 0 1')
        self.assertFalse(testSymmetric(incorrectMatrix))
        self.assertFalse(testSymmetric(wrongSize))
        self.assertTrue(testSymmetric(correctMatrix))
    
    def testTestAntisymmeric(self):
        correctMatrix = np.matrix('0 1 0; 0 0 0; 0 1 0')
        incorrectMatrix = numpy.matrix('0 1 1; 1 0 1; 1 1 0')
        self.assertTrue(testAntisymmetric(correctMatrix))
        self.assertFalse(testAntisymmetric(incorrectMatrix))
    
    def testTestTransitive(self):
        correctMatrix = np.matrix('1 1 0; 1 1 0; 0 0 0')
        incorrectMatrix = numpy.matrix('1 1 0; 1 1 1; 1 0 0')
        self.assertTrue(testTransitive(correctMatrix))
        self.assertFalse(testTransitive(incorrectMatrix))
    
    def testTestEquivalence(self):
        correctMatrix = np.matrix('1 0 1; 0 1 0; 1 0 1')
        incorrectMatrix = numpy.matrix('1 1 1; 0 1 1; 0 0 1')
        self.assertTrue(testEquivalence(correctMatrix))
        self.assertFalse(testEquivalence(incorrectMatrix))
    
    def testTestPartialOrder(self):
        correctMatrix = np.matrix('1 1 1; 0 1 1; 0 0 1')
        incorrectMatrix = numpy.matrix('1 0 1; 0 1 0; 1 0 1')
        self.assertTrue(testPartialOrder(correctMatrix))
        self.assertFalse(testPartialOrder(incorrectMatrix))
    
    def basicRelationsTest(self):
        emptyTester = np.array('0 0 0; 0 0 0; 0 0 0')
        universalTester = np.array('1 1 1; 1 1 1; 1 1 1')
        equalityTester = np.array('1 0 0; 0 1 0; 0 0 1')
        notEqualTester = np.array('0 1 1; 1 0 1; 1 1 0')
        greaterThanTester = np.array('0 0 0; 1 0 0; 1 1 0')
        greaterThanOrEqualTester = np.array('1 0 0; 1 1 0; 1 1 1')
        lessThanTester = np.array('0 1 1; 0 0 1; 0 0 0')
        lessThanOrEqualTester = np.array('1 1 1; 0 1 1; 0 0 1')
        self.assertTrue(np.equal(emptyTester, np.array(emptyRelation(3))))
        self.assertTrue(np.equal(universalTester, np.array(universalRelation(3))))
        self.assertTrue(np.equal(equalityTester, np.array(equalityRelation(3))))
        self.assertTrue(np.equal(notEqualTester, np.array(notEqualRelation(3))))
        self.assertTrue(np.equal(greaterThanTester, np.array(greaterThanRelation(3))))
        self.assertTrue(np.equal(greaterThanOrEqualTester, np.array(greaterThanOrEqualRelation(3))))
        self.assertTrue(np.equal(lessThanTester, np.array(lessThanRelation(3))))
        self.assertTrue(np.equal(lessThanOrEqualTester, np.array(lessThanOrEqualRelation(3))))
    
    def testCombinatorics(self):
        self.assertEqual(4096, combinatoricsReflexiveOrIrreflexive(4))
        self.assertEqual(1024, combinatoricsSymmetric(4))
        self.assertEqual(5, combinatoricsEquivalence(3))
        self.assertEqual(11664, combinatoricsAntisymmetric(4))
        
    def testReflexiveClosure(self):
        originalMatrix = np.matrix('1 0 0; 0 1 1; 1 0 1')
        finalMatrix = np.matrix('1 0 0; 0 1 1; 1 0 1')
        finalArray = np.array(finalMatrix)
        self.assertTrue(np.array_equal(finalArray, np.array(reflexiveClosure(originalMatrix))))
    
    def testSymmetricClosure(self):
        originalMatrix = np.matrix('1 0 0; 0 1 1; 1 0 1')
        finalMatrix = np.matrix('1 0 1; 0 1 1; 1 1 1')
        finalArray = np.array(finalMatrix)
        self.assertTrue(np.array_equal(finalArray, np.array(symmetricClosure(originalMatrix))))
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
