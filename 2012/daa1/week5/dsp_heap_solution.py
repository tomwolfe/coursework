import heapq
def gen_list_edges(filename):
    myfile=open(filename)
    str=myfile.read()
    direct_input=str.split('\n')
    myfile.close()
    #delete last empty line
    direct_input=direct_input[:-1] # len(direct_input) equals 200
    #element in temp_element is ['vertex,distance','vertex,distance',...]
    temp_element=[]
    for e in direct_input:
        temp_element.append(e.split())
    #element in final_list is [[vertex,distance],[vertex,distance],...]
    #eg [{vertex:distance, vertex:distance...},{...}] where array index
    #is the starting vertex
    final_list=[]
    #I miss .each_index from ruby here
    #unsure of python's equivalent
    i=0
    n=len(temp_element)
    while i<n:
        temp_element[i]=temp_element[i][1:] # removes vertex label
        final_list.append({})
        for e in temp_element[i]:
            ver,dis=e.split(',')
            # in my case, verticies indexed from 1 in .txt file
            ver_int=int(ver)-1
            final_list[i][ver_int]=int(dis)
        i=i+1
    return final_list

def dijkstra_heap(G,v):
    dist_so_far = []
    distMap = {v: 0}
    heapq.heappush(dist_so_far, (0, v))
    final_dist = {}
    while len(final_dist) < len(G):
        (d, w) = heapq.heappop(dist_so_far)
        final_dist[w] = d
        for x in G[w]:
            if x not in final_dist:
                d = final_dist[w] + G[w][x]
                if x not in distMap or d < distMap[x]:
                    distMap[x] = d
                    heapq.heappush(dist_so_far, (d, x))
    return final_dist

filename='dijkstra.txt'
edge_list=gen_list_edges(filename)
v0=0 #start vertex
A=dijkstra_heap(edge_list,v0)
print A[6],A[36],A[58],A[81],A[98],A[114],A[132],A[164],A[187],A[196]
