class Solution {
    public int maxSubArray(int[] nums) {
        // if(nums[0]<0 && nums[nums.length-1]<0){
        //     return  ;
        // }
        int max_output = Integer.MIN_VALUE;
        int curr_output= 0;
        for(int i=0; i<=nums.length-1; i++){
          if (curr_output < 0){
            curr_output = nums[i];
        } 
        else{
            curr_output += nums[i];
        }
        if(max_output<curr_output)  
        {
            max_output = curr_output;
        }
            
        }
        return max_output;
        }
}