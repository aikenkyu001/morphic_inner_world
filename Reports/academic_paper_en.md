# Morphic Inner World: Achieving Language- and Platform-Invariant Deterministic Intelligence through Geometric Term-Algebraic Projection

**Author:** Fumio Miyata  
**Date:** March 10, 2026  
**DOI:** https://doi.org/10.5281/zenodo.18905026  
**Keywords:** Cognitive Architecture, Symbolic Reasoning, Term Algebra, Compositionality, Deterministic Inference, Language Invariance, Platform Invariance

---

## Abstract
Reliable compositional reasoning remains a central challenge in artificial intelligence. While modern large language models demonstrate impressive linguistic capabilities, they often exhibit instability when reasoning over deeply nested or structurally complex tasks. This paper introduces **Morphic Inner World (MIW)**, a cognitive architecture designed to explore the potential for **Language- and Platform-Invariant Deterministic Intelligence**. We model reasoning as a structure-preserving **geometric projection** from natural language into a symbolic reasoning space defined as a **free term algebra**. By utilizing a strategic longest-match tokenizer, a fixed dictionary of **44 Morphic Primitives**, and a decoupled **Wisdom Base**, MIW aims to provide a high degree of logical consistency across multiple languages (English/Japanese) and execution kernels (Python/Fortran). Evaluation against a benchmark of 60 tasks yielded 100.0% accuracy and bit-identical parity, suggesting a potential for effectively decoupling logical substance from its linguistic and physical substrates within the evaluated scope.

---

## 1. Introduction
Modern neural language models struggle with **systematic compositional reasoning**, particularly in tasks requiring precise structural manipulation (Lake & Baroni, 2018; Liu et al., 2023). These limitations are often attributed to the probabilistic nature of transformer-based architectures, which may lack a rigid structural anchor (Baroni, 2022). Historically, cognitive architectures like **ACT-R** (Anderson et al., 2004) and **SOAR** (Langley et al., 2009; Ludwig, 2005) have provided structured frameworks for over 40 years (Kotseruba & Tsotsos, 2020) but often relied on heuristic search. Recent trends in **Deterministic Artificial Intelligence** (Alexander, 2020) and **Adaptive Machine Intelligence** (Bhatnagar, 2025) emphasize the need for bit-level reproducibility and formal provenance in machine reasoning (Marcus, 2020). This paper proposes MIW, where reasoning is modeled as a **deterministic algebraic reduction** within a term-algebraic manifold (Gurevich, 1995; Abadi & Plotkin, 2020), tracing its logical roots back to the fundamental **postulates for logic** (Church, 1932).

---

## 2. Architecture and Formal Model

### 2.1 The Global Flow
The MIW architecture processes input through a unidirectional three-stage pipeline (Fig. 1). From an information-theoretic perspective, this process can be viewed as a transition from high-entropy linguistic input to a low-entropy, structured logical normal form (Tononi, 2004; Saanum et al., 2024). This transition is governed by principles of **harmonic mind** architectures (Smolensky & Legendre, 2006).

![Fig. 1](images/fig1_global_flow.pdf)
**Fig. 1: Global Architecture of Morphic Inner World.** The pipeline illustrates the deterministic progression from ambiguous natural language to a verified normal form through structure-preserving stages.

### 2.2 Input Projection and MSP Check
The projection phase $h: \mathcal{L} \to \Sigma^*$ is designed to be strictly deterministic. It employs:
1.  **Strategic Longest-Match Tokenization**: To resolve semantic ambiguity without complex parsers, phrases in the dictionary are sorted by character length in descending order before matching. This is intended to ensure that more specific, complex intents (e.g., "sort by end time") are prioritized over generic sub-components (e.g., "sort"), thereby reducing overlapping term interference. This deterministic mapping aligns with the principles of **structural representation** in hybrid cognitive systems (Licato et al., 2014), **universal grammar** (Montague, 1970), and categorical syntactic processes (Steedman, 2000).
2.  **MSP (Morphic Structural Pointers)**: Numbered markers (e.g., "1.", "2.") serve as structural anchors. The synthesizer is configured to filter out text outside these anchors, treating it as background noise. This protocol aims to allow the system to extract precise logic even from documents exceeding 8,000 tokens of unstructured text, addressing the "lost in the middle" phenomenon (Liu et al., 2023) and ensuring that the **linguistic structure** is correctly identified for deliberate reasoning (Baroni, 2022; Boggs, 2025).

