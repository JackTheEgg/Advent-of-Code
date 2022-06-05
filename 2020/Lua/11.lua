local x, y, seats, seats2 = 1, 1, {}, {}
for line in io.lines("11.txt") do
  for c in line:gmatch(".") do
    seats["("..x..","..y..")"] = c
    seats2["("..x..","..y..")"] = c
    x = x + 1
  end
  y = y + 1
  x = 1
end

local function step(sts)
  local newSts = {}
  for k, v in pairs(sts) do
    if v ~= "." then
      local x, y = k:match("%((%d+),(%d+)%)")
      local chars = {}
      for dx = -1, 1 do
        for dy = -1, 1 do
          if not (dx == 0 and dy == 0) then table.insert(chars, sts["("..x+dx..","..y+dy..")"] or " ") end
        end
      end
      local occ = 0 for _, s in pairs(chars) do if s == "#" then occ = occ + 1 end end
      if v == "L" then if occ == 0 then newSts[k] = "#" else newSts[k] = "L" end
      elseif v == "#" then if occ >= 4 then newSts[k] = "L" else newSts[k] = "#" end
      end
    else
      newSts[k] = "."
    end
  end
  return newSts
end

local dirs = {{1,0}, {-1,0}, {-1,-1}, {1,1}, {1,-1}, {-1,1}, {0,1}, {0,-1}}
local function step2(sts)
  local newSts = {}
  for k, v in pairs(sts) do
    if v ~= "." then
      local chars = {}
      for _, dir in pairs(dirs) do
        local x, y = k:match("%((%d+),(%d+)%)")
        x = x + dir[1]
        y = y + dir[2]
        while sts["("..x..","..y..")"] do
          if sts["("..x..","..y..")"] ~= "." then table.insert(chars, sts["("..x..","..y..")"]) break end
          x = x + dir[1]
          y = y + dir[2]
        end
      end
      local occ = 0 for _, s in pairs(chars) do if s == "#" then occ = occ + 1 end end
      if v == "L" then if occ == 0 then newSts[k] = "#" else newSts[k] = "L" end
      elseif v == "#" then if occ >= 5 then newSts[k] = "L" else newSts[k] = "#" end
      end
    else
      newSts[k] = "."
    end
  end
  return newSts
end

local states = {seats}
while true do
  seats = step(seats)
  local same = true
  for k in pairs(seats) do
    if seats[k] ~= states[#states][k] then same = false break end
  end
  if same then local count = 0 for _, v in pairs(seats) do if v == "#" then count = count + 1 end end print(count) break end
  table.insert(states, seats)
end

local states2 = {seats2}
while true do
  seats2 = step2(seats2)
  local same = true
  for k in pairs(seats2) do
    if seats2[k] ~= states2[#states2][k] then same = false break end
  end
  if same then local count = 0 for _, v in pairs(seats2) do if v == "#" then count = count + 1 end end print(count) break end
  table.insert(states2, seats2)
end
