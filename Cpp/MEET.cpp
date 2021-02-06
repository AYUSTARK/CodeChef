#include<bits/stdc++.h>
#include<string>
#include<vector>
using namespace std;
int main() {
    int t;
    cin >> t;
    fflush(stdin);
    while (t--) {
        string str;
        string hr, min, hr_p, min_p, ampmcheck;
        getline(cin, str);
        fflush(stdin);
        //cout << str << endl;
        hr += str[0];
        hr += str[1];
        min += str[3];
        min += str[4];
        ampmcheck += str[6];
        ampmcheck += str[7];
        hr_p = hr;
        min_p = min;
        int hour = atoi(hr_p.c_str());
        int minute = atoi(min_p.c_str());
        if (hour != 12 and ampmcheck == "PM") {
            hour = hour + 12;
        } else if (hour == 12 and ampmcheck == "AM") {
            hour = 0;
        }
        int officetimehour = hour;
        int officetimeminute = minute;
        int final_office_time = officetimehour * 100 + officetimeminute;
        //cout<<officetimehour<<" "<<officetimeminute<<endl;
        int n;
        cin >> n;
        fflush(stdin);
        vector<int> ot(0);
        for (int i = 1; i <= n; i++) {
            string str1;
            string hr1, hr2, min1, min2, hr_l, hr_r, min_l, min_r, ampmcheck_l, ampmcheck_r;
            getline(cin, str1);
            fflush(stdin);
            hr1 += str1[0];
            hr1 += str1[1];
            min1 += str1[3];
            min1 += str1[4];
            ampmcheck_l += str1[6];
            ampmcheck_l += str1[7];
            hr_l = hr1;
            min_l = min1;
            int hour_l = atoi(hr_l.c_str());
            int minute_l = atoi(min_l.c_str());
            if (hour_l != 12 and ampmcheck_l == "PM") {
                hour_l = hour_l + 12;
            } else if (hour_l == 12 and ampmcheck_l == "AM") {
                hour_l = 0;
            }
            int employee_start_hour = hour_l;
            int employee_start_minute = minute_l;
            //cout<<"EMPLOYEE START TIME"<<employee_start_hour<<" "<<employee_start_minute<<endl;
            int employee_final_start_time = (employee_start_hour * 100) + employee_start_minute;
            hr2 += str1[9];
            hr2 += str1[10];
            min2 += str1[12];
            min2 += str1[13];
            ampmcheck_r += str1[15];
            ampmcheck_r += str1[16];
            hr_r = hr2;
            min_r = min2;
            int hour_r = atoi(hr_r.c_str());
            int minute_r = atoi(min_r.c_str());
            if (hour_r != 12 and ampmcheck_r == "PM") {
                hour_r = hour_r + 12;
            } else if (hour_r == 12 and ampmcheck_r == "AM") {
                hour_r = 0;
            }
            int employee_end_hour = hour_r;
            int employee_end_minute = minute_r;
            int employee_final_end_time = employee_end_hour * 100 + employee_end_minute;
            cout << final_office_time << " " << employee_final_start_time << " " << employee_final_end_time << endl;
            /*if (final_office_time >= employee_final_start_time && final_office_time <= employee_final_end_time) {
                ot.push_back(1);
            } else {
                ot.push_back(0);
            }
        }
        for (auto itr:ot) {
            cout << itr;
        }*/
            cout << endl;
        }
    }
}