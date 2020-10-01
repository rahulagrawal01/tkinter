#!/usr/bin/python
#hello this is a very good project
import Tix

class View(object):
    def __init__(self, root):
        self.root = root
        self.makeCheckList()

    def makeCheckList(self):
        self.cl = Tix.Tree(self.root)
        #self.cl = Tix.Tree(self.root, browsecmd=self.selectItem)
        self.cl.pack()

        # this is the tixHList
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.hlist.add("CL1.a", text="subitem1")
        self.cl.hlist.add("CL1.a.b", text="subsubitem1")
        self.cl.hlist.add("CL1.a.b.c", text="subsubsubitem1")
        self.cl.hlist.add("CL1.a.b.c.d", text="subsubsubsubitem1")
        self.cl.hlist.add("CL1.Item1", text="subitem1")
        self.cl.hlist.add("CL2", text="checklist2")
        self.cl.hlist.add("CL2.Item1", text="subitem1")
        #self.cl.setstatus("CL2", "on")
        #self.cl.setstatus("CL2.Item1", "on")
        #self.cl.setstatus("CL1", "off")
        #self.cl.setstatus("CL1.Item1", "off")
        self.cl.autosetmode()

    def selectItem(self, item):
        print item
        #print item, self.cl.getstatus(item)

def main():
    root = Tix.Tk()
    view = View(root)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    main()
