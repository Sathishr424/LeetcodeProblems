// Last updated: 12/6/2025, 5:55:29 am
class Solution {
public:
    int maxArea(vector<int>& height) {
        unsigned int ret = 0;
        //unsigned int tmp;
        for (unsigned int i=0; i<height.size()-1; i++){
            for (unsigned int j=i+1; j<height.size(); j++){
                unsigned tmp = height[i];
                if (height[i] > height[j]) tmp = height[j];
                if (tmp * ((j+1)-(i+1)) > ret){
                    ret = tmp * ((j+1)-(i+1));
                }
            }
        }return ret;
    }
};