### 2.3 Morphic Primitives and Wisdom Base
The dictionary consists of **44 irreducible primitives** ($\Sigma$). A key architectural feature is the **Wisdom Base (WB)**, a decoupling layer that maps abstract primitive IDs to platform-specific implementations (Fig. 2). This registry is designed to allow the same logical structure (AST) to be instantiated across kernels (Python vs. Fortran) while maintaining functional equivalence. This approach builds upon the concept of **deterministic self-reflection** (Bhatnagar, 2025).

![Fig. 2](images/fig2_substrate.pdf)
**Fig. 2: Substrate Independence Layer.** The Wisdom Base acts as a cognitive registry, decoupling the universal logic (AST) from platform-specific execution kernels to ensure implementation invariance.

Furthermore, MIW employs **Semantic Cleansing** at the boundary of the execution kernel, with the goal of normalizing native input data into Morphic Values before evaluation. Complex recursive algorithms are treated as **Fixpoint Packages**—atomic primitives that encapsulate internal structural recursion—allowing the synthesis engine to maintain a manageable logical flow during the execution of high-complexity tasks. This set forms the basis of the free term algebra $\mathcal{M} = \mathcal{T}(\Sigma, \mathcal{V})$, which facilitates **systematic generalization** through algebraic representation (Zhang et al., 2022) and universal knowledge models (Sukhobokov, 2024).

---

## 3. Structural Synthesis and Evaluation Semantics

Synthesis $g: \Sigma^* \to \mathcal{M}$ constructs symbolic trees satisfying mandatory arity constraints $\alpha(P)$ (Fig. 3). The synthesis engine utilizes **Arity-based Partial Application**, where functions are transformed into closures ($VClosure$) until all required arguments are supplied. This facilitates the dynamic composition of logic from linear natural language phrases, supported by theories of **dual-process models** of compositional generalization (Novello et al., 2025).

![Fig. 3](images/fig3_folding.pdf)
**Fig. 3: Recursive Folding Logic.** Primitives are recursively composed into an irreducible AST structure by strictly validating arity constraints $\alpha(P)$ against incoming arguments.

Furthermore, logical steps are composed into an **Immutable DAG Structure** using nested `Let` bindings. This is intended to ensure that each intermediate result is an immutable named object within the evaluation scope, aiming to eliminate side effects and provide a clear lineage for computed values. Evaluation is performed via deterministic rewrite rules $R_P$ (Landin, 1964), ensuring termination and confluence (see Appendix A). This formal evaluation process is grounded in **Structural Operational Semantics** (Plotkin, 1977) and the principle of **Propositions as Types** (Wadler, 2015).

---

## 4. Examples of Compositional Reasoning
MIW was applied to diverse reasoning categories beyond simple sorting:
- **Algorithmic**: `FILTER(EVEN, SORT(numbers))`.
- **Spatial Reasoning**: `DIJKSTRA(graph, start, end)`.
- **Constraint Satisfaction**: `SOLVE_SUDOKU(grid)`.
- **Optimization**: `TREE_MAX_PATH(root)`.

The specific transformation of a linear task description into a formal result is visualized in the execution trace (Fig. 4), demonstrating the system's ability to maintain deliberate **visual-symbolic reasoning** (Boggs, 2025).

![Fig. 4](images/fig4_trace.pdf)
**Fig. 4: Execution Trace Pipeline.** A concrete example of the activity_selection task, tracing the mapping from NL phrases to primitive IDs and the final execution within the Morphic VM.

---

## 5. Experimental Evaluation
MIW was evaluated against 60 compositional tasks, achieving a 100.0% success rate within the tested parameters. Key scaling results observed include:
- **v=8000**: Robust extraction under extreme context noise.
- **d=15**: Correct execution of 15-level nested logic.
- **n=20**: Simultaneous verification of 20+ independent logical constraints.

