-- Loaded after Omarchy defaults from ~/.config/hypr/bindings.lua.
-- Keep the firmware's window actions useful across workspace layouts.
local function horizontal_action(direction, swap)
  return function()
    local window = hl.get_active_window()
    if not window then
      return
    end

    local workspace = window.workspace
    if not window.floating and workspace and workspace.tiled_layout == "scrolling" then
      hl.dispatch(hl.dsp.layout((swap and "swapcol " or "focus ") .. direction))
    elseif swap then
      hl.dispatch(hl.dsp.window.swap({ direction = direction }))
    else
      hl.dispatch(hl.dsp.focus({ direction = direction }))
    end
  end
end

-- Replace ordinary left/right focus and swap with layout-aware variants.
o.rebind("SUPER + LEFT", "Focus left (layout-aware)", horizontal_action("l", false))
o.rebind("SUPER + RIGHT", "Focus right (layout-aware)", horizontal_action("r", false))
o.rebind("SUPER + SHIFT + LEFT", "Swap left (column in scrolling)", horizontal_action("l", true))
o.rebind("SUPER + SHIFT + RIGHT", "Swap right (column in scrolling)", horizontal_action("r", true))

-- Dedicated, previously unbound chords for the next monitor (not a direction).
-- Omarchy's helpers preserve monitor-local workspace ownership when moving.
-- XKB's evdev map names physical F13/F14 XF86Tools/XF86Launch5. Match the
-- physical XKB codes (Linux KEY_F13/F14 + 8), independent of those keysyms.
o.bind("SUPER + CTRL + ALT + code:191", "Move window to next monitor", o.workspaces.move_window_to_monitor("+1"))
o.bind("SUPER + CTRL + ALT + code:192", "Move workspace to next monitor", o.workspaces.move_to_monitor("+1"))
