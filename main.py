class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_index = bisect_right(letters,target) ## if the target already exists bisect_right ensures that the new value will be insterted to the most right
        return letters[target_index] if target_index<len(letters)  else letters[0]
    #    low = 0
    #    high = len(letters) - 1

    #    while low <= high:
    #         mid = (low+high)>>1
    #         guess = letters[mid]
    #         if guess == target:
    #             return letters[mid + 1]
    #         elif guess > target:
    #             high = mid -1
    #         else:
    #             low = mid + 1
    #    return letters[0]         

                    
