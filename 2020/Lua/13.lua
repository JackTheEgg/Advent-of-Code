local buses, buses2, lcount, tstamp, cCount = {}, {}, 0, 0, 0
for line in io.lines("13.txt") do
  if lcount == 0 then tstamp = tonumber(line) lcount = lcount + 1
  else
    for c in line:gmatch("(%d+)") do table.insert(buses, tonumber(c)) end
    for c in line:gmatch("(%w+)") do if c:match("(%d+)") then buses2[tonumber(c)] = cCount end cCount = cCount + 1 end
  end
end

local rems = {}
for _, v in pairs(buses) do
  table.insert(rems, { id = v, val = v - (tstamp % v) })
end
table.sort(rems, function(a, b) return a.val < b.val end)
print(rems[1].val * rems[1].id)

local d, i = 1, 0
for bus, off in pairs(buses2) do
  while true do
    i = i + d
    if (i + off) % bus == 0 then
      d = d * bus
      break
    end
  end
end
print(i)
