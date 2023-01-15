# Leetcode
# 981. Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.hashmap = {} # key=string, value=[[value1, timestamp1], [value2, timestamp 2]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap.keys():
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        """
        Run binary search on the timestamp values of the key.
        """
        if key in self.hashmap.keys():
            sorted_values = self.hashmap[key]
            left, right = 0, len(sorted_values)-1
            result = ""
            while left<=right:
                middle = left + (right-left)//2
                # print(self.hashmap)
                if sorted_values[middle][1] == timestamp:
                    return sorted_values[middle][0]
                elif sorted_values[middle][1] < timestamp:
                    # We want a lesser value, if exact match is not found, we update the result when a lesser value is found.
                    result = sorted_values[middle][0]
                    left = middle + 1
                else:
                    right = middle - 1
            return result
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)