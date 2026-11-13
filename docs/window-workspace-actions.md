# Window and workspace action catalog

Inspected 2026-11-13 against installed Hyprland 0.56.2 and Omarchy source/live
keybindings. This is the full relevant installed window/workspace shortcut set,
with repeated directions and workspace numbers grouped. It also lists unbound
Hyprland capabilities separately. It does not include application launchers,
session controls, recording, or arbitrary custom scripts.

Super = GUI/Windows key. Directions = arrow keys; n = 1–9 or 0 for slot 10.
Workspace slots refer to the focused monitor, not global Hyprland workspace IDs.
No bindings were changed while assembling this catalog.

## Focus and monitors

| Action | Current shortcut |
| --- | --- |
| Focus window left/down/up/right | Super + direction |
| Cycle windows forward/backward | Alt + Tab / Alt + Shift + Tab |
| Raise focused window / lower the window being left | Included in the Alt+Tab / Alt+Shift+Tab bindings |
| Focus next/previous monitor | Ctrl + Alt + Tab / Ctrl + Alt + Shift + Tab |
| Move focused window to monitor in a direction and follow | Super + Shift + Ctrl + direction |
| Move current workspace to monitor in a direction | Super + Shift + Alt + direction |
| Change monitor scaling up/down | Super + Slash / Super + Alt + Slash |

## Workspaces

| Action | Current shortcut |
| --- | --- |
| Select monitor-local workspace n | Super + n |
| Move focused window to workspace n and follow | Super + Shift + n |
| Move focused window to workspace n without following | Super + Shift + Alt + n |
| Next/previous workspace on this monitor | Super + Tab / Super + Shift + Tab |
| Return to former workspace on this monitor | Super + Ctrl + Tab |
| Next/previous workspace with pointer | Super + wheel down/up |
| Cycle layout forward/backward | Super + L / Super + Alt + L |
| Toggle scratchpad / send window there silently | Super + S / Super + Alt + S |
| Toggle Quake console / send window there silently | Super + Grave / Super + Shift + Grave |

Layout cycle: Dwindle → Scrolling → Floating; backward reverses it. Workspace
IDs are allocated in monitor-owned blocks, but the shortcuts keep local labels
1–10. Local slots 6–10 remain available to the host even if omitted from the
proposed keyboard layer.

## Window state and lifetime

| Action | Current shortcut |
| --- | --- |
| Close focused window | Super + W or Super + Q |
| Close all windows | Ctrl + Alt + Delete |
| Toggle floating/tiling | Super + T |
| Fullscreen | Super + F |
| Tiled fullscreen | Super + Ctrl + F |
| Full width / maximized | Super + Alt + F |
| Pop out: float and pin | Super + O |
| Minimize to dock | Super + M |
| Toggle transparency | Super + Backspace |
| Toggle gaps | Super + Shift + Backspace |
| Toggle single-window square aspect | Super + Ctrl + Backspace |
| Toggle full-screen desktop presentation | Super + Ctrl + Alt + F |
| Toggle Dwindle split | Super + J |

Pseudo-tiling exists in Omarchy defaults at Super+P, but Javi overrides that
shortcut with password-manager autotype. It is not currently an available
pseudo-tiling shortcut. Likewise Super+Shift+Alt+G is Javi's WhatsApp launcher.
The desktop presentation toggle is a host UI mode, distinct from fullscreening
one window.

## Position and size

| Action | Current shortcut |
| --- | --- |
| Swap focused window in a direction | Super + Shift + direction |
| Grow/shrink width | Super + Minus / Super + Equal |
| Grow/shrink width by a small step | Add Alt to the preceding shortcuts |
| Grow/shrink width by a large step | Add Ctrl to the preceding shortcuts |
| Shrink/grow height | Super + Shift + Minus / Super + Shift + Equal |
| Small/large height steps | Add Alt / Ctrl to the preceding shortcuts |
| Save width / restore saved width | Super + Alt + Home / Super + Home |
| Drag window / resize with pointer | Super + left mouse / Super + right mouse |

