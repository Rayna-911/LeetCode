/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public ArrayList<Interval> merge(ArrayList<Interval> intervals) {
        ArrayList<Interval> res = new ArrayList<Interval>();
        
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a,Interval b){
                return a.start>b.start?1:(a.start==b.start?0:-1);}});
        
        if (intervals == null || intervals.size()<2){
            return intervals;
        }
        
        for(Interval inter : intervals){
            if (res.size()==0){
                res.add(inter);
            }
            else{
                if(res.get(res.size()-1).start<=inter.start && inter.start<=res.get(res.size()-1).end){
                    res.get(res.size()-1).end = Math.max(res.get(res.size()-1).end,inter.end);
                }
                else{
                    res.add(inter);
                }
            }
        }
        return res;
    }
}