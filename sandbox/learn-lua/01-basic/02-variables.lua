local num = 42
print(num)
-- NOTE: assigning without 'local' creates a global variable (likely unintended)
local s = "Hello" -- Immutable strings like Python
local r = "Hello"
local u = [[ Double brackets
	     start and end
	     multi-learn strings.]]
local t = nil -- Undefines t; Lua has garbage collection.
print(s, r, t)
print("-------MultiLine Comment-------")
print(u)
print()
