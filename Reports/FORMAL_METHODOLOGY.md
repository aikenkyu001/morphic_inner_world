# Formal Methodology: Morphic Inner World

## 1. Morphic Primitives and Arity (Σ)
Each linguistic phrase is grounded in a deterministic primitive with a fixed arity (α).

| Primitive | Arity | Description | Grounded Phrase (EN) | Grounded Phrase (JP) |
| :--- | :---: | :--- | :--- | :--- |
| sort_by_end | 1 | Grounding for sort_by_end | sort by end time | 終了時間ソート |
| filter_overlapping | 1 | Grounding for filter_overlapping | select non-overlapping | 重複排除選択 |
| length | 1 | Grounding for length | count elements | 要素数カウント |
| solve_sudoku | 1 | Grounding for solve_sudoku | solve sudoku | 数独解決 |
| word_break | 2 | Grounding for word_break | check word break | 単語分割判定 |
| dijkstra | 3 | Grounding for dijkstra | calculate shortest path | 最短経路計算 |
| rotate_matrix | 1 | Grounding for rotate_matrix | rotate matrix | 行列回転 |
| tree_max_path | 1 | Grounding for tree_max_path | calculate tree path | 最大パス合計 |
| bitwise_range_and | 2 | Grounding for bitwise_range_and | calculate bitwise range | ビットAND範囲 |
| boggle_solve | 2 | Grounding for boggle_solve | solve boggle | ボングルパズル |
| fractional_knapsack | 2 | Grounding for fractional_knapsack | calculate knapsack | 分納ナップサック |
| merge_intervals | 1 | Grounding for merge_intervals | merge intervals | インターバルマージ |
| kth_largest | 2 | Grounding for kth_largest | find kth largest | k番目最大要素 |
| lcs | 2 | Grounding for lcs | calculate lcs | 最長共通部分列 |
| lru_cache_op | 2 | Grounding for lru_cache_op | simulate cache | キャッシュ操作 |
| merge_k_lists | 1 | Grounding for merge_k_lists | merge k lists | ソート済みマージ |
| is_valid_parentheses | 1 | Grounding for is_valid_parentheses | validate parentheses | 括弧正当性判定 |
| autocomplete_trie | 2 | Grounding for autocomplete_trie | trie autocomplete | オートコンプリート |
| bitmask_group | 1 | Grounding for bitmask_group | bitmask group | ビットマスクグループ |
| matrix_chain | 1 | Grounding for matrix_chain | matrix chain cost | 行列連鎖コスト |
| optimal_bst | 1 | Grounding for optimal_bst | optimal bst cost | 最適探索木コスト |
| regex_match | 2 | Grounding for regex_match | regex match | 正規表現マッチ |
| word_ladder_bfs | 3 | Grounding for word_ladder_bfs | ladder length | ラダー最短距離 |
| mst_prim | 2 | Grounding for mst_prim | minimum spanning tree | 最小全域木計算 |
| redundant_conn | 1 | Grounding for redundant_conn | redundant connection | 冗長接続特定 |
| sparse_mul | 2 | Grounding for sparse_mul | sparse multiplication | スパース行列乗算 |
| spiral_gen | 1 | Grounding for spiral_gen | generate spiral | 渦巻き行列生成 |
| rain_3d | 1 | Grounding for rain_3d | 3d rain water | 3D雨水計算 |
| text_justify | 2 | Grounding for text_justify | justify text | テキスト均等付 |
| word_search_2 | 2 | Grounding for word_search_2 | search grid words | グリッド単語検索 |
| permute_dup | 1 | Grounding for permute_dup | unique permutations | 重複順列生成 |
| quicksort | 1 | Grounding for quicksort | perform quicksort | クイックソート |
| mergesort | 1 | Grounding for mergesort | perform mergesort | マージソート |
| lca_nary | 3 | Grounding for lca_nary | find lowest ancestor | 共通祖先検索 |
| serialize_tree | 1 | Grounding for serialize_tree | serialize tree | 木直列化 |
| deserialize_tree | 1 | Grounding for deserialize_tree | deserialize tree | 木構造復元 |
| ladder_all | 3 | Grounding for ladder_all | find all ladders | ラダー全経路 |
| identity | 1 | Grounding for identity | identity transform | 恒等変換 |
| lru_cache_concurrent | 2 | Grounding for lru_cache_concurrent | concurrent cache | 並行キャッシュ操作 |
| reconstruct_list | 1 | Grounding for reconstruct_list | reconstruct list | 連結リスト構成 |
| check_constraints | 1 | Grounding for check_constraints | check constraints | 制約判定 |
| process_context | 2 | Grounding for process_context | process context | コンテキスト処理 |
| flatten_nesting | 1 | Grounding for flatten_nesting | flatten nesting | 構造平坦化 |
| composite_task_60 | 2 | Grounding for composite_task_60 | ultimate dynamic logic synthesis | 究極の動的論理合成 |

## 2. Tokenization and AST Synthesis Algorithm
### Algorithm 1: Longest-Match Tokenization
1. Sort all phrases in the Semantic Dictionary by length in descending order.
2. Iterate through the input string, matching the longest available phrase first to avoid ambiguity.
3. Map matched phrases to their corresponding Morphic Primitives.

### Algorithm 2: Arity-based Recursive Folding
The synthesized AST is built by folding the sequence of primitives , P_2, ..., P_n$ with input variables , V_2, ...$.
The folding process ensures that for each $, its required $lpha(P_i)$ arguments are filled from the current evaluation stack or the input variables.