Javi's Width +/- override cycles the configured presets on tiled Scrolling
windows: 33.3%, 50%, 66.7%, 100%. Elsewhere it uses the original 100px step.
The Alt and Ctrl variants remain the original 25px and 300px resize operations;
they do not cycle presets. Height defaults use 100px, with the same 25/300px
variants. Actual geometry depends on the layout and application size constraints.

## Window groups (tabs)

| Action | Current shortcut |
| --- | --- |
| Toggle grouping | Super + G |
| Move window out of group | Super + Alt + G |
| Move window into neighboring group in a direction | Super + Alt + direction |
| Next/previous group tab | Super + Alt + Tab / Super + Alt + Shift + Tab |
| Previous/next group tab | Super + Ctrl + Left / Right |
| Select group tab 1–5 | Super + Alt + 1–5 |
| Next/previous group tab with pointer | Super + Alt + wheel down/up |

## Scrolling-specific actions, available but not separately bound

These are layout messages, not ordinary global shortcuts. New host bindings
would be needed to call them from firmware. Verified against the
[Hyprland 0.56 Scrolling reference](https://wiki.hypr.land/0.56.0/Configuring/Layouts/Scrolling-Layout/).

| Message | Purpose |
| --- | --- |
| `move` | Pan the tape by pixels or columns |
| `colresize` | Set/cycle width; optionally set every column's width |
| `fit active/visible/all/toend/tobeg/expand` | Fit selected columns; expand uses spare space |
| `fit_into_view` | Reveal the active column fully |
| `focus` | Layout-local directional focus with wrapping |
| `swapcol l/r` | Reorder whole columns |
| `promote` / `expel` | Give a window its own column |
| `consume` | Put the window into the preceding column |
| `consume_or_expel prev/next` | Join or leave a column depending on its contents |
| `inhibit_scroll` | Toggle workspace tape movement |

The proposed focus/swap rows would add layout-aware host handling for the
Scrolling-specific horizontal actions. Existing Super+arrow / Super+Shift+arrow
bindings currently use ordinary focus/swap dispatchers.

## Additional unbound Hyprland building blocks

The installed Lua API (`/usr/share/hypr/stubs/hl.meta.lua`) also exposes:

- Window: center, pin/unpin, pseudo-tile, raise/lower, exact or relative move and
  resize, target-specific swap, separate client/internal fullscreen state.
- Groups: reorder tabs, lock groups/all groups, deny a window group membership.
- Workspace: rename, change ID, move to a monitor, swap monitors' active
  workspaces, arbitrary named/special workspaces.
- Automation: focus a chosen application/window, manipulate window properties
  and tags, reveal swallowed windows, send shortcuts, release input capture.
- Process control: force-kill or signal a window's process (distinct from close).
- Other layouts have their own layout messages; they need layout-specific
  checks rather than assuming Scrolling commands work everywhere.

These are capabilities to bind deliberately, not additional defaults. Arbitrary
Lua and scripts can combine them, so there is no finite list of every possible
compound action. The [dispatcher reference](https://wiki.hypr.land/configuring/core/dispatchers/)
describes the broader API; installed 0.56.2 stubs are the version check for this
machine.

## Local evidence and refreshing this list

- `omarchy menu keybindings --print`: live merged shortcut descriptions.
- `/usr/share/omarchy/default/hypr/bindings/tiling.lua`: default window/workspace
  shortcuts and dispatcher semantics.
- `/usr/share/omarchy/default/hypr/monitor-workspaces.lua`: monitor ownership,
  local slot focus, silent moves, and monitor transfers.
- `/usr/share/omarchy/default/hypr/bindings/utilities.lua`: appearance toggles.
- `~/.config/hypr/bindings.lua`: password-manager overrides and width presets.
- `/usr/share/omarchy/bin/omarchy-hyprland-workspace-layout-toggle`: layout cycle.
