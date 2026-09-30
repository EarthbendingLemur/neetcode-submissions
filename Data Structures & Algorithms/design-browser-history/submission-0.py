
class Node:

    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.curPage = self.home

    def visit(self, url: str) -> None:
        newPage = Node(url)
        newPage.prev = self.curPage
        self.curPage.next=newPage
        self.curPage = self.curPage.next
        

    def back(self, steps: int) -> str:
        curSteps = steps
        while self.curPage.prev and curSteps > 0:
            self.curPage = self.curPage.prev
            curSteps -= 1
        return self.curPage.val
        

    def forward(self, steps: int) -> str:
        curSteps = steps
        while self.curPage.next and curSteps > 0:
            self.curPage = self.curPage.next
            curSteps -= 1
        return self.curPage.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)