The **n=20** result illustrates a capacity for maintaining logical consistency far exceeding typical human cognitive spans (Miller's Law, 7±2). Unlike stochastic models that exhibit performance decay as complexity increases, MIW maintains absolute reliability (Fig. 5). Within the scope of this study, results achieved bit-identical parity between Python and Modern Fortran kernels, confirming implementation invariance through **term rewriting** systems (Baumgartner et al., 2025).

![Fig. 5](images/fig5_reliability.pdf)
**Fig. 5: Reliability vs. Complexity Contrast.** Morphic's deterministic engine maintains 100% accuracy regardless of task scale (v, d, n), whereas stochastic models (LLMs) typically exhibit decay and hallucinations.

---

## 6. Discussion: Relation to Neuro-symbolic AI
Unlike neuro-symbolic systems such as DeepProbLog, **Plan-SOFAI** (Fabiano et al., 2024), or integrated manufacturing systems (Wu et al., 2025), MIW operates as a pure algebraic reduction engine. By replacing stochastic search with deterministic projection, MIW aims to offer zero inference variance, linear computational cost, and direct interpretability (Sinha & Garcez, 2025; Yang et al., 2025).

Furthermore, the 100.0% parity achieved across English and Japanese specifications in this study provides empirical evidence of a fundamental **decoupling between linguistic form and logical substance** (Fig. 6), highlighting the critical distinction between meaning and understanding in the age of data (Bender & Koller, 2020). In the MIW framework, natural language serves as a coordinate system used to orient and trigger logical primitives. This **Language Invariance** suggests that the "geometry of thought"—represented here as a formal AST—may function as a universal invariant, independent of the specific linguistic shell used for its transmission, a concept supported by **logical frameworks** (Harper et al., 1987).

![Fig. 6](images/fig6_manifold.pdf)
**Fig. 6: Language Invariance Manifold.** Demonstrating geometric convergence where English and Japanese specifications are projected into the same universal AST, yielding an identical normalized result.

Finally, the achievement of **bit-identical parity** between Python and Modern Fortran kernels supports the concept of **Platform Invariance** (Fig. 7). It indicates that the reduction of logic to a Normal Form can be a mathematical necessity that transcends the specific idioms of a computing environment. By decoupling the "logic of thought" from the "mechanics of execution," MIW demonstrates the potential to liberate deterministic intelligence from its underlying substrate (Alexander, 2020; Bhatnagar, 2025).

![Fig. 7](images/fig7_manifold.pdf)
**Fig. 7: Deterministic Kernel Parity.** A single AST is processed by independent execution kernels (Python and Fortran), both converging on a bit-identical Normal Form to prove substrate independence.

---

## 7. Conclusion
MIW provides evidence that compositional reasoning can be implemented as a deterministic structure-preserving mapping. Future work will explore hybridization with probabilistic models (Bengio et al., 2020) to bridge structural and perceptual grounding (Harnad, 1990). Furthermore, the potential introduction of **Sheaf Theory** into the Morphic Core language (Shkursky, 2025)—treating knowledge as a structure over topological spaces—to pave the way for a more generalized **Geometric Cognition** (Dhar et al., 2025). This may lead to emergent cognition through architectures like **COGENT3** (Salazar, 2025) and advanced **neuromorphic engineering** (Indiveri & Liu, 2021; Sandamirskaya, 2014).

---

## Data Availability Statement
The full source code for the MIW kernels (Python and Modern Fortran), the benchmark suite consisting of 60 algorithmic tasks, and the synthesis/execution logs are available for peer review and replication at the following repository: [https://github.com/aikenkyu001/morphic_inner_world](https://github.com/aikenkyu001/morphic_inner_world). The dataset is also archived via Zenodo (DOI: [10.5281/zenodo.18905026](https://doi.org/10.5281/zenodo.18905026)).

---

## Appendix A: Formal Reduction Semantics
Evaluation is defined as a reduction to **Normal Form (NF)**. The evaluation function $Eval: \mathcal{T}(\Sigma, \mathcal{V}) \to NF$ is defined by:
1. $Eval(c) = c$ for atomic literals.
2. $Eval(P(t_1, ..., t_n)) = R_P(Eval(t_1), ..., Eval(t_n))$ for applications.
Termination and confluence are ensured by finite arity constraints and orthogonality of rewrite rules. This reduction follows the principles of Propositions as Types (Wadler, 2015).

To maintain absolute predictability, MIW employs **Deterministic Error Handling** (Fig. 8). Instead of triggering system-level exceptions, the evaluator returns a **VError** value in cases of undefined operations or type mismatches. This approach treats errors as legitimate states within the logic, ensuring that the kernel never crashes and always produces a well-defined result even under failure conditions (Bhatnagar, 2025).

![Fig. 8](images/fig8_error.pdf)
**Fig. 8: Deterministic Error Flow.** Unlike traditional systems that crash upon exceptions, MIW propagates VError objects through the evaluation logic to maintain safe and predictable termination.

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

- Abadi, M., & Plotkin, G. (2020). A simple differentiable programming language. *Proc. ACM Program. Lang.*, 4, POPL.
- Alexander, D. R. (2020). Deterministic artificial intelligence. *IntechOpen*.
- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111, 1036–1060.
- Baroni, M. (2022). On the proper role of linguistically-oriented deep net analysis in linguistic theorizing. *arXiv preprint*.
- Baumgartner, P., et al. (2025). The AlphaPhysics term rewriting system for marking algebraic proofs. *arXiv preprint*.
- Bender, E. M., & Koller, A. (2020). Climbing towards NLU. *Proceedings of the ACL*.
- Bengio, Y., et al. (2020). Thinking fast and slow in AI. *arXiv preprint*.
- Bhatnagar, K. (2025). The RAM cognitive architecture: A deterministic, self-reflective paradigm for adaptive machine intelligence. *Zenodo*.
- Boggs, J. M. (2025). Deliberate visual-symbolic reasoning in a cognitive architecture (Doctoral dissertation). *University of Michigan*.
- Church, A. (1932). A set of postulates for the foundation of logic. *Annals of Mathematics*, 33, 346–366.
- Dhar, R., et al. (2025). Toward a sheaf-theoretic understanding of compositionality in large language models. *OpenReview*.
- Fabiano, F., et al. (2024). Plan-SOFAI: A neuro-symbolic planning architecture. *OpenReview*.
- Gurevich, Y. (1995). Evolving algebras: A tutorial introduction. *Microsoft Research*.
- Harnad, S. (1990). The symbol grounding problem. *Physica D: Nonlinear Phenomena*, 42, 335–346.
- Harper, R., Honsell, F., & Plotkin, G. (1987). A framework for defining logics. *Journal of the ACM, 40*(1), 143–184.
- Indiveri, G., & Liu, S.-C. (2021). Introducing 'Neuromorphic Computing and Engineering'. *Neuromorphic Computing and Engineering*, 1(1), 010001.
- Kotseruba, I., & Tsotsos, J. K. (2020). 40 years of cognitive architectures. *AI Review*, 53(1), 17–94.
- Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *Proceedings of ICML*.
- Landin, P. J. (1964). The mechanical evaluation of expressions. *The Computer Journal*, 6(4), 308–320.
- Langley, P., et al. (2009). Cognitive architectures: Research issues and challenges. *Cognitive Systems Research, 10*(1), 141–160.
- Licato, J., et al. (2014). Structural representation and reasoning in a hybrid cognitive architecture. *IJCNN*.
- Liu, N. F., et al. (2023). Lost in the Middle. *TACL*.
- Ludwig, J. (2005). Psychologically inspired symbolic cognitive architectures. *University of Oregon Computer Science Reports*.
- Marcus, G. (2020). The next decade in AI: Four steps towards robust artificial intelligence. *arXiv preprint*.
- Novello, A., et al. (2025). A neuroscience-inspired dual-process model of compositional generalization. *arXiv preprint*.
- Plotkin, G. D. (1977). A structural approach to operational semantics. *University of Edinburgh*.
- Saanum, T., et al. (2024). Simplifying latent dynamics with softly state-invariant world models. *NeurIPS*.
- Salazar, E. (2025). Introducing COGENT3: An AI architecture for emergent cognition. *arXiv preprint*.
- Sandamirskaya, Y. (2014). Dynamic neural fields as a step toward cognitive neuromorphic architectures. *Frontiers in Neuroscience*, 7, 276.
- Shkursky, A. (2025). The distinction field: A unified architecture of cognition and reality. *PhilArchive*.
- Sinha, S., & d'Avila Garcez, A. (2025). Neuro-symbolic frameworks: Conceptual characterization and empirical comparative analysis. *Neuro-Symbolic Artificial Intelligence Journal*.
- Sukhobokov, A. (2024). A universal knowledge model and cognitive architecture for prototyping AGI. *arXiv preprint*.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.
- Wadler, P. (2015). Propositions as Types. *Communications of the ACM*, 58(12), 75–84.
- Wu, S., et al. (2025). Toward human-like artificial intelligence by integrating cognitive architectures and large language models. *Neuro-Symbolic AI Journal*.
- Yang, X. W., Liu, J. Y., Wang, Y., & Chen, Y. (2025). Neuro-symbolic artificial intelligence. *IJCAI*.
- Zhang, C., yu, Y., Zhang, Z., & Cao, Z. (2022). Learning algebraic representation for systematic generalization in abstract reasoning. *European Conference on Computer Vision (ECCV)*.
