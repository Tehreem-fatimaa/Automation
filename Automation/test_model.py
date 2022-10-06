import unittest
from model import Bracket,Press,Tool
class TestInterpolation(unittest.TestCase):
    
    def test_PieceCollision(self):
        press =self.ComposePress()
        brk = Bracket(Tool(10),150)
        self.assertFalse(press.tool_Add(brk))

    def test_PieceCollisionLeft(self):
        press =self.ComposePress()
        brk = Bracket(Tool(100),10)
        self.assertFalse(press.tool_Add(brk))
    
    def test_PieceCollisionRight(self):
        press =self.ComposePress()
        brk = Bracket(Tool(100),190)
        self.assertFalse(press.tool_Add(brk))
    
    def test_AutoInsert(self):
        press =self.ComposePress()
        brk = Bracket(Tool(100),190)
        self.assertTrue(press.Auto_Insert(brk))
        self.assertTrue(press.Bar[1].Start == press.Bar[0].End+brk.CLEREANCE)
    
    def test_AutoInsert2(self):
        press =self.ComposePress()
        brk = Bracket(Tool(100),490)
        press.Auto_Insert(brk)
        self.assertTrue(press.Auto_Insert(brk))
        self.assertTrue(press.Auto_Insert(brk))
        self.assertTrue(press.Auto_Insert(brk))
        self.assertTrue(press.Auto_Insert(brk))

    def test_Remove(self):
        press =self.ComposePress()
        brk = Bracket(Tool(100),500)
        press.tool_Add(brk)
        int_before = len(press.Bar)
        press.tool_Remove(brk)
        int_after = len(press.Bar)
        self.assertTrue(int_before == int_after+1)
    def ComposePress(self):
        press =Press(1000)
        tol = Tool(100,"myTool")
        brk1 = Bracket(tol,100)
        press.tool_Add(brk1)
        return press
        
if __name__ == '__main__':
    unittest.main()