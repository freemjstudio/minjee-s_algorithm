def StringChallenge(strParam):
  str2num = {'zero':'0','one':'1','two':'2','three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7','eight':'8','nine':'9', 'plus':'+', 'minus':'-'}

  num2str = {'-':'negative','0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
  n = len(strParam)
  expr = ""
  left = 0 # last index
  for i in range(n):
    for j in range(i+1, n):
      if strParam[i:j] in str2num:
        expr += str2num[strParam[i:j]]
        left = j
        continue
  expr += str2num[strParam[left:]]
  result = str(eval(expr))

  answer = ""
  for i in result:
    answer += num2str[i]
  # code goes here
  return answer

# keep this function call here
print(StringChallenge(input()))