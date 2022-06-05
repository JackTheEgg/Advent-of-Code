local grid = {}
local slopes = {{1,1}, {3,1}, {5,1}, {7,1}, {1,2}}
for line in io.lines("3.txt") do
  table.insert(grid, line)
end

local scores = {}
for n, coords in pairs(slopes) do
  local x, y, count = 1, 1, 0
  while true do
    if not grid[y] then break end
    if grid[y]:sub(x % #grid[y] ~= 0 and x % #grid[y] or #grid[y], x % #grid[y] ~= 0 and x % #grid[y] or #grid[y]) == "#" then
      count = count + 1
    end
    x = x + coords[1]
    y = y + coords[2]
  end
  if n == 2 then
    print(count)
  end
  table.insert(scores, count)
end

local prod = 1
for _, v in pairs(scores) do
  prod = prod * v
end
print(prod)
