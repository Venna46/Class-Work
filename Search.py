arr = [11,22,33,44,55,66,77,88,99] #11 will be index 0

key: int = 99
start: int = 0
end = len(arr)
n = len(arr)-1
found: bool= False

for i in arr:
    if arr[i] == key:
        print(f"found")
        break
    else:
      print(f"not found")

while start<= end:
    mid = (start + end) // 2
    if arr[mid] == key:
        print(f"Found element at pos:", mid)
        found = True
        break
    elif key < arr[mid]:
        end = mid-1
    elif key > arr[mid]:
        start = mid+1

if not found:
    print(f"{key} not found in the list")

    #implement using recursion