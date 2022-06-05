local count = 0
local count2 = 0
for line in io.lines("2.txt") do
  local low, up, letter, str = line:match("(%d+)-(%d+) (%l): (%l+)")
  if (str:sub(low, low) == letter and str:sub(up, up) ~= letter) or (str:sub(low, low) ~= letter and str:sub(up, up) == letter)then
    count2 = count2 + 1
  end
  local c = 0
  for char in str:gmatch(".") do
    if char == letter then
      c = c + 1
    end
  end
  if c >= tonumber(low) and c <= tonumber(up) then
    count = count + 1
  end
end
print(count)
print(count2)
