public int[] twoSum(int[] nums, int target) {
    Arrays.sort(nums);

    int slow = 0;
    int fast = nums.length - 1;

    while (slow < fast) {
        int total = nums[slow] + nums[fast];
        if (total == target) {
            int[] out = {slow, fast};
            return out;
        }

        else if (total < target)
            slow++;
        else
            fast--;
    }
    return null;
}
