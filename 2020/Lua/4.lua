local pps = {}
local pp = {}
for line in io.lines("4.txt") do
  if line == "" then table.insert(pps, pp) pp = {} end
  for info in line:gmatch("%S+:%S+") do
    local k, v = info:match("(%S+)%:(%S+)")
    pp[k] = v
  end
end
table.insert(pps, pp)

local function checkByr(n)
  return tonumber(n) >= 1920 and tonumber(n) <= 2002 end

local function checkIyr(n)
  return tonumber(n) >= 2010 and tonumber(n) <= 2020 end

local function checkEyr(n)
  return tonumber(n) >= 2020 and tonumber(n) <= 2030 end

local function checkHgt(s)
  if s:sub(-2, -1) == "cm" then
    return tonumber(s:sub(1,-3)) >= 150 and tonumber(s:sub(1,-3)) <= 193
  elseif s:sub(-2, -1) == "in" then
    return tonumber(s:sub(1,-3)) >= 59 and tonumber(s:sub(1,-3)) <= 76
  end
end

local function checkHcl(s)
  return s:match("%#[0-9, a-f+]") and #s == 7 end

local function checkEcl(s)
  return s == "amb" or s == "blu" or s == "brn" or s == "gry" or s == "grn" or s == "hzl" or s == "oth" end

local function checkPid(s)
  return s:match("%d%d%d%d%d%d%d%d%d") and #s == 9 end

local count = 0
local count2 = 0
for _, pp in pairs(pps) do
  local c = 0
  for _, _ in pairs(pp) do
    c = c + 1
  end
  if (c == 8) or (c == 7 and not pp["cid"]) then
    count = count + 1
    if checkByr(pp["byr"]) and
      checkIyr(pp["iyr"]) and
      checkEyr(pp["eyr"]) and
      checkHgt(pp["hgt"]) and
      checkHcl(pp["hcl"]) and
      checkEcl(pp["ecl"]) and
      checkPid(pp["pid"]) then
        count2 = count2 + 1
      end
  end
end
print(count)
print(count2)
