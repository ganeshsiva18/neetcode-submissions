class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> stringmap;
        for (string s : strs){
            vector<int> count(26, 0);
            for (char c : s){
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for (int n : count){
                key += ',' + to_string(n);
            }
            stringmap[key].push_back(s);
        }
        vector<vector<string>> strsfin;
        for (const auto& [key, val] : stringmap){
            strsfin.push_back(val);
        }
        return strsfin;
    }
};
