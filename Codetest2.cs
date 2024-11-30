using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[,] quest) {
        //Console.WriteLine($"{quest[0,1]}");

        int quest_length = quest.GetLength(0);
        //Console.WriteLine(quest_length);
        int limit_time=0;
        int max_clear=0;
        List<int> ClearNumber = new List<int>();

        for (int x=0;x<quest_length;x++){
            limit_time+=quest[x,1];
        }

        //Console.WriteLine(limit_time);
        int get_exp = 0;
        for(int y=0;y<quest_length;y++){
            for(int x =0;x<quest_length;x++){
                int limit_exp = quest[x,0];
                int cur_exp = quest[x,1];
                if(get_exp<limit_exp){
                    if(!ClearNumber.Contains(x)){
                        ClearNumber.add(x);
                        get_exp+=cur_exp;
                        max_clear++;
                        }
                }

            }
        }
        Console.WriteLine(max_clear);






        int answer = 0;
        return answer;
    }
}