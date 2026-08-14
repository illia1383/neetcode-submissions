class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0

        for i in range(len(details)):
            print(int(details[i][-4: -2]))
            if int(details[i][-4: -2]) > 60:
                #print(int(details[i][3: 5]))
                counter += 1
        return counter