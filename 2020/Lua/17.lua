local function willActivate(x, y, z, t)
  local count = 0
  for dx = -1, 1 do
    for dy = -1, 1 do
      for dz = -1, 1 do
        if not (dx == 0 and dy == 0 and dz == 0) then
          if t[x+dx..","..y+dy..","..z+dz] then count = count + 1 end
        end
      end
    end
  end
  if t[x..","..y..","..z] and (count == 2 or count == 3) then return true end
  if (not t[x..","..y..","..z]) and count == 3 then return true end
  return false
end

local function willActivate2(x, y, z, w, t)
  local count = 0
  for dx = -1, 1 do
    for dy = -1, 1 do
      for dz = -1, 1 do
        for dw = -1, 1 do
          if not (dx == 0 and dy == 0 and dz == 0 and dw == 0) then
            if t[x+dx..","..y+dy..","..z+dz..","..w+dw] then count = count + 1 end
          end
        end
      end
    end
  end
  if t[x..","..y..","..z..","..w] and (count == 2 or count == 3) then return true end
  if (not t[x..","..y..","..z..","..w]) and count == 3 then return true end
  return false
end

local function step(tbl)
  local newTbl = {}
  for k in pairs(tbl) do
    local x, y, z = k:match("(-?%d+),(-?%d+),(-?%d+)")
    x = tonumber(x)
    y = tonumber(y)
    z = tonumber(z)
    for dx = -1, 1 do
      for dy = -1, 1 do
        for dz = -1, 1 do
          if willActivate(x+dx, y+dy, z+dz, tbl) then newTbl[x+dx..","..y+dy..","..z+dz] = true end
        end
      end
    end
  end
  return newTbl
end

local function step2(tbl)
  local newTbl = {}
  for k in pairs(tbl) do
    local x, y, z, w = k:match("(-?%d+),(-?%d+),(-?%d+),(-?%d+)")
    x = tonumber(x)
    y = tonumber(y)
    z = tonumber(z)
    w = tonumber(w)
    for dx = -1, 1 do
      for dy = -1, 1 do
        for dz = -1, 1 do
          for dw = -1, 1 do
            if willActivate2(x+dx, y+dy, z+dz, w+dw, tbl) then newTbl[x+dx..","..y+dy..","..z+dz..","..w+dw] = true end
          end
        end
      end
    end
  end
  return newTbl
end

local active, active2 = {}, {}
local x, y = 1, 1
for l in io.lines("17.txt") do
  for c in l:gmatch(".") do
    if c == "#" then active[x..","..y..","..0] = true active2[x..","..y..",".."0"..","..0] = true end
    x = x + 1
  end
  x = 1
  y = y + 1
end

for _ = 1, 6 do
  active = step(active)
  active2 = step2(active2)
end

local count = 0
for _ in pairs(active) do count = count + 1 end
print(count)
count = 0
for _ in pairs(active2) do count = count + 1 end
print(count)
