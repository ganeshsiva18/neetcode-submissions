class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr = {-1, -1};
        int comp;
        std::unordered_map<int, int> intmap;
        for (int i = 0; i < nums.size(); i++){
            comp = target-nums[i];
            if (intmap.contains(comp)){
                arr[0] = intmap[comp];
                arr[1] = i;
                return arr;
            } else {
                intmap[nums[i]] = i;
            }
        }
        return arr;
    }
};
