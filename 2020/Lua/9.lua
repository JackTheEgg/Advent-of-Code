local nums = {}
for line in io.lines("9.txt") do
  table.insert(nums, tonumber(line))
end

local pre, badNum = 25, 0
for i = pre + 1, #nums do
  local good = false
  for j = i - pre, i - 1 do
    for k = i - pre + 1, i - 1 do
      if nums[j] + nums[k] == nums[i] then good = true break end
    end
  end
  if not good then badNum = nums[i] break end
end
print(badNum)

for i = 1, #nums do
  local set, count, found = {nums[i]}, nums[i], false
  for j = i + 1, #nums do
    count = count + nums[j]
    table.insert(set, nums[j])
    if count == badNum then table.sort(set) print(set[1] + set[#set]) found = true break
    elseif count > badNum then break end
  end
  if found then break end
end
