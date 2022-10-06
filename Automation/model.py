from turtle import pos


class Bracket:
    CLEREANCE = 1
    def __init__(self,tool,position) -> None:
        self.Start = position
        self.End = position+tool.Length
        self.Tool = tool
    def __str__(self) -> str:
        return "start {0} end {1} -- tool {2}\n".format(self.Start,self.End,self.Tool)
    def Collide(self,bracket):
        return self.isInside(bracket) or self.CollisionLeft(bracket)  or self.CollisionRight(bracket) 
    def isInside(self,bracket):
        return self.Start>= bracket.Start and self.End <=bracket.End
    def CollisionRight(self,bracket):
        return self.Start <= bracket.Start and self.End >= bracket.Start
    def CollisionLeft(self,bracket):
        return bracket.Start <= self.Start and bracket.End >= self.Start
    def Add(self,_Bracket):
        bracket = Bracket(_Bracket.Tool,self.End+self.CLEREANCE)
        return bracket
class Press:
    def __init__(self,LenBar) -> None:
        self.Bar =[]
        self.LenBar = Bracket(Tool(LenBar),0)

    def test_CanHostBracket(self,Bracket):
        return Bracket.isInside(self.LenBar)

    def tool_Remove(self,Range):
        for _Bracket in self.Bar:
            if _Bracket.isInside(Range):
                self.Bar.remove(_Bracket)


    def Auto_Insert(self,Bracket):
        if(self.test_CanHostBracket(Bracket)):
            bl = True
            for _Bracket in self.Bar:
                newPos= _Bracket.Add(Bracket)
                bl = bl and not _Bracket.Collide(newPos) 
        if bl:
            self.Bar.append(newPos)
        return bl

    def tool_Add(self,Bracket):
        if(self.test_CanHostBracket(Bracket)):
            for _Bracket in self.Bar:
                if _Bracket.Collide(Bracket) :
                    return False
            self.Bar.append(Bracket)
            return True
        return False


class Tool:
    def __init__(self,length,name= "Default") -> None:
        self.Length = length
        self.Name = name
        assert(length>0)
    def __str__(self) -> str:
        return "Length {0} Name {1}".format(self.Length,self.Name)
