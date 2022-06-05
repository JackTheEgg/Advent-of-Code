local sTurn = {}
local turn, lastSpoken = 0, nil
for line in io.lines("15.txt") do
  for c in line:gmatch("(%d+),?") do
    turn = turn + 1
    sTurn[tonumber(c)] = {turn}
    lastSpoken = tonumber(c)
  end
end

for i = turn + 1, 30000000 do
  if i == 2021 then print(lastSpoken) end
  if not sTurn[lastSpoken] or #sTurn[lastSpoken] == 1 then
    table.insert(sTurn[0], i)
    lastSpoken = 0
  else
    local next = sTurn[lastSpoken][2] - sTurn[lastSpoken][1]
    table.remove(sTurn[lastSpoken], 1)
    if sTurn[next] then table.insert(sTurn[next], i) else sTurn[next] = {i} end
    lastSpoken = next
  end
end
print(lastSpoken)
