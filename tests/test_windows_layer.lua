-- Run from the repository root: lua tests/test_windows_layer.lua
local bindings, calls, active = {}, {}, nil
local function action(kind, value)
  return { kind = kind, value = value }
end
hl = {
  get_active_window = function() return active end,
  dispatch = function(value) calls[#calls + 1] = value end,
  dsp = {
    layout = function(value) return action("layout", value) end,
    focus = function(value) return action("focus", value.direction) end,
    window = { swap = function(value) return action("swap", value.direction) end },
  },
}
o = {
  bind = function(key, _, callback) assert(not bindings[key]); bindings[key] = callback end,
  rebind = function(key, _, callback) bindings[key] = callback end,
  workspaces = {
    move_window_to_monitor = function(target) return action("move window", target) end,
    move_to_monitor = function(target) return action("move workspace", target) end,
  },
}
dofile("host/windows-layer.lua")

for _, direction in ipairs({ {"LEFT", "l"}, {"RIGHT", "r"} }) do
  for _, swap in ipairs({ false, true }) do
    local key = "SUPER + " .. (swap and "SHIFT + " or "") .. direction[1]
    for _, layout in ipairs({ "scrolling", "dwindle" }) do
      for _, floating in ipairs({ false, true }) do
        active = { floating = floating, workspace = { tiled_layout = layout } }
        bindings[key]()
        local result = calls[#calls]
        if layout == "scrolling" and not floating then
          assert(result.kind == "layout")
          assert(result.value == (swap and "swapcol " or "focus ") .. direction[2])
        else
          assert(result.kind == (swap and "swap" or "focus"))
          assert(result.value == direction[2])
        end
      end
    end
    active = nil
    local count = #calls
    bindings[key]()
    assert(#calls == count, "No active window must be a no-op")
  end
end
-- XKB maps physical F13/F14 to XF86Tools/XF86Launch5 on this host.
-- Bind their XKB keycodes, so the firmware's HID keys still trigger the action.
assert(bindings["SUPER + CTRL + ALT + code:191"], "Physical F13 must match regardless of its keysym")
assert(bindings["SUPER + CTRL + ALT + code:192"], "Physical F14 must match regardless of its keysym")
assert(bindings["SUPER + CTRL + ALT + code:191"].kind == "move window")
assert(bindings["SUPER + CTRL + ALT + code:192"].kind == "move workspace")
assert(bindings["SUPER + CTRL + ALT + code:191"].value == "+1")
assert(bindings["SUPER + CTRL + ALT + code:192"].value == "+1")
print("Windows host routing: scrolling, other layouts, floating, no window, monitor actions passed")
