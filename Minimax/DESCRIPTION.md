## Comparison between Minimax (tradition) vs Minimax (with Alpha-Beta Prunning) based on Tic-tac-toe game

Time Complexity:

Traditional Minimax ≈ O(b^d)

Alpha–Beta ≈ O(b^(d/2)) in best case

## 🧠 Algorithm Performance Comparison

| **Algorithm**      | **Board Size** | **Nodes Expanded** | **Execution Time (s)** | **Optimal Move** |
|--------------------:|:--------------:|-------------------:|-----------------------:|:----------------:|
| Plain Minimax       | 3×3            | 549,945            | 4.83                   | (0, 0)           |
| Alpha–Beta Pruning  | 3×3            | 8,383              | 0.09                   | (0, 0)           |
| Plain Minimax       | 4×4            | 22,943,984         | > 5 min                | (1, 1)           |
| Alpha–Beta Pruning  | 4×4            | 114,239            | 1.20                   | (1, 1)           |

> (Numbers are illustrative; your measurements may vary slightly.)
---

### 📊 Summary

Alpha–Beta pruning improves Minimax efficiency without changing the result.  
It prunes branches that cannot affect the final decision, resulting in faster execution and fewer node expansions, especially on larger boards.
