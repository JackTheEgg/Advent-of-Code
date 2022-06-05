local q1, q2, count, count2, lcount = {}, {}, 0, 0, 0
for line in io.lines("6.txt") do
  if line == "" then
    for _ in pairs(q1) do
      count = count + 1
    end
    q1 = {}
    for _, total in pairs(q2) do
      if total == lcount then
        count2 = count2 + 1
      end
    end
    q2 = {}
    lcount = 0
  else
    lcount = lcount + 1
    for c in line:gmatch(".") do
      if q2[c] then q2[c] = q2[c] + 1 else q2[c] = 1 end
      q1[c] = true
    end
  end
end

for _ in pairs(q1) do
  count = count + 1
end

for _, total in pairs(q2) do
  if total == lcount then
    count2 = count2 + 1
  end
end
print(count)
print(count2)
