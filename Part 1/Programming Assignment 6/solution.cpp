#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int main(){
    ifstream file("algo1-programming_prob-2sum.txt");
    // file.open();
    //file.open("")
    string line;
    vector<int> nums;
    long int x;
    while(getline(file, line)){
        //istringstream strstream(line);
        nums.push_back(stoi(line));
        //cout << x;
    }
    unordered_map<int, int> freqdict;
    for(const int &n:nums){
        if(freqdict.find(n)==freqdict.end()){
            freqdict[n] = 0;
        }
        freqdict[n] += 1;
    }
    cout <<  freqdict.size();
    string fuck;
    cin >> fuck;
    int count = 0;
    for(int t=-10000; t <= 10000; t++){
        cout << t << endl;
        for(auto it=freqdict.begin(); it!=freqdict.end(); ++it){
            
            x = t - it->first;
            if(x==it->first){
                if(it->second >= 2){
                    count ++;
                    break;
                }
            }else{
                if(freqdict.find(x)!=freqdict.end()){
                    count ++;
                    break;
                }
            }
        }
    }
    cout << "Number of fricking integers: " << count;
}