# Backtracking
## Recommended Order for Review
* 10 Regular Expression Matching
* 17 Letter Combinations of a Phone Number
* 22 Generate Parentheses
* 39 Combination Sum
* 40 Combination Sum II
* 46 Permutations
* 93 Restore IP Addresses
* 79 Word Search
* 212 Word Search II
* 37 Sudoku Solver
* 127 Word Ladder
* 126 Word Ladder II
* 49 Group Anagrams
* 78 Subsets
* 131 Palindrome Partitioning

## Resources
1. https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=583166&highlight=backtracking
2. https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=589136&highlight=backtracking

**Template**
* https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
```java
public List<List<Integer>> someProblem(int[] nums) {
    List<List<Integer>> out = new ArrayList<>();
    // May need to sort input
    // Arrays.sort(nums);
    backtrack(out, new ArrayList<>(), nums, 0);
    return out;
}

private void backtrack(List<List<Integer>> out , List<Integer> tempList, int [] nums, int start){
    // Must create a new clone for output since old reference keeps changing
    list.add(new ArrayList<>(tempList));
    for(int i = start; i < nums.length; i++){
        tempList.add(nums[i]);
        backtrack(out, tempList, nums, i + 1);
        // Reverse the tempList to its original form for next iteration
        tempList.remove(tempList.size() - 1);
    }
}
```
