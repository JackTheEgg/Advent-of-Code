local nums = {}
for line in io.lines("1.txt") do
  table.insert(nums, tonumber(line))
end

for i = 1, #nums do
  for j = 2, #nums do
    if nums[i] + nums[j] == 2020 then
      print(nums[i] * nums[j])
    end
    for k = 3, # nums do
     if nums[i] + nums[j] + nums[k] == 2020 then
      print(nums[i] * nums[j] * nums[k]) 
     end
    end
  end
end
