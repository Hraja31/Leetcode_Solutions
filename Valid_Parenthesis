class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        const char* ptr = s.c_str();;
        while (*ptr != NULL)
        {
            if (*ptr == '(' || *ptr == '{' || *ptr == '[')
                st.push(*ptr);
            else{
                if(st.empty())
                    return false;
                if(*ptr == ')'){
                    if(st.top() == '(')
                        st.pop();
                    else return false;
                }
                else if(*ptr == '}'){
                    if(st.top() == '{')
                        st.pop();
                    else return false;
                }
                else if(*ptr == ']'){
                    if(st.top() == '[')
                        st.pop();
                    else return false;
                }
            }
            ptr++;
        }
        if (st.empty())
            return true;
        return false;
    }
};
