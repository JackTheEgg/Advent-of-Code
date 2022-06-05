local function toBits(num,bits)
    local t = {}
    for b = bits, 1, -1 do
        t[b] = math.fmod(num, 2)
        num = math.floor((num - t[b]) / 2)
    end
    return t
end

local combs = {[0] = 1}
for i = 1, 37 do combs[i] = combs[i - 1] * 2 end

local memory, memory2, mask = {}, {}, nil
for line in io.lines("14.txt") do
  if line:find("mask") then
    mask = line:match("mask = (.+)")
  else
    local dir, n = line:match("mem%[(%d+)%] = (%d+)")
    local bin = toBits(tonumber(n), 36)
    local binDir = toBits(tonumber(dir), 36)
    for i = 1, #mask do
      if mask:sub(i, i) ~= "X" then bin[i] = mask:sub(i,i) end
      if mask:sub(i,i) == "X" or mask:sub(i,i) == "1" then binDir[i] = mask:sub(i,i) end
    end
    memory[tonumber(dir)] = tonumber(table.concat(bin), 2)
    local xCount = 0
    for _, v in pairs(binDir) do if v == "X" then xCount = xCount + 1 end end
    local maxCombs, cmbs, vals = combs[xCount], 0, {}
    while cmbs < maxCombs do
      local s = ""
      for _ = 1, xCount do
        s = s .. math.random(0,1) -- lol
      end
      vals[s] = true
      cmbs = 0
      for _ in pairs(vals) do
        cmbs = cmbs + 1
      end
    end
    for b in pairs(vals) do
      local test, i = table.concat(binDir), 1
      local t = {}
      for c in test:gmatch(".") do table.insert(t, c) end
      for k in pairs(t) do if t[k] == "X" then t[k] = b:sub(i,i) i = i + 1 end end
      memory2[tonumber(table.concat(t), 2)] = tonumber(n)
    end
  end
end

local count = 0
for _, v in pairs(memory) do count = count + v end
print(count)

count = 0
for _, v in pairs(memory2) do count = count + v end
print(count)
