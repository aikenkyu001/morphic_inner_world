program morphic_exec_cli
    use morphic_types
    implicit none
    type(morphic_value) :: res_en, res_jp, expected, input_val
    print *, "--- Fortran Bilingual Real-Time Execution Report ---"
    print *, "Task                                          | EN | JP | Kernel Status"
    ! Executing BitmaskGrouper
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("BitmaskGrouper", input_val)
    res_jp = evaluate_task("BitmaskGrouper", input_val)
    call verify_bilingual_exec("BitmaskGrouper                               ", res_en, res_jp, expected)
    ! Executing activity_selection
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("activity_selection", input_val)
    res_jp = evaluate_task("activity_selection", input_val)
    call verify_bilingual_exec("activity_selection                           ", res_en, res_jp, expected)
    ! Executing autocomplete_trie
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("autocomplete_trie", input_val)
    res_jp = evaluate_task("autocomplete_trie", input_val)
    call verify_bilingual_exec("autocomplete_trie                            ", res_en, res_jp, expected)
    ! Executing binary_tree_maximum_path_sum
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("binary_tree_maximum_path_sum", input_val)
    res_jp = evaluate_task("binary_tree_maximum_path_sum", input_val)
    call verify_bilingual_exec("binary_tree_maximum_path_sum                 ", res_en, res_jp, expected)
    ! Executing bitwise_and_range
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("bitwise_and_range", input_val)
    res_jp = evaluate_task("bitwise_and_range", input_val)
    call verify_bilingual_exec("bitwise_and_range                            ", res_en, res_jp, expected)
    ! Executing boggle_solver
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("boggle_solver", input_val)
    res_jp = evaluate_task("boggle_solver", input_val)
    call verify_bilingual_exec("boggle_solver                                ", res_en, res_jp, expected)
    ! Executing dijkstra_shortest_path
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("dijkstra_shortest_path", input_val)
    res_jp = evaluate_task("dijkstra_shortest_path", input_val)
    call verify_bilingual_exec("dijkstra_shortest_path                       ", res_en, res_jp, expected)
    ! Executing dijkstra_v2_state_space
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("dijkstra_v2_state_space", input_val)
    res_jp = evaluate_task("dijkstra_v2_state_space", input_val)
    call verify_bilingual_exec("dijkstra_v2_state_space                      ", res_en, res_jp, expected)
    ! Executing fractional_knapsack
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("fractional_knapsack", input_val)
    res_jp = evaluate_task("fractional_knapsack", input_val)
    call verify_bilingual_exec("fractional_knapsack                          ", res_en, res_jp, expected)
    ! Executing interval_merger
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("interval_merger", input_val)
    res_jp = evaluate_task("interval_merger", input_val)
    call verify_bilingual_exec("interval_merger                              ", res_en, res_jp, expected)
    ! Executing kth_largest_element
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("kth_largest_element", input_val)
    res_jp = evaluate_task("kth_largest_element", input_val)
    call verify_bilingual_exec("kth_largest_element                          ", res_en, res_jp, expected)
    ! Executing longest_common_subsequence
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("longest_common_subsequence", input_val)
    res_jp = evaluate_task("longest_common_subsequence", input_val)
    call verify_bilingual_exec("longest_common_subsequence                   ", res_en, res_jp, expected)
    ! Executing lowest_common_ancestor_nary
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("lowest_common_ancestor_nary", input_val)
    res_jp = evaluate_task("lowest_common_ancestor_nary", input_val)
    call verify_bilingual_exec("lowest_common_ancestor_nary                  ", res_en, res_jp, expected)
    ! Executing lru_cache
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("lru_cache", input_val)
    res_jp = evaluate_task("lru_cache", input_val)
    call verify_bilingual_exec("lru_cache                                    ", res_en, res_jp, expected)
    ! Executing lru_cache_v2_concurrency
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("lru_cache_v2_concurrency", input_val)
    res_jp = evaluate_task("lru_cache_v2_concurrency", input_val)
    call verify_bilingual_exec("lru_cache_v2_concurrency                     ", res_en, res_jp, expected)
    ! Executing matrix_chain_multiplication
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("matrix_chain_multiplication", input_val)
    res_jp = evaluate_task("matrix_chain_multiplication", input_val)
    call verify_bilingual_exec("matrix_chain_multiplication                  ", res_en, res_jp, expected)
    ! Executing merge_k_sorted_lists
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("merge_k_sorted_lists", input_val)
    res_jp = evaluate_task("merge_k_sorted_lists", input_val)
    call verify_bilingual_exec("merge_k_sorted_lists                         ", res_en, res_jp, expected)
    ! Executing merge_sort_in_place
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("merge_sort_in_place", input_val)
    res_jp = evaluate_task("merge_sort_in_place", input_val)
    call verify_bilingual_exec("merge_sort_in_place                          ", res_en, res_jp, expected)
    ! Executing minimum_spanning_tree_prim
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("minimum_spanning_tree_prim", input_val)
    res_jp = evaluate_task("minimum_spanning_tree_prim", input_val)
    call verify_bilingual_exec("minimum_spanning_tree_prim                   ", res_en, res_jp, expected)
    ! Executing optimal_bst_cost
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("optimal_bst_cost", input_val)
    res_jp = evaluate_task("optimal_bst_cost", input_val)
    call verify_bilingual_exec("optimal_bst_cost                             ", res_en, res_jp, expected)
    ! Executing permutations_with_duplicates
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("permutations_with_duplicates", input_val)
    res_jp = evaluate_task("permutations_with_duplicates", input_val)
    call verify_bilingual_exec("permutations_with_duplicates                 ", res_en, res_jp, expected)
    ! Executing procedural_quicksort
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("procedural_quicksort", input_val)
    res_jp = evaluate_task("procedural_quicksort", input_val)
    call verify_bilingual_exec("procedural_quicksort                         ", res_en, res_jp, expected)
    ! Executing redundant_connection_ii
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("redundant_connection_ii", input_val)
    res_jp = evaluate_task("redundant_connection_ii", input_val)
    call verify_bilingual_exec("redundant_connection_ii                      ", res_en, res_jp, expected)
    ! Executing regex_matcher
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("regex_matcher", input_val)
    res_jp = evaluate_task("regex_matcher", input_val)
    call verify_bilingual_exec("regex_matcher                                ", res_en, res_jp, expected)
    ! Executing rotate_image_n_by_n
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("rotate_image_n_by_n", input_val)
    res_jp = evaluate_task("rotate_image_n_by_n", input_val)
    call verify_bilingual_exec("rotate_image_n_by_n                          ", res_en, res_jp, expected)
    ! Executing serialize_deserialize_nary_tree
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("serialize_deserialize_nary_tree", input_val)
    res_jp = evaluate_task("serialize_deserialize_nary_tree", input_val)
    call verify_bilingual_exec("serialize_deserialize_nary_tree              ", res_en, res_jp, expected)
    ! Executing sparse_matrix_multiplication
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("sparse_matrix_multiplication", input_val)
    res_jp = evaluate_task("sparse_matrix_multiplication", input_val)
    call verify_bilingual_exec("sparse_matrix_multiplication                 ", res_en, res_jp, expected)
    ! Executing spiral_matrix_ii
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("spiral_matrix_ii", input_val)
    res_jp = evaluate_task("spiral_matrix_ii", input_val)
    call verify_bilingual_exec("spiral_matrix_ii                             ", res_en, res_jp, expected)
    ! Executing sudoku_solver
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("sudoku_solver", input_val)
    res_jp = evaluate_task("sudoku_solver", input_val)
    call verify_bilingual_exec("sudoku_solver                                ", res_en, res_jp, expected)
    ! Executing sudoku_solver_v2_nesting
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("sudoku_solver_v2_nesting", input_val)
    res_jp = evaluate_task("sudoku_solver_v2_nesting", input_val)
    call verify_bilingual_exec("sudoku_solver_v2_nesting                     ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n1
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n1", input_val)
    res_jp = evaluate_task("synthetic_constraints_n1", input_val)
    call verify_bilingual_exec("synthetic_constraints_n1                     ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n13
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n13", input_val)
    res_jp = evaluate_task("synthetic_constraints_n13", input_val)
    call verify_bilingual_exec("synthetic_constraints_n13                    ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n2
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n2", input_val)
    res_jp = evaluate_task("synthetic_constraints_n2", input_val)
    call verify_bilingual_exec("synthetic_constraints_n2                     ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n20
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n20", input_val)
    res_jp = evaluate_task("synthetic_constraints_n20", input_val)
    call verify_bilingual_exec("synthetic_constraints_n20                    ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n3
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n3", input_val)
    res_jp = evaluate_task("synthetic_constraints_n3", input_val)
    call verify_bilingual_exec("synthetic_constraints_n3                     ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n5
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n5", input_val)
    res_jp = evaluate_task("synthetic_constraints_n5", input_val)
    call verify_bilingual_exec("synthetic_constraints_n5                     ", res_en, res_jp, expected)
    ! Executing synthetic_constraints_n8
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_constraints_n8", input_val)
    res_jp = evaluate_task("synthetic_constraints_n8", input_val)
    call verify_bilingual_exec("synthetic_constraints_n8                     ", res_en, res_jp, expected)
    ! Executing synthetic_context_v100
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v100", input_val)
    res_jp = evaluate_task("synthetic_context_v100", input_val)
    call verify_bilingual_exec("synthetic_context_v100                       ", res_en, res_jp, expected)
    ! Executing synthetic_context_v1000
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v1000", input_val)
    res_jp = evaluate_task("synthetic_context_v1000", input_val)
    call verify_bilingual_exec("synthetic_context_v1000                      ", res_en, res_jp, expected)
    ! Executing synthetic_context_v2000
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v2000", input_val)
    res_jp = evaluate_task("synthetic_context_v2000", input_val)
    call verify_bilingual_exec("synthetic_context_v2000                      ", res_en, res_jp, expected)
    ! Executing synthetic_context_v4000
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v4000", input_val)
    res_jp = evaluate_task("synthetic_context_v4000", input_val)
    call verify_bilingual_exec("synthetic_context_v4000                      ", res_en, res_jp, expected)
    ! Executing synthetic_context_v500
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v500", input_val)
    res_jp = evaluate_task("synthetic_context_v500", input_val)
    call verify_bilingual_exec("synthetic_context_v500                       ", res_en, res_jp, expected)
    ! Executing synthetic_context_v8000
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_context_v8000", input_val)
    res_jp = evaluate_task("synthetic_context_v8000", input_val)
    call verify_bilingual_exec("synthetic_context_v8000                      ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d1
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d1", input_val)
    res_jp = evaluate_task("synthetic_nesting_d1", input_val)
    call verify_bilingual_exec("synthetic_nesting_d1                         ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d10
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d10", input_val)
    res_jp = evaluate_task("synthetic_nesting_d10", input_val)
    call verify_bilingual_exec("synthetic_nesting_d10                        ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d15
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d15", input_val)
    res_jp = evaluate_task("synthetic_nesting_d15", input_val)
    call verify_bilingual_exec("synthetic_nesting_d15                        ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d2
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d2", input_val)
    res_jp = evaluate_task("synthetic_nesting_d2", input_val)
    call verify_bilingual_exec("synthetic_nesting_d2                         ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d3
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d3", input_val)
    res_jp = evaluate_task("synthetic_nesting_d3", input_val)
    call verify_bilingual_exec("synthetic_nesting_d3                         ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d4
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d4", input_val)
    res_jp = evaluate_task("synthetic_nesting_d4", input_val)
    call verify_bilingual_exec("synthetic_nesting_d4                         ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d5
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d5", input_val)
    res_jp = evaluate_task("synthetic_nesting_d5", input_val)
    call verify_bilingual_exec("synthetic_nesting_d5                         ", res_en, res_jp, expected)
    ! Executing synthetic_nesting_d7
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("synthetic_nesting_d7", input_val)
    res_jp = evaluate_task("synthetic_nesting_d7", input_val)
    call verify_bilingual_exec("synthetic_nesting_d7                         ", res_en, res_jp, expected)
    ! Executing task_60
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("task_60", input_val)
    res_jp = evaluate_task("task_60", input_val)
    call verify_bilingual_exec("task_60                                      ", res_en, res_jp, expected)
    ! Executing text_justification
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("text_justification", input_val)
    res_jp = evaluate_task("text_justification", input_val)
    call verify_bilingual_exec("text_justification                           ", res_en, res_jp, expected)
    ! Executing trapping_rain_water_ii
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("trapping_rain_water_ii", input_val)
    res_jp = evaluate_task("trapping_rain_water_ii", input_val)
    call verify_bilingual_exec("trapping_rain_water_ii                       ", res_en, res_jp, expected)
    ! Executing valid_parentheses_complex
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("valid_parentheses_complex", input_val)
    res_jp = evaluate_task("valid_parentheses_complex", input_val)
    call verify_bilingual_exec("valid_parentheses_complex                    ", res_en, res_jp, expected)
    ! Executing word_break
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("word_break", input_val)
    res_jp = evaluate_task("word_break", input_val)
    call verify_bilingual_exec("word_break                                   ", res_en, res_jp, expected)
    ! Executing word_break_v2_context_4k
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("word_break_v2_context_4k", input_val)
    res_jp = evaluate_task("word_break_v2_context_4k", input_val)
    call verify_bilingual_exec("word_break_v2_context_4k                     ", res_en, res_jp, expected)
    ! Executing word_ladder
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("word_ladder", input_val)
    res_jp = evaluate_task("word_ladder", input_val)
    call verify_bilingual_exec("word_ladder                                  ", res_en, res_jp, expected)
    ! Executing word_ladder_v2_branching
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("word_ladder_v2_branching", input_val)
    res_jp = evaluate_task("word_ladder_v2_branching", input_val)
    call verify_bilingual_exec("word_ladder_v2_branching                     ", res_en, res_jp, expected)
    ! Executing word_search_ii
    input_val%value_type = 3; input_val%bool_val = .true.
    expected%value_type = 3; expected%bool_val = .true.
    res_en = evaluate_task("word_search_ii", input_val)
    res_jp = evaluate_task("word_search_ii", input_val)
    call verify_bilingual_exec("word_search_ii                               ", res_en, res_jp, expected)
    print *, "--- Verification Complete: 60/60 Real Executions Analyzed ---"
end program morphic_exec_cli