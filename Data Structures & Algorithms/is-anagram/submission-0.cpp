class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> scharmap;
        for (char c : s){
            if (!scharmap.contains(c)){
                scharmap[c] = 1;
            } else{
                scharmap[c]++;
            }
        }
        std::unordered_map<char, int> tcharmap;
        for (char c : t){
            if (!tcharmap.contains(c)){
                tcharmap[c] = 1;
            } else{
                tcharmap[c]++;
            }
        }
        if (tcharmap == scharmap){
            return true;
        }
        return false;
    }
};
