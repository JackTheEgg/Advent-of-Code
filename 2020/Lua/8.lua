local prog = {}
for line in io.lines("8.txt") do
  local instr, n = line:match("(%l+) (%+?%-?%d+)")
  table.insert(prog, { opc = instr, val = tonumber(n), vis = false })
end

local function copy(tbl)
  local newtbl = {}
  for k, v in pairs(tbl) do
    if type(v) == "table" then
      newtbl[k] = copy(v)
    else
      newtbl[k] = v
    end
  end
  return newtbl
end

local function run(prog)
  local i, acc = 1, 0
  while true do
    if i == #prog + 1 then return acc, true
    elseif prog[i].vis then return acc, false
    elseif prog[i].opc == "acc" then
      acc = acc + prog[i].val
      prog[i].vis = true
      i = i + 1
    elseif prog[i].opc == "jmp" then
      prog[i].vis = true
      i = i + prog[i].val
    elseif prog[i].opc == "nop" then
      prog[i].vis = true
      i = i + 1
    end
  end
end

local progs = {[1] = prog}
for k, v in pairs(prog) do
  if v.opc == "jmp" then
    local test = copy(prog)
    test[k].opc = "nop"
    table.insert(progs, test)
  elseif v.opc == "nop" then
    local test = copy(prog)
    test[k].opc = "jmp"
    table.insert(progs, test)
  end
end

for k, v in pairs(progs) do
  local acc, good = run(v)
  if k == 1 then print(acc) end
  if good then print(acc) break end
end
