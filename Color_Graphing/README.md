# 🎨 **Graph Coloring Problem explain:**
Giving a graph:
<img width="498" height="382" alt="image" src="https://github.com/user-attachments/assets/6e961ea8-9b4d-4c21-91bd-006b67d4a7f4" />

*Which we need to coloring each node individually, in real-time case it would have take faster if we color through instinct, that would be very efficient on small tree, while on wider problem like a map of a country, coloring them would be a paint, thats when Graph Coloring Problem kicking in"
There are multiple way to approach, including this technique called: Graph Coloring Problem.*
The image contains notes on fundamental concepts related to **Constraint Satisfaction Problems (CSP)** and their application to **Graph Coloring**.
## 1.1. 🧠 Key Concepts to Remember (Kiến thức cần nhớ)

* **Constraint :** Is a relation on a set of variables.
* **A Constraint can be represented by:** 
    * A formula (mathematics/logic). 
    * A table listing all appropriate value assignments for the variables.

* **Constraint Satisfaction Problem :**
    * A finite set of variables $X$.
    * A domain of values for each variable $D$. 
    * A finite set of constraints. 

> A solution to a Constraint Satisfaction Problem is a complete assignment of values to the variables that satisfies all constraints.

* **Optimal Graph Coloring Algorithm 

    * **Constraint:** Two adjacent vertices cannot have the same color. 
    * **Repeat the following steps until all vertices are colored:**
        * **Step 1:** Select the vertex with the largest degree and color it with color $i$. 
        * **Step 2:** Update Degrees: 
            * The colored vertex: Degree $= 0$. 
            * Its adjacent vertices: Degree $:= \text{Degree} - 1$. 
        * **Step 3:** Mark the adjacent vertices and forbid them from using color $i$. 
-----
# Step 1: 
Identify which node has the most edges (edges is determine through many vertices that connect to it)

<img width="476" height="351" alt="image" src="https://github.com/user-attachments/assets/22984249-e3f5-4147-9a75-d6e79376230d"/>



# Step 2: 
As we have 1 colored node node 3 we now proceed to decrease the edges which have connetion to node 3 , which remaining:
<img width="369" height="258" alt="image" src="https://github.com/user-attachments/assets/56d7c706-e05e-4576-b942-32c4fb56b3c8" />


# Step 3:
Continue identify which node has the most edges and we color it, we are seeing node 1 and 2 and 4 have the most edges (all 3 have 2 edges) and whichever we choose will slightly change the outcome but still on the logic track
<img width="350" height="251" alt="image" src="https://github.com/user-attachments/assets/6da5a005-7a2f-49e5-9b91-f5be0f49f8b5" />      or     <img width="338" height="252" alt="image" src="https://github.com/user-attachments/assets/4a9460de-bb73-4c6c-a833-e4da35a1d738" />



or


<img width="364" height="249" alt="image" src="https://github.com/user-attachments/assets/8e0a11af-b22f-49d0-b36d-f3cbcfdd1af0" />



# Step 4: For personal choice, me will choose node 1 colored blue , which reduced other node edges due to the constraint "which node has been color will remain edges as 0":
<img width="345" height="246" alt="image" src="https://github.com/user-attachments/assets/7f8e3a2d-3e4c-4811-87f2-a8371d0c22f8" />



# Step 5: As the constraint, "Two adjacent vertices cannot have the same color" therefore we have node 4 colored blue and reduced every other nodes related to node 4
<img width="348" height="271" alt="image" src="https://github.com/user-attachments/assets/feb5edde-ffae-4ccc-bf21-ca1f18bd6855" />


# Step 6: Follow the constraint we mentioned earlier on step 5, we will have the colored graph look like this:
<img width="342" height="270" alt="image" src="https://github.com/user-attachments/assets/9d92b373-6a24-4b40-9f44-ae74426fdee6" />
or this for full detail:
<img width="348" height="269" alt="image" src="https://github.com/user-attachments/assets/922e0eb8-f22b-4231-948f-decd596778d2" />





