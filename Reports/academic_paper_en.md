# Morphic Inner World: Achieving Language- and Platform-Invariant Deterministic Intelligence through Geometric Term-Algebraic Projection

**Author:** Fumio Miyata  
**Date:** March 9, 2026  
**DOI:** https://doi.org/10.5281/zenodo.18905026  
**Keywords:** Cognitive Architecture, Symbolic Reasoning, Term Algebra, Compositionality, Deterministic Inference, Language Invariance, Platform Invariance

---

## Abstract
Reliable compositional reasoning remains a central challenge in artificial intelligence. While modern large language models demonstrate impressive linguistic capabilities, they often exhibit instability when reasoning over deeply nested or structurally complex tasks. This paper introduces **Morphic Inner World (MIW)**, a cognitive architecture designed to explore the potential for **Language- and Platform-Invariant Deterministic Intelligence**. We model reasoning as a structure-preserving **geometric projection** from natural language into a symbolic reasoning space defined as a **free term algebra**. By utilizing a strategic longest-match tokenizer, a fixed dictionary of **44 Morphic Primitives**, and a decoupled **Wisdom Base**, MIW aims to provide a high degree of logical consistency across multiple languages (English/Japanese) and execution kernels (Python/Fortran). Evaluation against a benchmark of 60 tasks yielded 100.0% accuracy and bit-identical parity, suggesting a potential for effectively decoupling logical substance from its linguistic and physical substrates within the evaluated scope.

---

## 1. Introduction
Modern neural language models struggle with **systematic compositional reasoning**, particularly in tasks requiring precise structural manipulation (Lake & Baroni, 2018; Liu et al., 2023). These limitations are often attributed to the probabilistic nature of transformer-based architectures, which may lack a rigid structural anchor. Historically, cognitive architectures like **ACT-R** and **SOAR** provided structured frameworks but often relied on heuristic search. This paper proposes MIW, where reasoning is modeled as a **deterministic algebraic reduction** within a term-algebraic manifold.

---

## 2. Architecture and Formal Model

### 2.1 The Global Flow
The MIW architecture processes input through a unidirectional three-stage pipeline (Fig. 1). From an information-theoretic perspective, this process can be viewed as a transition from high-entropy linguistic input to a low-entropy, structured logical normal form.

![Fig. 1: Overview of the MIW architecture. Natural language is projected via a deterministic tokenizer into primitive operators (Sec 2.2), composed into symbolic structures (Sec 3.1), and reduced to normal form (Sec 3.2). MSP Check (Sec 2.2) and the 44 Primitives (Sec 2.3) are intended to maintain structural integrity.](images/fig1_global_flow.pdf)

### 2.2 Input Projection and MSP Check
The projection phase $h: \mathcal{L} \to \Sigma^*$ is designed to be strictly deterministic. It employs:
1.  **Strategic Longest-Match Tokenization**: To resolve semantic ambiguity without complex parsers, phrases in the dictionary are sorted by character length in descending order before matching. This is intended to ensure that more specific, complex intents (e.g., "sort by end time") are prioritized over generic sub-components (e.g., "sort"), thereby reducing overlapping term interference.
2.  **MSP (Morphic Structural Pointers)**: Numbered markers (e.g., "1.", "2.") serve as structural anchors. The synthesizer is configured to filter out text outside these anchors, treating it as background noise. This protocol aims to allow the system to extract precise logic even from documents exceeding 8,000 tokens of unstructured text.

### 2.3 Morphic Primitives and Wisdom Base
The dictionary consists of **44 irreducible primitives** ($\Sigma$). A key architectural feature is the **Wisdom Base (WB)**, a decoupling layer that maps abstract primitive IDs to platform-specific implementations. This registry is designed to allow the same logical structure (AST) to be instantiated across kernels (Python vs. Fortran) while maintaining functional equivalence. 

Furthermore, MIW employs **Semantic Cleansing** at the boundary of the execution kernel, with the goal of normalizing native input data into Morphic Values before evaluation. Complex recursive algorithms are treated as **Fixpoint Packages**—atomic primitives that encapsulate internal structural recursion—allowing the synthesis engine to maintain a manageable logical flow during the execution of high-complexity tasks. This set forms the basis of the free term algebra $\mathcal{M} = \mathcal{T}(\Sigma, \mathcal{V})$.

---

## 3. Structural Synthesis and Evaluation Semantics

Synthesis $g: \Sigma^* \to \mathcal{M}$ constructs symbolic trees satisfying mandatory arity constraints $\alpha(P)$. The synthesis engine utilizes **Arity-based Partial Application**, where functions are transformed into closures ($VClosure$) until all required arguments are supplied. This facilitates the dynamic composition of logic from linear natural language phrases. 

Furthermore, logical steps are composed into an **Immutable DAG Structure** using nested `Let` bindings. This is intended to ensure that each intermediate result is an immutable named object within the evaluation scope, aiming to eliminate side effects and provide a clear lineage for computed values. Evaluation is performed via deterministic rewrite rules $R_P$, ensuring termination and confluence (see Appendix A).

