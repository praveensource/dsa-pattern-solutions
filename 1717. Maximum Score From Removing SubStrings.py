class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        # function to remove pairs 
        def remove_pairs(s,first,second,score):
            stack = []
            points = 0
            for ch in s:
                #checking if the top of stack is according to our assumption
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    points += score
                else:
                    stack.append(ch)
            return "".join(stack),points

        # removal
        # to gain maximum points we need to use which parameter gives us maximum value
        # basically more value then gives more output
        if x >= y:
            # first removing all the ab substring so that we get maximum points
            s,gain1 = remove_pairs(s,"a","b",x)
            # removing ba if exists so that we can maximize our points.
            # this is only if it exists
            _,gain2 = remove_pairs(s,"b","a",y)

        else:
            #if given y is greater we remove ba substring from the string and gain points
            s,gain1 = remove_pairs(s,"b","a",y)
            # using this just if in case we have ab substring so that if we have we can maximize our points or gains.
            _,gain2 = remove_pairs(s,"a","b",x)
        return gain1 + gain2
        


