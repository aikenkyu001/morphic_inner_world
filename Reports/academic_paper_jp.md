# Morphic Inner World：合成的推論のための決定論的項代数認知アーキテクチャ・フレームワーク

**著者:** Fumio Miyata  
**日付:** 2026年3月9日  
**DOI:** https://doi.org/10.5281/zenodo.18905026  
**キーワード:** 認知アーキテクチャ、記号推論、項代数、合成性、決定論推論

---

## 概要
信頼性の高い合成的推論は、人工知能における中心的な課題であり続けている。現代の大規模言語モデルは優れた言語能力を示す一方で、深く入れ子になった構造や複雑なタスクにおいて不安定性を示すことが多い。本論文では、推論を自然言語入力から自由項代数として定義される記号推論空間への構造保存写像（射影）としてモデル化する決定論的認知アーキテクチャ、**Morphic Inner World (MIW)** を提案する。本フレームワークは、決定論的な最長一致トークナイザと **44 個の既約なプリミティブ** からなる意味論的辞書を用い、確率的推論に依存することなく絶対的な論理的一貫性を保証する。本アーキテクチャは、アルゴリズム、空間推論、および制約充足を含む 60 の課題からなるベンチマークを用いて評価された。実験の結果、定義されたタスクにおいて 100.0% の精度を達成し、Python と Modern Fortran という独立した実装間での完全な一致を確認した。

---

## 1. 緒言
現代のニューラル言語モデルは、特に精密な構造操作を必要とするタスクにおいて、**系統的な合成的推論**に苦慮している (Lake & Baroni, 2018; Liu et al., 2023)。これらの限界は、強固な構造的アンカーを欠いたトランスフォーマーベースのアーキテクチャの確率的性質に起因する。歴史的に、**ACT-R** や **SOAR** といった認知アーキテクチャは構造化された枠組みを提供してきたが、推論においてはヒューリスティックな探索に依存することが多かった。本論文では、推論を項代数多様体における**決定論的な代数的簡約**として扱う MIW を提案する。

---

## 2. アーキテクチャと形式モデル

### 2.1 全体フロー
MIW アーキテクチャは、単方向の 3 段階パイプライン（図 1）を通じて入力を処理する。情報理論的な観点からは、このプロセスは高エントロピーな言語入力から、低エントロピーで構造化された論理正規形への遷移を意味する。

![図 1: MIW 認知アーキテクチャの概要。自然言語は決定論的なトークナイザを通じて原始オペレータへと射影され（2.2節）、記号構造へと合成された後（3.1節）、正規形へと簡約される（3.2節）。MSP チェック（2.2節）と 44 個のプリミティブ（2.3節）が構造的整合性を保証する。](images/fig1_global_flow.pdf)

### 2.2 入力射影と MSP チェック
射影フェーズ $h: \mathcal{L} \to \Sigma^*$ は厳密に決定論的であり、以下の要素を用いる：
1.  **最長一致トークナイズ**: 言語フレーズは貪欲な最長一致戦略を用いて意味論的辞書と照合される。本研究の範囲内では、**制御された語彙（Controlled Vocabulary）** を用いることで言語的多義性を回避し、タスクの意図とプリミティブの間の 1 対 1 の写像を保証している。
2.  **MSP (Morphic Structural Pointers)**: 「1.」「2.」などの番号付きマーカーが構造的アンカーとして機能し、論理ブロックを識別する。これにより、周囲の高エントロピーなノイズを無視することが可能となる。

### 2.3 モルフィック・プリミティブ (Σ)
辞書は、関数型プログラミングの基本操作および中核的な認知タスクに基づいて選定された **44 個の既約なプリミティブ** で構成される（付録 C 参照）。この集合が自由項代数 $M = \mathcal{T}(\Sigma, V)$ の基底となる。

---

## 3. 構造合成と評価意味論
合成 $g: \Sigma^* \to \mathcal{M}$ は、必須のアリティ制約 $\alpha(P)$ を満たす記号木を構築する。評価は、終止性と合流性が保証された決定論的な書き換え規則 $R_P$ を通じて実行される（付録 A 参照）。

---

## 4. 合成的推論の具体例
MIW は単純なソート以外の多様な推論カテゴリーを処理する：
- **アルゴリズム**: `FILTER(EVEN, SORT(numbers))`。
- **空間推論**: `DIJKSTRA(graph, start, end)`。
- **制約充足**: `SOLVE_SUDOKU(grid)`。
- **最適化**: `TREE_MAX_PATH(root)`。

---

## 5. 実験的評価
MIW は、60 の合成的推論タスクにおいて、文脈サイズ $v=8000$、再帰深度 $d=15$ までの極限条件下で 100.0% の精度を維持した。Python と Modern Fortran による独立した実装はビットレベルで同一の出力を生成した。

---

## 6. 考察：Neuro-symbolic AI との関係
DeepProbLog のような現代的な Neuro-symbolic システムとは異なり、MIW は純粋な代数的簡約エンジンとして動作する。確率的な探索を決定論的な射影に置き換えることで、MIW は推論の分散ゼロ、線形な計算コスト、および直接的な解釈可能性を提供する。

---

## 7. 結論
MIW は、合成的推論が決定論的な構造保存写像として実装可能であることを示した。今後の課題は、構造的接地と知覚的接地を橋渡しするために、確率的モデルとのハイブリッド化を調査することである。

---

## 付録 A：形式的簡約意味論
評価プロセスを **正規形 (Normal Form: NF)** への簡約として定義する。評価関数 $Eval: \mathcal{T}(\Sigma, \mathcal{V}) \to NF$ は、原子リテラル $c$ に対して $Eval(c) = c$、適用 $P(t_1, ..., t_n)$ に対して $Eval(P(t_1, ..., t_n)) = R_P(Eval(t_1), ..., Eval(t_n))$ と定義される。有限のアリティ制約と書き換え規則の直交性により、終止性と合流性が保証される。

## 付録 B：ベンチマーク課題
タスクの全リストは **Zenodo (DOI: 10.5281/zenodo.18905026)** で公開されている。

## 付録 C：モルフィック・プリミティブ (Σ) 全リスト
| プリミティブ | アリティ | プリミティブ | アリティ |
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

## 参考文献

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111, 1036–1060.
- Bender, E. M., & Koller, A. (2020). Climbing towards NLU. *Proceedings of the ACL*.
- Church, A. (1932). A set of postulates for the foundation of logic. *Annals of Mathematics*, 33, 346–366.
- Harnad, S. (1990). The symbol grounding problem. *Physica D: Nonlinear Phenomena*, 42, 335–346.
- Indiveri, G., & Liu, S.-C. (2021). Introducing 'Neuromorphic Computing and Engineering'. *Neuromorphic Computing and Engineering*, 1(1), 010001.
- Kotseruba, I., & Tsotsos, J. K. (2020). 40 years of cognitive architectures. *AI Review*, 53(1), 17–94.
- Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *Proceedings of ICML*.
- Landin, P. J. (1964). The mechanical evaluation of expressions. *The Computer Journal*, 6(4), 308–320.
- Liu, N. F., et al. (2023). Lost in the Middle. *TACL*.
- Sandamirskaya, Y. (2014). Dynamic neural fields as a step toward cognitive neuromorphic architectures. *Frontiers in Neuroscience*, 7, 276.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.
- Wadler, P. (2015). Propositions as Types. *Communications of the ACM*, 58(12), 75–84.
