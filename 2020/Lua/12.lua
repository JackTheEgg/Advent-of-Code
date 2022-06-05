local x, y, face, i = 0, 0, "E", 2
local faces = {"N", "E", "S", "W"}
local dirs = {["N"] = {0,1}, ["E"] = {1,0}, ["S"] = {0,-1}, ["W"] = {-1,0}}

for line in io.lines("12.txt") do
  local instr, n = line:match("(%w)(%d+)")
  if instr == "N" then y = y + tonumber(n)
  elseif instr == "S" then y = y - tonumber(n)
  elseif instr == "W" then x = x - tonumber(n)
  elseif instr == "E" then x = x + tonumber(n)
  elseif instr == "F" then x = x + tonumber(n) * dirs[face][1] y = y + tonumber(n) * dirs[face][2]
  elseif instr == "L" then i = (i - tonumber(n) / 90) if i <= 0 then i = i + 4 end face = faces[i]
  elseif instr == "R" then i = (i + tonumber(n) / 90) if i > 4 then i = i - 4 end face = faces[i]
  end
end
print(math.abs(x) + math.abs(y))

local function rot90L(x, y)
  return -y, x
end

local function rot90R(x, y)
  return y, -x
end

local x, y, Wx, Wy = 0, 0, 10, 1

for line in io.lines("12.txt") do
  local instr, n = line:match("(%w)(%d+)")
  if instr == "N" then Wy = Wy + tonumber(n)
  elseif instr == "S" then Wy = Wy - tonumber(n)
  elseif instr == "W" then Wx = Wx - tonumber(n)
  elseif instr == "E" then Wx = Wx + tonumber(n)
  elseif instr == "F" then x = x + tonumber(n) * Wx y = y + tonumber(n) * Wy
  elseif instr == "L" then
    if n == "180" then Wx = -Wx Wy = -Wy
    elseif n == "90" then Wx, Wy = rot90L(Wx, Wy)
    elseif n == "270" then Wx, Wy = rot90R(Wx, Wy)
    end
  elseif instr == "R" then
    if n == "180" then Wx = -Wx Wy = -Wy
    elseif n == "90" then Wx, Wy = rot90R(Wx, Wy)
    elseif n == "270" then Wx, Wy = rot90L(Wx, Wy)
    end
  end
end
print(math.abs(x) + math.abs(y))
