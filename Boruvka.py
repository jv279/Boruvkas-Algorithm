def cheapest_edge(graph, component):
    '''
    Params:
    graph - The input graph
    component - the node in the graph that you are looking for the
    Returns:
    the cheapest edge of that component
    '''
    # a list of weights and the nodes
    values_withindexes =  []
    for i in component: 
        for j in range(len(graph[i])):
            if graph[i][j] !=0 and j not in component:
                #append the weight, then the two nodes in numerical order 
                values_withindexes.append((graph[i][j], min(i,j), max(i,j)))
    counter = 0
    for i in values_withindexes:
        if counter == 0:
            #initially in the loop the first value will be the cheapest edge
            cheapestEdge = i
        if cheapestEdge[0] > i[0]:
            cheapestEdge = i
        counter +=1

    return cheapestEdge

def merge_common(llist):
    """
    params:
    llist - a list of lists, in each list are values
    Returns:
    a list of lists where all the components 
    """
    components = []
    for i in llist:
        if len(components) == 0:
            #initially the first item in the list is set as a component
            components.append(i)
            continue
        
        if len(components)>0:
            #if the item is not found in the component lists later it is added as its own component
            in_list = False

            for component in range(len(components)):
                if common_value(i, components[component]):
                    #The item in the list is appended to the component when they share a common value
                    in_list = True
                    components[component] = components[component]+ i
                    continue
                                 
            if in_list == False:
                #if not found in the current compon
                components.append(i)
    new_components = []
    for i in components:
        new_components.append(list(set(i)))
    return new_components


def common_value(list1, list2): 
    """
    params:
    list1: a list of values
    list2: a list of values
    returns:
    boolean true if there is a value in common between the two lists, false if not
    """
    result = False
  
   
    for x in list1: 
        for y in list2: 
    
            # if one value common 
            if x == y: 
                result = True
                return result  
                  
    return result 

def boruvkas(graph):
    """
    Params:
    graph - a weighted adjacency matrix of the network

    Returns:
    a list of tuples, the first value being the weight of the edge, and the second and third value being the two nodes connected
    """


    components = [[i] for i in range(len(graph))]
    MST = []
    while len(components) > 1:
        cheapest_edges = []
        for i in range(len(components)):
            # create a list for all components smallest edge
            if cheapest_edge(graph, components[i]) not in cheapest_edges:
                cheapest_edges.append(cheapest_edge(graph, components[i]))
        
        mergers = cheapest_edges
        MST.append(mergers)
        new_components = []
        for i in mergers:
            for j in components:
                # if either value is in the current component, that value from merger is appended to the list of new_components
                if i[1] in j:
                    merge_a = j
                    
                if i[2] in j:
                    merge_b = j
                    
            new_components.append(merge_a + merge_b)
        #the new components list will have values in it that are in common due to the first loop only getting the pairings 
        #this function checks through the new component list and merges the values in common together
        components = merge_common(new_components)
        
    return sum(MST,[])
graph = [
    [0,4,0,0,0,0,0,8,0],
    [4,0,8,0,0,0,0,11,0],
    [0,8,0,7,0,4,0,0,2],
    [0,0,7,0,9,14,0,0,0],
    [0,0,0,9,0,10,0,0,0],
    [0,0,4,14,10,0,2,0,0],
    [0,0,0,0,0,2,0,1,6],
    [8,11,0,0,0,0,1,0,7],
    [0,0,2,0,0,0,6,7,0]
]

graph2 = [
    [0,10,6,5],
    [10,0,0,15],
    [6,0,0,4],
    [5,15,4,0]
    
]

Demonstration_Graph = [
    [0,2,0,3,0],
    [2,0,11,0,0],
    [0,11,0,6,1],
    [3,0,6,0,13],
    [0,0,1,13,0]
]

print("Minimum Spanning Tree (Weight, Vertex1, Vertex2)  ", boruvkas(Demonstration_Graph))
total = 0
for i in boruvkas(Demonstration_Graph):
    total+= i[0]

print("Total Weight of MST is ", total)
