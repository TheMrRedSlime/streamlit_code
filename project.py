import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Route Finder")
st.subheader("Find the shortest path between towns!")


cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore",
    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
    "Bhopal", "Nagpur", "Patna", "Chandigarh", "Guwahati"
]

city1 = st.selectbox(options=cities, label="City #1")

city2 = st.selectbox(options=cities, label="City #2")


if st.button("Compare"):
    if city1 is None or city2 is None:
        st.error("Please choose a city!")
    else:
    
        g=nx.Graph()
        g.add_nodes_from(cities)
        
        # Routes with approximate distances (in km)
        g.add_edge("Delhi", "Jaipur", weight=280)
        g.add_edge("Delhi", "Lucknow", weight=500)
        g.add_edge("Delhi", "Chandigarh", weight=250)
        g.add_edge("Delhi", "Bhopal", weight=760)
        
        g.add_edge("Jaipur", "Ahmedabad", weight=670)
        g.add_edge("Jaipur", "Mumbai", weight=1140)
        
        g.add_edge("Ahmedabad", "Mumbai", weight=530)
        g.add_edge("Mumbai", "Pune", weight=150)
        g.add_edge("Mumbai", "Hyderabad", weight=710)
        g.add_edge("Mumbai", "Nagpur", weight=820)
        
        g.add_edge("Hyderabad", "Bangalore", weight=570)
        g.add_edge("Hyderabad", "Chennai", weight=630)
        g.add_edge("Hyderabad", "Nagpur", weight=500)
        
        g.add_edge("Bangalore", "Chennai", weight=340)
        g.add_edge("Bangalore", "Pune", weight=840)
        
        g.add_edge("Kolkata", "Patna", weight=590)
        #g.add_edge("Kolkata", "Bhubaneswar", weight=440)
        g.add_edge("Kolkata", "Guwahati", weight=1030)
        g.add_edge("Kolkata", "Delhi", weight=1500)
        
        g.add_edge("Nagpur", "Bhopal", weight=350)
        g.add_edge("Lucknow", "Patna", weight=530)
        g.add_edge("Patna", "Delhi", weight=1080)

        pos = {
            "Delhi": (0.5, 0.8),
            "Chandigarh": (0.45, 0.9),
            "Jaipur": (0.4, 0.75),
            "Lucknow": (0.65, 0.75),
            "Bhopal": (0.5, 0.6),
            "Nagpur": (0.55, 0.5),
            "Ahmedabad": (0.35, 0.65),
            "Mumbai": (0.3, 0.5),
            "Pune": (0.3, 0.45),
            "Hyderabad": (0.5, 0.4),
            "Bangalore": (0.45, 0.25),
            "Chennai": (0.55, 0.2),
            "Kolkata": (0.85, 0.65),
            "Patna": (0.75, 0.7),
            "Guwahati": (0.95, 0.8),
        }
        fig, ax = plt.subplots(facecolor='grey')
        ax.set_facecolor('lightgrey')
        
        nx.draw(
            g, pos, ax=ax, with_labels=True, node_size=1000,
            node_color="green", font_color="black", edgecolors="black", font_size=12
        )

        path=nx.shortest_path(g, source=city1, target=city2)
        length=nx.shortest_path_length(g, source=city1, target=city2, weight="weight")

        st.info(f"Shortest path: {" -> ".join(path)}")
        st.info(f"Shortest length: {length}km")

        path_edges = list(zip(path, path[1:]))

        nx.draw_networkx_edges(g, pos, edgelist=path_edges, width=3, edge_color="blue")
        
        st.pyplot(fig)