def normalize(path):
  stack = []
  array = path.split('/')
  result = ""
  if path[0] == '/':
    result += '/'
  for i in range(len(array)):
    if array[i] == '':
      continue
    if array[i] == '..':
      if len(stack) > 0 and stack[-1] != '..':
        stack.pop()
      else:
        stack.append(array[i])
    elif array[i] != '.':
      stack.append(array[i])

  temp = "/".join(stack)
  result += temp
  return result

def assertEquals(expected, actual):
  assert expected == actual, f'{expected} != {actual}'


# os.path.normpath()

assertEquals("a/b/c/d", normalize("a/b/./c/d"))
assertEquals("a/b/c/d", normalize("a/b//c/d"))

assertEquals("/home/david/work", normalize("/home/user/../david/work"))
assertEquals("/home/user/.m2/cache", normalize("/home/user/.m2/cache"))
assertEquals("/home/user/.m2/cache", normalize("/home/user//.m2///cache//"))

assertEquals("/home/user/.cache./13../57../90", normalize("/home/user/.cache./13../57../90"))
assertEquals("/home/david/57/90", normalize("/home/user/.cache./13../../../24.././../../david/57/90"))

assertEquals("/home/ubuntu", normalize("/tmp/../home/./ubuntu"))
assertEquals("/tmp", normalize("/tmp/v/a/../.."))
# assertEquals("/tmp", normalize("/tmp/v/a/../../../../../tmp"))



assertEquals("a/b/c/d", normalize("a/b/c/d"))
assertEquals("/home/ubuntu/homework", normalize("/home/ubuntu/./homework"))
assertEquals("/home/homework", normalize("/home/ubuntu/../homework"))
assertEquals("/home/ubuntu/homework", normalize("/home/ubuntu/homework"))
assertEquals("a/b/c/d", normalize("a///b////c/d"))

assertEquals("/home", normalize("/home/ubuntu/homework/../.."))
assertEquals("a/b/c/d", normalize("./a/b/c/d"))
assertEquals("/a/b/c", normalize("/./a/b/c"))

assertEquals("..", normalize(".."))
assertEquals("../..", normalize("../.."))
assertEquals("../../..", normalize("../../.."))

assertEquals("../../../d", normalize("../../../d"))
assertEquals("../a.txt", normalize("../a.txt"))
assertEquals("../d", normalize("a/b/../c/../../../d"))
assertEquals("../../d", normalize("a/b/../c/../../../../d"))

assertEquals("../a.txt", normalize("./../a.txt"))
assertEquals("a", normalize("./a"))
assertEquals("..", normalize(".."))
assertEquals("../../..", normalize("../../.."))
assertEquals("../../../..", normalize("../../../.."))
assertEquals("../../../..", normalize(".././.././../../."))
assertEquals("../b.txt", normalize("../c/d/../../b.txt"))

print("done-----")
