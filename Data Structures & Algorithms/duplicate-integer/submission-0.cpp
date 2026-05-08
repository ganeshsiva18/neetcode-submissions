#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> numsets;
        for (int i = 0; i<nums.size(); i++){
            if (numsets.contains(nums[i])){
                return true;
            } else{
                numsets.insert(nums[i]);
            }
        }
        return false;
    }
};