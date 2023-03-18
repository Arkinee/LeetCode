class BrowserHistory:
    home = ""
    arr = []
    temp = []
    
    def __init__(self, homepage: str):
        self.home = homepage
        self.arr.clear()
        self.temp.clear()
        
    def visit(self, url: str) -> None:
        self.arr.append(url)
        self.temp.clear()
        print("visit " + str(self.arr))

    def back(self, steps: int) -> str:
        print(self.arr)

        if(steps > len(self.arr)):
            for i in range(len(self.arr)):
                self.temp.append(self.arr.pop())
            return self.home
        
        for i in range(steps):
            a = self.arr.pop()
            self.temp.append(a)
            
        #print(self.arr[-1])
        if(len(self.arr) == 0):
            return self.home
        
        return self.arr[-1]

    def forward(self, steps: int) -> str:
        print("temp " + str(self.temp))
        
        if(steps < len(self.temp)):
            for _ in range(steps):
                a = self.temp.pop()
                print("pop " + str(a))
                self.arr.append(a)
            
            return self.arr[-1]    
            
        else:
            for i in range(len(self.temp)):
                self.arr.append(self.temp.pop())

            if(len(self.arr) == 0):
                return self.home

            return self.arr[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)