![Fig. 2: Arity-based Recursive Folding. The synthesis engine recursively composes primitives into an irreducible AST structure by validating arity constraints $\alpha(P)$ against available arguments.](images/fig2_folding.pdf)

---

## 4. Examples of Compositional Reasoning
MIW was applied to diverse reasoning categories beyond simple sorting:
- **Algorithmic**: `FILTER(EVEN, SORT(numbers))`.
- **Spatial Reasoning**: `DIJKSTRA(graph, start, end)`.
- **Constraint Satisfaction**: `SOLVE_SUDOKU(grid)`.
- **Optimization**: `TREE_MAX_PATH(root)`.

---

## 5. Experimental Evaluation
MIW was evaluated against 60 compositional tasks, achieving a 100.0% success rate within the tested parameters. Key scaling results observed include:
- **v=8000**: Robust extraction under extreme context noise.
- **d=15**: Correct execution of 15-level nested logic.
- **n=20**: Simultaneous verification of 20+ independent logical constraints.
The **n=20** result illustrates a capacity for maintaining logical consistency far exceeding typical human cognitive spans (Miller's Law, 7±2). Within the scope of this study, results achieved bit-identical parity between Python and Modern Fortran kernels.

---

## 6. Discussion: Relation to Neuro-symbolic AI
Unlike neuro-symbolic systems such as DeepProbLog, MIW operates as a pure algebraic reduction engine. By replacing stochastic search with deterministic projection, MIW aims to offer zero inference variance, linear computational cost, and direct interpretability.

Furthermore, the 100.0% parity achieved across English and Japanese specifications in this study provides empirical evidence of a fundamental **decoupling between linguistic form and logical substance**. In the MIW framework, natural language serves as a coordinate system used to orient and trigger logical primitives. This **Language Invariance** suggests that the "geometry of thought"—represented here as a formal AST—may function as a universal invariant, independent of the specific linguistic shell used for its transmission. By isolating knowledge into 44 irreducible primitives, MIW illustrates a pathway toward rendering intelligence more robust against the stochastic noise of human language.

Finally, the decision to utilize two fundamentally contrasting programming paradigms—**Python** and **Modern Fortran**—was intended to test implementation invariance. The achievement of **bit-identical parity** between these disparate execution kernels supports the concept of **Platform Invariance**. It indicates that the reduction of logic to a Normal Form can be a mathematical necessity that transcends the specific idioms of a computing environment. By decoupling the "logic of thought" from the "mechanics of execution," MIW demonstrates the potential to liberate deterministic intelligence from its underlying substrate, providing a foundation for cross-platform cognitive verification.

---

## 7. Conclusion
MIW provides evidence that compositional reasoning can be implemented as a deterministic structure-preserving mapping. Future work will explore hybridization with probabilistic models to bridge structural and perceptual grounding. Furthermore, the potential introduction of **Sheaf Theory** into the Morphic Core language—treating knowledge as a structure over topological spaces—may pave the way for a more generalized **Geometric Cognition** capable of handling complex overlapping environmental manifolds.

---

## Data Availability Statement
The full source code for the MIW kernels (Python and Modern Fortran), the benchmark suite consisting of 60 algorithmic tasks, and the synthesis/execution logs are available for peer review and replication at the following repository: [https://github.com/aikenkyu001/morphic_inner_world](https://github.com/aikenkyu001/morphic_inner_world). The dataset is also archived via Zenodo (DOI: [10.5281/zenodo.18905026](https://doi.org/10.5281/zenodo.18905026)).

---

## Appendix A: Formal Reduction Semantics
Evaluation is defined as a reduction to **Normal Form (NF)**. The evaluation function $Eval: \mathcal{T}(\Sigma, \mathcal{V}) \to NF$ is defined by:
1. $Eval(c) = c$ for atomic literals.
2. $Eval(P(t_1, ..., t_n)) = R_P(Eval(t_1), ..., Eval(t_n))$ for applications.
Termination and confluence are ensured by finite arity constraints and orthogonality of rewrite rules.

To maintain absolute predictability, MIW employs **Deterministic Error Handling**. Instead of triggering system-level exceptions, the evaluator returns a **VError** value in cases of undefined operations or type mismatches. This approach treats errors as legitimate states within the logic, ensuring that the kernel never crashes and always produces a well-defined result even under failure conditions.

![Fig. 3: Multi-Kernel Deterministic Reduction. The Abstract Syntax Tree is evaluated through independent Python and Modern Fortran kernels, converging on a bit-identical Normal Form to verify implementation invariance.](images/fig3_reduction.pdf)

## Appendix B: Benchmark Tasks
Full task list is available via **Zenodo (DOI: 10.5281/zenodo.18905026)**.

## Appendix C: Full List of Morphic Primitives ($\Sigma$)
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
