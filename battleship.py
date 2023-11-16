def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  compiledList = []
  
  for lst in G:
    compiledList.extend(lst)
    
  hitCount = 0
    
  for num in compiledList:
    if num == 1:
      hitCount += 1
  
  total = R * C
  return hitCount/total
