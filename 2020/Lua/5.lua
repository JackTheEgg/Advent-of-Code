local seats = {}
for line in io.lines("5.txt") do
  line = line:gsub("F", "0")
  line = line:gsub("B", "1")
  line = line:gsub("L", "0")
  line = line:gsub("R", "1")
  table.insert(seats, tonumber(line, 2))
end
table.sort(seats)
print(seats[#seats])

for i, _ in pairs(seats) do
  if seats[i+1] - seats[i] ~= 1 then
    print(seats[i] + 1)
    break
  end
end
