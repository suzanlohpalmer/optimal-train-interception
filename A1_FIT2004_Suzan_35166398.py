class MinHeap:
    def __init__(self, max_size):
        """
        Function description: 
        This function initialises a MinHeap data structure with supplemetary memory. 
        The index_array keeps track of where each element is located inside the heap (the_array).
        When initialising the MinHeap:
        - We use a 1-based indexing in the_array. Each entry corresponds to a umique key or element value (int from 0 to max_size -1).
        - We use -1 with index_array to indicate that there are no elemtents currently in the heap. 
        - An extra index mapping array was used to find a value's position in the heap in O(1) time.  

        Input: 
        argv1: max_size, an integer representing the maximum number of elements the heap can contain.

        Output: 
        None, only initializes internal data structures.

        Time complexity: 
        O(n), where n is the value of max_size.

        Time complexity analysis:
        Initializing both the_array and index_array takes linear time with respect to max_size.

        Input space complexity:
        O(1), the input is a single integer (max_size).

        Auxiliary space complexity:
        O(n), where n is the value of max_size.

        Space complexity analysis:
        - the_array uses O(n + 1) space to support 1-based indexing.
        - index_array uses O(n) space.
        - Since this function does not take or process any input structures, all allocated space is additional.
        - Therefore, the auxiliary memory required is O(n). 
        - Overall, this results in a total space complexity of O(n).
        """
        self.length = 0 # Initialising the heap
        self.the_array = [None] * (max_size + 1)  
        self.index_array = [-1] * max_size  # Tracks index of each element

    def __len__(self):
        """
        Function description: 
        This function returns the current number of elements stored in the heap.

        Input: 
        None

        Output: 
        An integer representing the number of elements currently in the heap.

        Time complexity: O(1)

        Time complexity analysis:
        The function just returns the value of a class attribute, which is a constant-time operation.

        Input space complexity: 
        O(1)

        Auxiliary space complexity:
        O(1)

        Space complexity analysis:
        - No additional memory is used beyond the return value.
        - It does not allocate or use any additional data structures or memory during execution. 
        - Therefore, the auxiliary space used remains constant, regardless of the heap size.
        - Overall, this results in a total space complexity of O(1).
        """
        return self.length

    def is_full(self):
        """
        Function description: 
        This function checks whether the heap is full, if no more elements can be inserted.
        - The heap uses 1-based indexing, so the check compares (length + 1) to the total size of the_array.
        - If length + 1 equals len(the_array), it means the next insertion index would be out of bounds.

        Input: 
        None

        Output: 
        A boolean value, True if the heap is full, False otherwise.

        Time complexity: 
        O(1)

        Time complexity analysis:
        This function performs a simple arithmetic comparison, which takes constant time.

        Input space complexity: 
        O(1)

        Auxiliary space complexity:
        O(1)

        Space complexity analysis:
        - No additional memory is used beyond the return value.
        - The return value does not count towards the auxiliary space.
        - Overall, this results in a total space complexity of O(1).
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k):
        """
        Function description: 
        This function moves the element at index k up the heap to restore the min-heap property, if violated.
        - The heap stores objects with a 'distance' attribute used for priority comparison.
        - The element at index k is compared with its parent; if smaller, it is moved upward.
        - The index_array is updated accordingly to reflect all swaps.
        - The process continues until the min-heap property is restored or the root is reached.

        Input: 
        argv1: k, an integer representing the index of the element to rise in the heap (1-based index).

        Output:
        None, heap structure is modified in-place.

        Time complexity: 
        O(log(n)), where n is the number of elements currently in the heap.

        Time complexity analysis:
        In the worst case, the element moves from a leaf to the root, which takes O(log(n)) time due to the tree height.

        Input space complexity: 
        O(1)

        Auxiliary space complexity:
        O(1)

        Space complexity analysis:
        - This function does not allocate any memory proportional to the size of the input n. 
        - It only uses a constant number of variables item, k, and temporary assignments within the loop. 
        - No recursion or additional data structures are used, so the overall memory used during the function execution remains constant, regardless of the size of the heap.
        - Overall, this results in a total space complexity of O(1).
        """
        item = self.the_array[k]  # element to rise is at index k
        while k > 1 and item.distance < self.the_array[k // 2].distance:  # compare with parent based on distance
            self.the_array[k] = self.the_array[k // 2]  # move parent down
            self.index_array[self.the_array[k].id] = k  # update index of moved parent
            k = k // 2  # move up to parent index
        self.the_array[k] = item  # place the rising element in its correct spot
        self.index_array[item.id] = k  # update index of the risen element

    def add(self, element):
        """
        Function description: 
        This function adds a new element to the min-heap and ensures the heap property is maintained by using the rise operation.
        - The element is inserted at the next available position at the end of the heap.
        - The index_array is updated to track the location of the element in the heap.
        - The rise function is called to restore the min-heap structure after insertion.

        Input: 
        argv1: element, an object to be added to the heap. It must have an 'id' attribute used for indexing.

        Output: 
        A boolean value, True if the element is successfully added, False if the heap is already full.

        Time complexity: 
        O(log(n)), where n is the number of elements currently in the heap.

        Time complexity analysis:
        - Checking if the heap is full and inserting the element both take constant time.
        - The rise operation restores the heap property by potentially bubbling the new element up to the root, which requires at most log(n) swaps in a binary heap.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - Only a fixed number of variables are used during the operation.
        - The operation modifies preallocated arrays in-place and doesn't allocate new memory dynamically.
        - Overall, this results in a total space complexity of O(1).
        """
        if self.is_full():
            return False
        self.length += 1 # Keeps track of how many items using self.length then increase by 1 to add element 
        self.the_array[self.length] = element # Element is added to the end of heap (self.length)
        self.index_array[element.id] = self.length # Updates to store index self.length 
        self.rise(self.length) # Maintain the meanheap rule

    def smallest_child(self, k):
        """
        Function description:
        This function returns the index of the smaller child of the node at index k in a binary min-heap based on the 'distance' attribute of elements.
        - If only the left child exists, it returns the left child by default.
        - Compares the 'distance' attribute of both children to determine the smaller one.

        Input:
        argv1: k, an integer representing the index of the parent node (1-based index).

        Output:
        An integer, which represents the index of the smaller child node.

        Time complexity: 
        O(1)

        Time complexity analysis:
        - Only a fixed number of arithmetic and comparison operations are performed.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - No additional memory is used beyond local variables.
        - No dynamic memory allocation or recursive calls are made.
        - Overall, this results in a total space complexity of O(1).
        """
        left = 2 * k  # Calculate index of the left child
        right = 2 * k + 1  # Calculate index of the right child

        # If right child is out of bounds (does not exist), or left child has a smaller distance
        if right > self.length or self.the_array[left].distance < self.the_array[right].distance:
            return left  # Return left if it is the only child or smaller one
        else:
            return right  # Return right if it exists and has smaller or equal distance

    def sink(self, k):
        """
        Function description: 
        This function pushes down the element at index k in the heap to its correct position to restore the min-heap property, if violated.
        - The heap contains elements with a 'distance' attribute used for comparison.
        - This function is typically used after removing the minimum element or updating an element's distance.
        - The index_array is updated during swaps to keep track of current positions of all elements.

        Input:
        argv1: k, an integer representing the index of the element to sink in the heap (1-based index).

        Output: 
        None, heap structure is modified in-place.

        Time complexity: 
        O(log(n)), where n is the number of elements currently in the heap.

        Time complexity analysis:
        - At most O(log(n)) swaps are performed as the element may move from the root to a leaf node.
        - Each step compares with the smallest child, which takes constant time.

        Input space complexity: 
        O(1)

        Auxiliary space complexity:
        O(1)

        Space complexity analysis:
        - Only a constant amount of additional memory is used.
        - The function only uses a constant number of auxiliary variables, such as item, k, and min_child.
        - No recursion or additional data structures are used, so memory usage does not depend on input size.
        - Overall, this results in a total space complexity of O(1).
        """
        item = self.the_array[k]  # element to be pushed down
        while 2 * k <= self.length:  # while there is at least one child
            min_child = self.smallest_child(k)
            if self.the_array[min_child].distance >= item.distance:
                break  # min-heap property is satisfied
            self.the_array[k] = self.the_array[min_child]  # move smaller child up
            self.index_array[self.the_array[k].id] = k  # update index_array for moved child
            k = min_child  # continue sinking at new position
        self.the_array[k] = item  # place item at its correct position
        self.index_array[item.id] = k  # update index_array for item
        
    def get_min(self):
        """
        Function description: 
        This function removes and returns the element with the smallest distance (i.e., the root of the min-heap), while maintaining the heap property.
        - If the heap is empty, returns None
        - The last element is moved to the root, then sink() is called to restore the heap.
        - The index_array is updated to reflect the removal and repositioning of elements.

        Input: 
        None

        Output:
        The element with the smallest distance (or None if the heap is empty).

        Time complexity: 
        O(log(n)), where n is the number of elements currently in the heap.

        Time complexity analysis:
        - Accessing the root element is O(1).
        - Replacing the root and sinking the new root to its correct position takes O(log(n)) in the worst case.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - Only a constant number of local variables are used.
        - No dynamic memory or recursion is involved.
        - Overall, this results in a total space complexity of O(1).
        """
        if self.length == 0:
            return None  # heap is empty
        min_elt = self.the_array[1]  # root of the heap has the minimum element
        self.index_array[min_elt.id] = -1  # mark as removed
        self.the_array[1] = self.the_array[self.length]  # move last element to root
        self.length -= 1  # decrease heap size
        if self.length > 0:
            self.index_array[self.the_array[1].id] = 1  # update index of new root
            self.sink(1)  # restore heap property
        return min_elt  # return the removed min element

    def update(self, element, new_distance):
        """
        Function description: 
        This function updates the distance (priority) of a given element in the min-heap and restores the heap property by performing a rise operation only if the new distance is smaller than the current one.
        - The index_array is used to retrieve the current index of the element in the heap.
        - This function does not support increasing the distance (no sinking is performed).
        - It assumes the element is already present in the heap.
        
        Input:
        argv1: element, the object stored in the heap that contains a 'distance' attribute and a unique 'id'.
        argv2: new_distance, an integer or float representing the updated priority value.

        Output: 
        None, heap structure is modified in-place

        Time complexity: 
        O(log(n)), where n is the number of elements in the heap.

        Time complexity analysis:
        - Checking the current index and comparing distances is O(1)
        - In the worst case, the element rises to the root, which takes O(log(n))

        Input space complexity:
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - Only a constant amount of auxiliary space is used
        - No dynamic memory allocation or recursion is performed
        - Overall, this results in a total space complexity of O(1).
        """
        idx = self.index_array[element.id]  # Find the index of the element in the heap using its ID
        if new_distance < element.distance:  # Only proceed if the new distance is smaller (min-heap)
            element.distance = new_distance  # Update the distance value
            self.rise(idx)  # Restore the min-heap property by rising the element


class Graph:
    def __init__(self, vertices_count):
        """
        Function description: 
        Initializes a graph by creating a list of Vertex objects, one for each index from 0 to vertices_count - 1.
        - Vertices are stored in a list indexed by their ID for constant-time access.

        Input:
        argv1: vertices_count, an integer representing the total number of vertices to create.

        Output: 
        None, initializes internal state

        Time complexity: 
        O(n), where n is the number of vertices.

        Time complexity analysis:
        -  A loop runs from 0 to vertices_count - 1, creating one Vertex per iteration.

        Input space complexity:
        O(1)

        Auxiliary space complexity: 
        O(n), where n is the number of vertices.

        Space complexity analysis:
        - The vertices list stores n Vertex objects.
        - Auxiliary space is constant.
        - The total space used is O(n) due to the list of Vertex objects.       
        """
        self.vertices = [None] * vertices_count  # Preallocate a list of size 'vertices_count'
        for i in range(vertices_count):
            self.vertices[i] = Vertex(i)  # Create and assign a Vertex with ID = i

    def add_edges(self, edges):
        """
        Function description: 
        Adds a list of directed edges to the graph. 
        Each edge is defined by a tuple containing the source vertex, destination vertex, cost, and time. 
        An Edge object is created and added to the corresponding source vertex's adjacency list.

        Input:
        argv1: edges, a list of tuples in the format (u, v, cost, time), where:
            - u: the source vertex ID (int)
            - v: the destination vertex ID (int)
            - cost: the cost associated with the edge (int or float)
            - time: the time required to traverse the edge (int or float)

        Output: 
        None, modifies the graph in-place by updating vertices' edge lists.

        Time complexity: 
        O(e), where e is the number of edges in the input list.

        Time complexity analysis:
        - Each edge is processed exactly once and added to the appropriate vertex.

        Input space complexity: 
        O(e), where e is the number of edges

        Auxilary space complexity: 
        O(e), where e is the number of edges

        Space complexity analysis:
        - A new Edge object is created for each edge and stored in the source vertex's edge list.
        - Only a constant amount of auxiliary memory is used for loop variables and unpacking tuples.
        - The total space used is O(e).  
        """
        for edge in edges:
            u, v, cost, time = edge  # unpack edge tuple into source, destination, cost, and time
            current_edge = Edge(u, v, cost, time)  # create an Edge instance
            self.vertices[u].add_edge(current_edge)  # add the edge to the adjacency list of vertex u

    def dijkstra(self, source):
        """
        Function description: 
        Computes the shortest paths from a given source vertex to all other vertices in the graph using Dijkstra's algorithm. 
        The method utilizes a binary min-heap to efficiently select the next vertex with the smallest known distance.
        - If a vertex is unreachable, its corresponding path is returned as an empty list.
        - The algorithm builds complete shortest-path trees and is suitable for single-source all-destination queries.

        Approach description: 
        - Uses a binary min-heap 'discovered' to prioritize processing the vertex with the smallest tentative distance.
        - Initializes all vertices as unvisited with infinite distance.
        - Sets the source distance to 0 and adds it to the heap.
        - Iteratively processes the vertex with the smallest distance, updating neighbors' distances and predecessors.
        - After completion, reconstructs shortest paths from the source to each vertex.

        Input:
        argv1: source, an integer representing the source vertex ID from which paths are computed.

        Output:
        distances (List[float]): Shortest distances from source to each vertex.
        all_paths (List[List[int]]): Paths from source to each vertex (as sequences of vertex IDs).

        Time complexity: 
        O((V + E) * log(V)), where V is the number of vertices, E is the number of edges.

        Time complexity analysis:
        - Each vertex is inserted and removed from the heap once - O(V log V)
        - Each edge is checked and possibly relaxed - O(E log V)
        - Overall, O((V + E) log V)

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(V), where V is the number of vertices.

        Space complexity analysis:
        - Stores distance, previous, and visited/discovered flags for V vertices
        - Two heaps store at most V elements
        - Output lists store paths for V vertices
        - No large temporary data structures beyond that.
        - Overall, this results in a total space complexity of O(V).
        """
        # Reset all vertices before running Dijkstra
        for vertex in self.vertices:
            vertex.distance = float('inf') # Start with infinite distance
            vertex.previous = None # No known predecessor yet
            vertex.visited = False  # Mark all as unvisited
            vertex.discovered = False # Not yet discovered

        # Min-heaps for discovered and visited vertices
        #return_dijkstra = MinHeap(len(self.vertices))  # Final list of processed vertices
        discovered = MinHeap(len(self.vertices))  # Priority queue for discovered vertices

        # Initialization with source vertex
        self.vertices[source].distance = 0
        discovered.add(self.vertices[source])
        self.vertices[source].discovered = True

        # Main loop: process discovered vertices
        while len(discovered) > 0:
            u = discovered.get_min()  # Get vertex with smallest tentative distance
            u.visited = True # Mark as visitee 
            #return_dijkstra.add(u)

            # Explore all neighbors of u
            for edge in u.edges:
                v = self.vertices[edge.v]  # Destination vertex of the edge

                if not v.visited:
                    # If the new path through u is shorter, update v's distance and predecessor
                    if v.distance > u.distance + edge.cost:
                        v.distance = u.distance + edge.cost  # Update shortest distance
                        v.previous = u  # Set predecessor for path reconstruction

                        if not v.discovered:
                            discovered.add(v)   # Add to heap if not already discovered
                            v.discovered = True  # Mark as discovered

    def get_path(self, target_id):
        """
        Function description: 
        This function reconstructs the shortest path from the source vertex to the target vertex using the 'previous' pointers set during the execution of Dijkstra's algorithm. 
        It traces the path back from the target vertex to the source by following the `previous` pointers, then reverses the path to return it in the correct order from source to target.

        Input:
        argv1: target_id, an integer representing the target vertex ID whose path from the source is being retrieved.

        Output: 
        List[int], a list of vertex IDs representing the shortest path from the source to the target.

        Time complexity: 
        O(V), where V is the number of vertices in the graph.

        Time complexity analysis:
        - The algorithm traverses from the target vertex back to the source vertex following the 'previous' pointers.
        - In the worst case, it visits all the vertices in the path, which could be of length up to V.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(V), where V is the number of vertices in the graph, because the path list may store up to V vertices in the worst case.

        Space complexity analysis:
        - The space is used for the 'path' list, which stores vertex IDs along the shortest path. In the worst case, this list may contain all vertices in the path.
        - The auxiliary space used is O(V) for the path list.
        - Overall, this results in a total space complexity of O(V).
        """
        path = []  # Initialize an empty list to store the path
        current = self.vertices[target_id]  # Start from the target vertex
        
        # Trace back the path by following the 'previous' pointers
        while current is not None:
            path.append(current.id)  # Add the current vertex's ID to the path
            current = current.previous  # Move to the previous vertex
        
        path.reverse()  # Reverse the path to get the correct order from source to target
        return path  # Return the final path
    
    
class Vertex:
    def __init__(self, id):
        """
        Function description: 
        This function initializes a Vertex object with default values used in graph traversal and shortest path algorithms such as Dijkstra's.

        Input:
        argv1: id, an integer representing the unique identifier for the vertex.

        Output: 
        A Vertex object with initialized attributes.

        Time complexity: 
        O(1)

        Time complexity analysis:
        - The constructor sets constant-time attributes and creates an empty list.
        - No loops or recursive structures involved.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - Each vertex holds a constant number of attributes and references.
        - The memory usage scales per object but does not depend on input size.
        - Overall, this results in a total space complexity of O(1).
        """
        self.id = id  # Unique identifier for this vertex
        self.edges = [] # List to hold outgoing edges from this vertex
        self.visited = False # Tracks if the vertex has been fully processed
        self.discovered = False  # Tracks if the vertex has been added to the priority queue
        self.distance = float('inf')  # Distance from the source node; starts as infinite
        self.previous = None  # Previous vertex in the shortest path
        self.intercept = False  # To indicate intercept conditions

    def add_edge(self, edge):
        """
        Function description: 
        This function adds an edge to the vertex's list of outgoing edges.

        Input:
        argv1: edge, an Edge object representing a directed connection from this vertex to another.

        Output: 
        None, modifies the vertex's internal edge list

        Time complexity: 
        O(1)

        Time complexity analysis:
        - Appending an item to a list is a constant-time operation.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - No new data structures are created; the edge reference is added to an existing list.
        - No additional memory is allocated beyond appending the reference.
        - Overall, this results in a total space complexity of O(1).
        """
        self.edges.append(edge)  # Append the given edge to the vertex's outgoing edge list


class Edge:
    def __init__(self, u, v, cost, time):
        """
        Function description: 
        This function initializes an Edge object representing a directed connection from vertex u to vertex v, with associated traversal cost and time.

        Input: 
        argv1: u, an integer representing the starting vertex (source)
        argv2: v, an integer representing the ending vertex (destination)
        argv3: cost, an integer representing the cost to traverse this edge (e.g., distance, fuel)
        argv4: time, an integer representing the time required to traverse this edge

        Output: 
        An Edge object with the specified source, destination, cost, and time attributes

        Time complexity: 
        O(1)

        Time complexity analysis:
        - Simple assignment operations are performed, all constant time.

        Input space complexity: 
        O(1)

        Auxiliary space complexity: 
        O(1)

        Space complexity analysis:
        - Each edge holds a fixed number of primitive attributes (integers).
        - No additional dynamic memory is allocated.
        - Overall, this results in a total space complexity of O(1).
        """
        self.u = u  # Source vertex ID
        self.v = v   # Destination vertex ID
        self.cost = cost  # Cost to travel this edge (used in Dijkstra)
        self.time = time  # Time to travel this edge (used in simulation/timing logic)

def multiverse_graphs(original_graph, T):
    """
    Function description: 
    This function constructs a time-expanded graph (a multiverse model), where each vertex is duplicated T times to represent different time states (modulo T).
    It models how time progresses in the graph when edges take time to traverse.

    Input:
    argv1: original_graph, a Graph object representing the original network of vertices and edges
    argv2: T, an integer representing the cycle length (modulo time); used to unfold time into layers

    Output: 
    A Graph object representing the multiverse (time-expanded) version of the original graph,
    where each vertex u is duplicated T times as u + t * N (N = number of original vertices), capturing transitions over time.

    Time complexity: 
    O(T * E), where T is the number of time layers, and E is the number of edges in the original graph.

    Time complexity analysis:
    - Each vertex is visited T times (once per time layer).
    - For each of the E edges, one new edge is added per time layer - T * E total edges.

    Input space complexity: 
    O(T * (V + E)), where V is the number of vertices, and E is the number of edges in the original graph.

    Auxiliary space complexity:
    O(T * (V + E)), since T layers of vertices and corresponding edges are stored.

    Space complexity analysis:
    - T copies of V vertices - O(T * V)
    - Each edge added once per time layer - O(T * E)
    - Overall, the total space complexity is O(T * (V + E)).
    """
    multiverse = Graph(len(original_graph.vertices) * T)  # Create T layers of the graph

    for t in range(T):  # For each time step (modulo T)
        for u in range(len(original_graph.vertices)):  # For each vertex in the original graph
            for edge in original_graph.vertices[u].edges:  # For each edge from vertex u
                v = edge.v         # Destination of the edge
                cost = edge.cost   # Cost of traversing the edge
                time = edge.time   # Time it takes to traverse the edge

                # Compute vertex IDs in the time-expanded graph
                u_time = u + t * len(original_graph.vertices)  # Source node in time layer t
                v_time = v + ((t + time) % T) * len(original_graph.vertices)  # Dest node in layer (t + time) % T

                # Add the edge to the multiverse graph with updated time-layered IDs
                multiverse.vertices[u_time].add_edge(Edge(u_time, v_time, cost, time))

    return multiverse  # Return the time-expanded graph
    
def compute_cost_and_time(path, graph):
    """
    Function description: 
    This function computes the total cost and total time taken to traverse a given path in a graph. 
    It sums the individual edge costs and times between consecutive vertices along the path.

    Input: 
    argv1: path, a list of integers representing the sequence of vertex IDs in the path
    argv2: graph, a Graph object containing the vertices and their edges

    Output:
    A tuple (total_cost, total_time), representing:
        - total_cost: the cumulative cost of the path
        - total_time: the cumulative time taken along the path

    Time complexity: 
    O(L), where L is the number of edges in the path (i.e., len(path) - 1)

    Time complexity analysis:
    - For each consecutive pair of vertices in the path, we scan the edges of the starting vertex.
    - In the worst case, we scan all edges of a vertex, but assuming sparse graphs or correct edges being early, it's efficient.

    Space complexity: 
    O(1)

    Auxiliary space complexity:
    O(1)

    Space complexity analysis:
    - Only constant space is used for tracking total cost and time.
    - No additional data structures are used. 
    - Overall, total space complexity is O(1).
    """
    total_cost = 0  # Initialize cost accumulator
    total_time = 0  # Initialize time accumulator

    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]  # Consecutive vertex pair

        vertex_u = graph.vertices[u]  # Access vertex u in the graph

        for edge in vertex_u.edges:  # Iterate through all edges from vertex u
            if edge.v == v:  # Look for edge leading to v
                total_cost += edge.cost  # Add the cost of this edge
                total_time += edge.time  # Add the time of this edge
                break  # Stop after finding the edge (assuming unique edges between pairs)

    return total_cost, total_time  # Return accumulated values

def friend_position_at_time(stations, start_idx, time):
    """
    Function description: 
    This function calculates the friend's current position in a cycle of stations after a certain amount of elapsed time. 
    It determines on which leg of the journey (between which two stations) the friend currently is, and how far along that leg they have traveled.

    Input: 
    argv1: stations, a list of (station_id, travel_time) tuples representing a cycle of stations. Each tuple defines the station and the time it takes to reach the next.
    argv2: start_idx, the index in the list where the friend starts from.
    argv3: time, the total time elapsed since the friend began their journey.

    Output: 
    A tuple (station_id, progress) where:
         - station_id: the station the friend departed from or arrived at.
         - progress: how many units of time into the current leg the friend is (0 means just departed from the current station).

    Time complexity: 
    O(n), where n is the number of stations in the cycle

    Time complexity analysis:
    - The loop iterates through the stations and reduces the remaining time, so it will run at most n times.
    - In the worst case, the friend completes nearly a full cycle, requiring O(n) steps.

    Input space complexity: 
    O(1)

    Auxiliary space complexity: 
    O(1)

    Space complexity analysis:
    - Only a constant number of variables are used regardless of the number of stations or time elapsed.
    - Overall, the total space complexity is O(1).
    """
    n = len(stations)  # Total number of stations in the cycle
    idx = start_idx # Current index in the station list
    t = time # Remaining time to simulate

    # Loop through the cycle until we find where the friend is
    while t >= 0:
        current_station, travel_time = stations[idx]  # Station and time to next
        next_idx = (idx + 1) % n  # Wrap around to simulate a cycle
        next_station, _ = stations[next_idx]  # Next station in the cycle

        if t < travel_time:
            # Friend hasn't finished this leg yet
            return (current_station, t)  # t units into the current edge
        else:
            # Finished this leg, move to the next
            t -= travel_time
            idx = next_idx

            if t == 0:
                # Just arrived at the next station
                return (next_station, 0)
            
def intercept(roads, stations, start, friendStart):
    """
    Function description: 
    This function determines the earliest station and time at which a driver can intercept a friend who is cycling repeatedly through a loop of stations.

    Approach description: 
    The approach involves simulating the friend's cycling route as a repeated cycle, and building a time-expanded graph ("multiverse") that represents possible driver positions at each unit of time modulo the friend's full loop duration. 
    Dijkstra's algorithm is then used on the multiverse graph to compute shortest paths from the driver's starting point at time zero. 
    The simulation tracks the friend's position at every time unit, and an interception is considered successful if the driver reaches the same station at the same time the friend is there (and not in transit).

    Input:
    argv1: roads (list[tuple[int, int, int, int]]), A list of roads in the format (u, v, cost, time) representing roads between nodes with associated travel cost and time.
    argv2: stations (list[int] or list[tuple[int, int]]),  A list of station IDs or (station_id, travel_time) tuples representing the cycle the friend is traveling through.
    argv3: start (int): The driver's starting station ID.
    argv4: friendStart (int): The friend's starting station ID (must be in the stations list).

    Output:
    tuple[int, int, list[int]]: A tuple containing:
        - the minimum cost to intercept the friend
        - the time at which the interception occurs
        - the path taken by the driver to reach the interception point.

    Time complexity: 
    O((L * T + R * T) * log(L * T)), where:
        L = number of vertices in the base graph,
        R = number of edges in the base graph,
        T = total time for the friend to complete one full cycle.

    Time complexity analysis:
    - The time-expanded graph contains V * T nodes and up to E * T edges.
    - Dijkstra's algorithm on this graph yields the stated complexity.
    - The final complexity is O(R Log L), after removing the constants T and dropping R as L dominates.

    Input space complexity:
    O(R + S), where R is the number of roads, S is the number of stations

    Auxiliary space complexity: 
    O(L + R) * T, where L is the number of locations, R is the number of roads, T is the cycle time.

    Space complexity analysis:
    - The multiverse graph requires O(V * T) space to store vertices and edges.
    - Distance tracking, visited flags, and path reconstruction also require O(V * T) space.
    - Overall, the total space complexity is O(L + R), after removing the constants T and dropping (R + S) as (L + R) dominates. 
    """
    # Extract station IDs from tuples
    station_ids = [s[0] for s in stations]

    # Create a graph for the station cycle
    station_graph = Graph(max(station_ids) + 1)
    station_edges = []

    # Convert each leg of the cycle into a directed edge
    for i in range(len(stations)):
        u, travel_time = stations[i]
        v, _ = stations[(i + 1) % len(stations)]  # Wrap around
        station_edges.append((u, v, 0, travel_time))  # Edge has zero cost, only time matters

    station_graph.add_edges(station_edges)

    # Compute the total time it takes for the friend to complete one cycle
    cycle_time = 0
    for i in range(len(station_ids)):
        u = station_ids[i]
        v = station_ids[(i + 1) % len(station_ids)]
        found_edge = None
        for edge in station_graph.vertices[u].edges:
            if edge.v == v:
                found_edge = edge
                break
        if found_edge is None:
            return None  # Edge missing, cannot simulate the cycle
        cycle_time += found_edge.time

    if cycle_time == 0:
        return None  # Invalid cycle

    # Build the base graph from road input
    base_graph = Graph(max(max(u, v) for u, v, *_ in roads) + 1)
    base_graph.add_edges(roads)

    # Build the time-expanded multiverse graph
    multiverse = multiverse_graphs(base_graph, cycle_time)

    # Track friend's position at each minute in the cycle
    friend_positions = [None] * cycle_time
    idx = station_ids.index(friendStart)
    t = 0
    i = idx
    while t < cycle_time:
        u, travel_time = stations[i]
        v = stations[(i + 1) % len(stations)][0]

        current_time = t
        if travel_time > 0 and current_time < cycle_time:
            multiverse_id = u + current_time * len(base_graph.vertices)
            multiverse.vertices[multiverse_id].intercept = True  # Mark possible interception point
            friend_positions[current_time] = u

        # Friend in transit: skip marking multiverse during travel
        for progress in range(1, travel_time):
            current_time = t + progress
            if current_time >= cycle_time:
                break

        t += travel_time
        i = (i + 1) % len(stations)

    # Begin Dijkstra from the driver’s start station at time = 0
    start_node = start + 0 * len(base_graph.vertices)
    multiverse.dijkstra(start_node)

    friend_idx = station_ids.index(friendStart)
    best_result = None

    # Check every vertex to see if it's a valid interception point
    for node_id, vertex in enumerate(multiverse.vertices):
        if vertex.distance == float('inf') or not hasattr(vertex, "intercept") or not vertex.intercept:
            continue

        path = multiverse.get_path(node_id)
        if not path:
            continue
        if not path or multiverse.vertices[node_id].distance == float('inf'):
            continue

        _, time = compute_cost_and_time(path, multiverse)
        real_node = node_id % len(base_graph.vertices)

        friend_location, progress = friend_position_at_time(stations, friend_idx, time)
        driver_cost, _ = compute_cost_and_time([p % len(base_graph.vertices) for p in path], base_graph)

        # Valid intercept only if friend is at node (not between) and both align
        intercept_possible = (progress == 0 and real_node == friend_location)

        if intercept_possible:
            if best_result is None or driver_cost < best_result[0] or (driver_cost == best_result[0] and time < best_result[1]):
                best_result = (driver_cost, time, [p % len(base_graph.vertices) for p in path])

    return best_result  # Return best interception route if any
    


