class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros,ones,zeroones,onezeros,output=0,0,0,0,0
        for c in s:
            if c=='1':
                output+=onezeros
                zeroones+=zeros
                ones+=1
            if c=='0':
                output+=zeroones
                onezeros+=ones
                zeros+=1
        return output
        