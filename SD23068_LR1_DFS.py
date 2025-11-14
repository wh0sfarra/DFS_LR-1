import streamlit as st

# ==========================================
# DISPLAY GRAPH IMAGE
# ==========================================
st.title("Depth-First Search (DFS)")
st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_container_width=True)

# ==========================================
# GRAPH 
# ==========================================
graph = {
    'A': ['B','D'],
    'B': ['A','C','E','G'],
    'C': ['B','D'],
    'D': ['C'],
    'E': ['H'],
    'H': ['G','F'],
    'G': ['F'],
    'F': []
}

nodes = list(graph.keys())

# ==========================================
# DFS FUNCTION 
# ==========================================
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

    return visited

# ==========================================
# STREAMLIT UI
# ==========================================
start_node = st.selectbox("Select starting node:", nodes)

if st.button("Run DFS"):
    result = dfs(graph, start_node)
    st.subheader("DFS Traversal Order")
    st.write(" → ".join(result))
