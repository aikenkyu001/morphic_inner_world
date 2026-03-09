# Morphic Inner World: A Deterministic Term-Algebra Cognitive Architecture Framework for Compositional Reasoning

**Author:** Fumio Miyata  
**Date:** March 9, 2026  
**DOI:** https://doi.org/10.5281/zenodo.18905026  
**Keywords:** Cognitive Architecture, Symbolic Reasoning, Term Algebra, Compositionality, Deterministic Inference

---

## Abstract
Reliable compositional reasoning remains a central challenge in artificial intelligence. While modern large language models demonstrate impressive linguistic capabilities, they often exhibit instability when reasoning over deeply nested or structurally complex tasks. This paper introduces **Morphic Inner World (MIW)**, a deterministic cognitive architecture that models reasoning as a structure-preserving projection from natural language into a symbolic reasoning space defined as a **free term algebra**. We formally define the projection mechanism, which utilizes a deterministic longest-match tokenizer and a fixed dictionary of **44 Morphic Primitives**, ensuring absolute logical consistency without reliance on probabilistic inference. The architecture is evaluated against a benchmark of 60 tasks encompassing algorithmic, spatial, and constraint-based reasoning. Results demonstrate 100.0% accuracy and implementation invariance across Python and Modern Fortran kernels.

---

## 1. Introduction
Modern neural language models struggle with **systematic compositional reasoning**, particularly in tasks requiring precise structural manipulation (Lake & Baroni, 2018; Liu et al., 2023). These limitations stem from the probabilistic nature of transformer-based architectures, which lack a rigid structural anchor. Historically, cognitive architectures like **ACT-R** and **SOAR** provided structured frameworks but often relied on heuristic search. This paper proposes MIW, where reasoning is a **deterministic algebraic reduction** within a term-algebraic manifold.

---

## 2. Architecture and Formal Model

### 2.1 The Global Flow
The MIW architecture processes input through a unidirectional three-stage pipeline (Fig. 1). From an information-theoretic perspective, this represents a transition from high-entropy linguistic input to a low-entropy, structured logical normal form.

![Fig. 1: Overview of the MIW architecture. Natural language is projected via a deterministic tokenizer into primitive operators (Sec 2.2), composed into symbolic structures (Sec 3.1), and reduced to normal form (Sec 3.2). MSP Check (Sec 2.2) and the 44 Primitives (Sec 2.3) ensure structural integrity.](images/fig1_global_flow.pdf)

### 2.2 Input Projection and MSP Check
The projection phase $h: \mathcal{L} \to \Sigma^*$ is strictly deterministic. It employs:
1.  **Longest-Match Tokenization**: Phrases are matched against a **Semantic Dictionary** using a greedy longest-prefix strategy. Within the current scope, linguistic ambiguity is avoided through the use of a **Controlled Vocabulary**, ensuring a one-to-one mapping between task intents and primitives.
2.  **MSP (Morphic Structural Pointers)**: Numbered markers (e.g., "1.", "2.") serve as structural anchors to identify logical blocks, allowing the system to ignore surrounding high-entropy noise.

### 2.3 Morphic Primitives (Σ)
The dictionary consists of **44 irreducible primitives** selected based on fundamental functional programming operations and core cognitive tasks (see Appendix C). This set forms the basis of the free term algebra $M = \mathcal{T}(\Sigma, V)$.

---

## 3. Structural Synthesis and Evaluation Semantics

Synthesis $g: \Sigma^* \to \mathcal{M}$ constructs symbolic trees satisfying mandatory arity constraints $\alpha(P)$. Evaluation is performed via deterministic rewrite rules $R_P$, ensuring termination and confluence (see Appendix A).

---

## 4. Examples of Compositional Reasoning
MIW handles diverse reasoning categories beyond simple sorting:
- **Algorithmic**: `FILTER(EVEN, SORT(numbers))`.
- **Spatial Reasoning**: `DIJKSTRA(graph, start, end)`.
- **Constraint Satisfaction**: `SOLVE_SUDOKU(grid)`.
- **Optimization**: `TREE_MAX_PATH(root)`.

