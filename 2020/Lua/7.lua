local bags = {}
for line in io.lines("7.txt") do
  local color, contents = line:match("(.+) bags contain (.+)%.")
  if contents ~= "no other bags" then
    local contains = {}
    for c in contents:gmatch("%d+ .- bags?,?") do
      local cont, col = c:match("(%d+) (.-) bags?,?")
      contains[col] = cont
    end
    bags[color] = contains
  end
end

local function getLen(tbl)
  local count = 0
  for _ in pairs(tbl) do count = count + 1 end return count end

local golden = {}
while true do
  local check = getLen(golden)
  for bag, conts in pairs(bags) do
    if conts["shiny gold"] then
      golden[bag] = true
    end
    for k in pairs(conts) do
      if golden[k] then
        golden[bag] = true
      end
    end
  end
  if getLen(golden) == check then print(check) break end
end

local count = 0

local function getBags(inp)
  local contents = {}
  for bag, n in pairs(inp) do
    if bags[bag] then
      for cont, amount in pairs(bags[bag]) do
        if contents[cont] then contents[cont] = contents[cont] + n * amount else contents[cont] = n * amount end
        count = count + n * amount
      end
    end
  end
  return contents
end

local contents = {["shiny gold"] = 1}
while true do
  local check = getLen(contents)
  if check == 0 then print(count) break
else
  contents = getBags(contents)
  end
end
