class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a=[]
        a.append(celsius+273.15)
        a.append(celsius*1.8+32.00)
        return a