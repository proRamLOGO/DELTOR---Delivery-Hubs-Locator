from math import sqrt

class node(object) :
    """
    Node class to implement a sub-city/node type object.

    Attributes :
        - data_type : specifies type of node. 
        - id : name of node.
        - x : x-coordniate.
        - y : y-coordinate.
        - neighbours : dictionary containing neighbouring cities.  Data Organisation {node() : distance}

    Methods :
        - __init__() : Constructor Function.
        - add_neighbour() : To link with another subcity/node.
        - update_dp() : To update neighbours dictionary.
        - get_connections() : To get neighbouring cities' objects.
        - get_distance() : To get distance from a neighbour city.
        - get_location() : To get Coordinates.
    
    """

    def __init__( self , name, x, y ) :
        self.data_type = 'sink'
        self.id = name
        self.x = x
        self.y = y
        self.neighbours = dict()

    def add_neighbour( self, neighbour ) :
        if neighbour not in self.neighbours.keys() :
            self.neighbours[neighbour] = sqrt((neighbour.x-self.x)**2 + (neighbour.y-self.y)**2 )
            self.update_dp()
            return True
        else :
            return False

    def update_dp( self ) :
        x = len(self.neighbours)
        if x == 2 :
            self.data_type = 'connector'
        elif x > 2 :
            self.data_type = 'junction'

    def get_connections( self ):
        return self.neighbours.keys()  

    def get_location( self ) :
        return ( self.x, self.y )

    def get_distance( self, neighbour ) :
        if neighbour in self.neighbours.keys() :
            return self.neighbours[neighbour]
        else :
            return "No Direct Link"
        

class City( object ) :
    """
    City class to implement a City type object.

    Attributes :
        - connectors : list of sub-cities which are connectors. 
        - junctions : list of sub-cities which are junctions.
        - sinks : list of sub-cities which are sinks. 
        - vertices : dictionary containing all sub-cities of city. Data Organisation {name : node()}
        - no_of_vertices = 0

    Methods :
        - __init__() : Constructor Function.
        - add_node() : To add a new subcity/node in the city.
        - add_edge() : To link 2 nodes/sub-cities.
        - get_node() : To get node type object identifeid by name.
        - get_connectors() : To get names of connector type cities.
        - get_junctions() : To get names of junction type sub-cities.
        - get_sinks() : To get names of sink type sub-cities.
        - get_vertices() : To get names of all sub-cities.
        - update_lsts() : To update connectors, sinks, junctions data memebers in city.
    
    """
    
    def __init__( self ) :
        self.sinks = list()
        self.junctions = list()
        self.connectors = list()
        self.vertices = dict() #{name : node() }
        self.no_of_vertices = 0

    def add_node( self, name, x, y ):
        if name not in self.vertices.keys() :
            new_node = node( name, x, y )
            self.vertices[name] = new_node
            return True
        else :
            return False
    
    def get_node( self, name ) :
        if name in self.vertices:
            return self.vertices[name]
        return None

    def add_edge( self, frm, to ) :
        status1 = False
        status2 = False
        frm = self.vertices[frm]
        to = self.vertices[to]
        status1 = frm.add_neighbour(to)
        status2 = to.add_neighbour(frm)
        return status1 and status2

    def get_vertices(self):
        return self.vertices.keys()

    def get_junctions(self):
        return self.junctions
    
    def get_sinks(self):
        return self.sinks
    
    def get_connectors(self):
        return self.sinks

    def update_lists(self) :
        for i in self.vertices.values() :
            if i.data_type == 'junction' :
                self.junctions += [i]
            elif i.data_type == 'connector' :
                self.connectors += [i]
            elif i.data_type == 'sink' :
                self.sinks += [i]
        


class Road( object ) :
    """
    Class to implement a Road type object.

    Attributes :
        - end : ending node of a road.
        - connectors : list of connector type nodes/sub-cities.
        - junctions : list of junction type nodes/sub-cities.
        - length : total length of path.
        - start : starting node of a road.
        - vertices : list comprising of all nodes/sub-cities in road.

    Methods :
        - __init__() : Constructor Function
        - update_length() : To compute path length of road.
        - update_types() : To update connectors, junctions data memebers in road.
    """

    def __init__( self ) :
        self.junctions = list()
        self.connectors = list()
        self.start = None
        self.end = None
        self.length = 0
        self.vertices = []

    def update_types( self ) :
        for i in self.vertices :
            if i.data_type == 'junction' :
                self.junctions += [i]
            elif i.data_type == 'connector' :
                self.connectors += [i]

    def update_length( self ) :
        for i in range(len(self.vertices)-1) :
            self.length += self.vertices[i].get_distance(self.vertices[i+1])

def dfs( city, node, visited, path ) :
    """
    Traversal Function. Function traverses and finds different available paths in a city between any pair of end sub-cities.

    Input :
        - city : City type object. City to be traversed.
        - node : node type object. Starting point of taversal
        - visited : list type object. Contains nodes that have been visited.
        - path : list type object. Contains the path produced by traversal.

    Output :
        - list type object containing path produced. 
    
    """
    node = city.vertices[node]
    if node not in visited :
        visited += [node]
        for n in node.neighbours :
            if node.data_type == 'sink' and node != visited[0] :
                return  [ node ]
            elif n not in visited :
                return [ node ] + dfs( city, n.id , visited, path )
        return [node]
    else :
        return [node]
