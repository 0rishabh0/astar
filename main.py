#%%
from map import plot_map
nrow=6
ncol=6
obstacles = [(2,1),(3,1),(4,1),(2,2),(2,3),(2,4),(3,4),(4,4)]

actions = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}

start = (5,2)
goal  = (0,3)
#%%
# fig, ax = plot_map(nrow,ncol,obstacles)

#%%

def manhattan(a,b):
    return abs(a[1]-a[0])+abs(b[1]-b[0])
    
class node(object):
    def __init__(self, x, y, g=None, h=manhattan):
        self.xy = (x,y)
        self.g  = g
        self.h  = h((x,y),goal)

    def __eq__(self, other):
        if self.xy == other:
            return True
        else:
            return False

    def get_successors(self):
        successors={}
        for action in actions:
            action_x = actions[action][0]; action_y = actions[action][1]
            x=self.xy[0]+action_x
            y=self.xy[1]+action_y
            if (x<=5 and x>=0)and(y>=0 and y<=5):
                g=self.g+action_y+action_x
                successors[(x,y)] = node(x,y,g)
        return successors      

    def f(self):
        return self.g + self.h

start_node = node(*start, 0)


open_list  = {start_node.xy: start_node}  # node : f value
close_list = {}
#%%
while len(open_list)!=0:
    q=min(open_list, key=lambda x: open_list[x].f())
    q_node = open_list.pop(q)
    successors = q_node.get_successors()
    for child in successors:
        child_node = successors[child]
        if child == goal:
            break

        if child in close_list:
            continue
        else:
            close_list[]
            # if close_list[child].f()<= child_node.f():
            #     continue
            # else:
            #     open_list[child] = child_node

        if child in open_list:
            if open_list[child].f() <= child_node.f():
                continue
        else:
            open_list[child] = child_node

    close_list[q] = q_node
    print(q)


print(open_list)
print(close_list)

