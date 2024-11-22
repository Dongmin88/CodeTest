using System;




public class Solution {
    public int diffIntMax(int[] diffs){
        int max = int.MinValue;
        foreach (int num in diffs){
            if(num>=max){
                max=num;
            }
        }
        return max; 
    }
    
    public int diffIntMin(int[] diffs){
        int min = int.MaxValue;
        foreach (int num in diffs){
            if(num<=min){
                min=num;
            }
        }
        return min; 
    }

    public int solution(int[] diffs, int[] times, long limit) {
        int Maxlevel=diffIntMax(diffs);
        int Minlevel=diffIntMin(diffs);
        int beforelevel = 0;
        int Midlevel=(Maxlevel+Minlevel)/2;
        Console.WriteLine(Midlevel);
        long spend_times =0;
        while(true){
            for(int x =0;x<diffs.Length;x++)
            {

                if(x==0)
                {
                    if(diffs[x]<=Midlevel){
                        spend_times=times[x];
                    }
                    else{
                        spend_times=(diffs[x]-Midlevel)*(times[x]);
                    }
 
                }
                else
                {
                    if(diffs[x]<=Midlevel){
                        spend_times=spend_times+(times[x]);
                    }
                    else{
                        spend_times=spend_times+((diffs[x]-Midlevel)*(times[x-1]+times[x])+times[x]);
                    }
                }

            }
            if(spend_times>limit)
            {
                spend_times=0;
                int nextlevel=0;
                nextlevel=(Midlevel+Maxlevel)/2;
                
                if(Midlevel==Minlevel){
                    Midlevel=nextlevel+1;
                    break;
                }
                
                Minlevel=Midlevel;
                Midlevel=nextlevel;
                Console.WriteLine($"{Minlevel} {Midlevel} {Maxlevel}");
                continue;
            }
            else
            {
                spend_times=0;
                int nextlevel=0;
                
                nextlevel=(Midlevel+Minlevel)/2;



                if(Midlevel==Maxlevel){
                    Midlevel=nextlevel;
                    break;
                }
                Maxlevel=Midlevel;
                Midlevel=nextlevel;
                Console.WriteLine($"{Minlevel} {Midlevel} {Maxlevel}");
                continue;
            }
            
        }
        Console.WriteLine(Midlevel);
        return Midlevel;
    }
}