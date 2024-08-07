from collections import deque
import time

class PasswordCracker:
    def __init__(self):
        while True:
            self.max_length = int(input("Enter Maximum length of password allowed:\n"))
            self.password = self.get_password()
            if not self.password:
                return
            self.crack_password()
    

    def check_hash(self, s):
        return (s == self.password)


    def get_password(self):
        while True:
            password = input(f"Enter a password having any combination of smallcase letters, numbers upto maximum length of {self.max_length} digits or press enter to exit\n")
            if not password:
                return
            if len(password) > self.max_length:
                print("Enter Valid Password!\n")
                continue
            for c in password:
                valid = True
                if (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")):
                    continue
                else:
                    valid = False
                    break
            if not valid:
                print("Enter Valid Password!\n")
                continue
            else:
                return password


    def crack_password(self):
        self.allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        t1 = time.time()
        self.dfs()
        t2 = time.time()
        print("DFS approach took",time.strftime("%HH %MM:%SS", time.gmtime(t2-t1)), "time for", self.max_length," digits\n")
        time.sleep(3)

        t3 = time.time()
        self.bfs()
        t4 = time.time()


        print("DFS approach took",time.strftime("%HH %MM:%SS", time.gmtime(t2-t1)), "time for", self.max_length," digits\n")
        print("BFS approach took",time.strftime("%HH %MM:%SS", time.gmtime(t4-t3)), "time for", self.max_length," digits\n")


    def dfs(self, prefix= ""):
        if self.check_hash(prefix):
            print("found")
            return True

        if len(prefix) > self.max_length:
            return
        print(prefix)
        for c in self.allowed:
            if self.dfs(prefix= prefix + c):
                return True


    def bfs(self):
        queue = [""]
        
        while queue:
            current = queue.pop(0)
            print(current)
            if self.check_hash(current):
                print("found")
                return True
            
            if len(current) < self.max_length:
                for c in self.allowed:
                    queue.append(current + c)



if __name__ == "__main__":
    a = PasswordCracker()