---

## 5. Experimental Evaluation
MIW maintained a 100.0% success rate across 60 compositional tasks up to $v=8000$ and $d=15$. Results achieved bit-identical parity between Python and Modern Fortran kernels.

---

## 6. Discussion: Relation to Neuro-symbolic AI
Unlike neuro-symbolic systems such as DeepProbLog, MIW operates as a pure algebraic reduction engine. By replacing stochastic search with deterministic projection, MIW offers zero inference variance, linear computational cost, and direct interpretability.

---

## 7. Conclusion
MIW demonstrates that compositional reasoning can be implemented as a deterministic structure-preserving mapping. Future work will explore hybridization with probabilistic models to bridge structural and perceptual grounding.

---

## Appendix A: Formal Reduction Semantics
Evaluation is defined as a reduction to **Normal Form (NF)**. The evaluation function $Eval: \mathcal{T}(\Sigma, \mathcal{V}) \to NF$ is defined by:
1. $Eval(c) = c$ for atomic literals.
2. $Eval(P(t_1, ..., t_n)) = R_P(Eval(t_1), ..., Eval(t_n))$ for applications.
Termination and confluence are ensured by finite arity constraints and orthogonality of rewrite rules.

## Appendix B: Benchmark Tasks
Full task list is available via **Zenodo (DOI: 10.5281/zenodo.18905026)**.

## Appendix C: Full List of Morphic Primitives (Σ)
| Primitive | Arity | Primitive | Arity |
| :--- | :---: | :--- | :---: |
| autocomplete_trie | 2 | matrix_chain | 1 |
| bitmask_group | 1 | merge_intervals | 1 |
| bitwise_range_and | 2 | merge_k_lists | 1 |
| boggle_solve | 2 | mergesort | 1 |
| check_constraints | 1 | mst_prim | 2 |
| composite_task_60 | 2 | optimal_bst | 1 |
| deserialize_tree | 1 | permute_dup | 1 |
| dijkstra | 3 | process_context | 2 |
| filter_overlapping | 1 | quicksort | 1 |
| flatten_nesting | 1 | rain_3d | 1 |
| fractional_knapsack | 2 | reconstruct_list | 1 |
| identity | 1 | redundant_conn | 1 |
| is_valid_parentheses | 1 | regex_match | 2 |
| kth_largest | 2 | rotate_matrix | 1 |
| ladder_all | 3 | serialize_tree | 1 |
| lca_nary | 3 | solve_sudoku | 1 |
| lcs | 2 | sort_by_end | 1 |
| length | 1 | sparse_mul | 2 |
| lru_cache_concurrent | 2 | spiral_gen | 1 |
| lru_cache_op | 2 | text_justify | 2 |
| tree_max_path | 1 | word_break | 2 |
| word_ladder_bfs | 3 | word_search_2 | 2 |

---

## References

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111, 1036–1060.
- Bender, E. M., & Koller, A. (2020). Climbing towards NLU. *Proceedings of the ACL*.
- Church, A. (1932). A set of postulates for the foundation of logic. *Annals of Mathematics*, 33, 346–366.
- Harnad, S. (1990). The symbol grounding problem. *Physica D*, 42, 335–346.
- Indiveri, G., & Liu, S.-C. (2021). Introducing 'Neuromorphic Computing and Engineering'. *Neuromorphic Computing and Engineering*, 1(1), 010001.
- Kotseruba, I., & Tsotsos, J. K. (2020). 40 years of cognitive architectures. *AI Review*, 53(1), 17–94.
- Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *Proceedings of ICML*.
- Landin, P. J. (1964). The mechanical evaluation of expressions. *The Computer Journal*, 6(4), 308–320.
- Liu, N. F., et al. (2023). Lost in the Middle. *TACL*.
- Sandamirskaya, Y. (2014). Dynamic neural fields as a step toward cognitive neuromorphic architectures. *Frontiers in Neuroscience*, 7, 276.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.
- Wadler, P. (2015). Propositions as Types. *Communications of the ACM*, 58(12), 75–84.
