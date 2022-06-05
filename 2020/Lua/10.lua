local nums, pres = {0}, {[0] = true}
for line in io.lines("10.txt") do
  table.insert(nums, tonumber(line))
  pres[tonumber(line)] = true
end

table.sort(nums)
table.insert(nums, nums[#nums] + 3)
pres[nums[#nums]] = true

local dif1, dif3 = 0, 0
for _, n in pairs(nums) do
  if pres[n+1] then
    dif1 = dif1 + 1
  elseif pres[n+3] then
    dif3 = dif3 + 1
  end
end
print(dif1 * dif3)

local ways = {[0] = 1}
for _, n in pairs(nums) do
  if n ~= 0 then
    ways[n] = (ways[n-3] or 0) + (ways[n-2] or 0) + (ways[n-1] or 0)
  end
end
print(ways[nums[#nums]])
