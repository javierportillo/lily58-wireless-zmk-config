# Windows layer redesign

Approved redesign implemented on 2026-11-13 in `config/clean.keymap`.
Both halves compile; the physical flash result is recorded in `keymap-draft.md`. Based on Javi's physical trial and the installed Omarchy
bindings, including monitor-scoped workspace helpers and the custom width presets.

## Entry and organization

In Menu only, RE1 selects Windows instead of sending Enter. Entry is therefore
RC6 → RE1, entirely on the right hand. RE1 remains Enter on other layers.
RE2 always returns to Base; RC6 still opens Menu; LC6 remains Escape.
The W selector is removed; RE1 is the primary Windows entry route.

Right side, columns 1–5 from center outward:

| Row | R1 | R2 | R3 | R4 | R5 |
| --- | --- | --- | --- | --- | --- |
| A | Workspace 1 | Workspace 2 | Workspace 3 | Workspace 4 | Workspace 5 |
| B | Swap left | Swap down | Swap up | Swap right | Fullscreen |
| C | Focus left | Focus down | Focus up | Focus right | Next monitor |
| D | Send silently WS1 | Send silently WS2 | Send silently WS3 | Send silently WS4 | Send silently WS5 |

H/J/K/L are physical direction mnemonics. All actions include their modifiers.
RA1–RA5 select monitor-local workspace slots; RD1–RD5 send the window silently
to those slots on the current monitor. The latest revision replaces row-A resize
controls with one-handed workspace selection. **RA6 increases width; RB6 reduces
width**, using the previous Super+Minus / Super+Equal actions. In Scrolling these
step through 33.3%, 50%, 66.7%, 100%; floating windows and other layouts retain
100px steps. Familiar Base shortcuts remain available.

RC5 selects the next monitor, alternating between the two enabled monitors and
retaining each monitor's active workspace. RB5 toggles ordinary fullscreen.

Left side, columns 1–5 from center outward:

| Row | L1 | L2 | L3 | L4 | L5 |
| --- | --- | --- | --- | --- | --- |
| B | Toggle group | Join group | Leave group | Next group tab | Previous group tab |
| C | Tiled fullscreen | Move window to next monitor | Move workspace to next monitor | Unassigned | Unassigned |
| D | Unassigned | Unassigned | Unassigned | Unassigned | Unassigned |

Join targets the group to the left (the default selected for implementation). Left row A remains unassigned. No modifier
strip, Restore action, or workspace 6–10 duplicates. E4 and D0 stay unused.
Other global anchors, including Space at LE1 and Backspace at LE2, are preserved.

The visualizer is generated directly from the implemented keymap; the separate
preview data and preview-only diagram have been retired.

## Installed host behavior

Use layout-aware horizontal focus: Scrolling's `focus l/r` stays on the current
monitor and wraps; other layouts retain ordinary directional focus. This keeps
RC5 the deliberate monitor-change action. Use `swapcol l/r` for Scrolling's
horizontal swap, with normal swaps on other layouts. Vertical focus/swap retain
ordinary behavior. These bindings are implemented in `host/windows-layer.lua`.

Normal window swaps and whole-column swaps differ when multiple windows share
a Scrolling column. The proposal intentionally chooses whole-column left/right
swaps, so the ordering of the scrolling tape is predictable.

## Available actions

See [window/workspace action catalog](window-workspace-actions.md). Choose further
secondary actions from there before populating the remaining left-hand keys.

## Host installation and checks

`~/.config/hypr/bindings.lua` loads this repository's `host/windows-layer.lua`
with `dofile` after the defaults. The loader currently uses the absolute checkout
path; update it if moving the checkout. The pre-install bindings file was backed
up alongside itself as `bindings.lua.bak.<timestamp>`.

LC2 sends Super+Ctrl+Alt+F13; LC3 sends Super+Ctrl+Alt+F14. These new host chords
call Omarchy's monitor-scoped `move_window_to_monitor("+1")` and
`move_to_monitor("+1")` helpers. RC5 keeps the existing Ctrl+Alt+Tab focus action.
The remaining keys use existing Omarchy shortcuts, including silent workspace
moves and group controls.

After host edits, run `lua tests/test_windows_layer.lua`, `hyprctl reload`, and
`hyprctl configerrors`. The Lua test covers Scrolling, other layouts, floating
windows, no focused window, and monitor-helper selection. It does not substitute
for physical keyboard/window interaction testing. Rebuild both firmware halves
and flash the left using the normal scripts after keymap edits.
