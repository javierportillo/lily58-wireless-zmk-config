# Clean keymap design brief

User preferences recorded on 2026-10-16. This is a design brief, not the current
bindings. Keep `config/lily58.keymap` as the original reference and develop the
replacement separately in `config/clean.keymap`.
Use the naming scheme in `key-positions.md`; an omitted side means both halves.

The [first complete map](keymap-draft.md) is now implemented in `config/clean.keymap`
and built for both halves. It includes the requested Symbols swap between
`RC4`–`RC5` and `RD4`–`RD5`. The left half was flashed on 2026-10-21 and its USB
keyboard return verified; typing and shortcut testing remain. The brief below
records the preferences that led to this design.

## Physical comfort and accuracy

- The main QWERTY letter positions on the home, upper, and lower rows are most
  accurate.
- Pinky extensions are inaccurate, except the outer home-row positions `C6`,
  which are comfortable.
- The number row is low accuracy. Keeping it for convenience remains an open
  question; essential number and symbol entry should have a comfortable path.
- Thumb preference: `E2` is home and most comfortable; `E1` is a close second;
  `E3` is mediocre; `E4` is almost unusable.
- The extra inner positions `D0` are hard to reach.
- Escape must be especially easy to reach.

## Interaction preferences

- Persistent layer selection is desirable. Holding a layer key while also
  holding modifiers and a target is undesirable.
- A predictable return to base through `RE2`, regardless of the active layer,
  is a valued property of the original layout. Agreed base behavior: remain
  on base without emitting a character or shortcut.
- Double taps are unreliable. Avoid tap dances for choosing layers.
- Home row modifiers are liked, but reaching arbitrary combinations with all
  target types is more important than blindly preserving their old behavior.
- **Chosen:** two-tap menu. Tap once to enter the selector, then tap a target
  selector key to enter a persistent layer. No layer key remains held.
- **Chosen:** retain home row modifiers and supplement them with one-shot
  modifiers for awkward keyboard chords.

## Required coverage

- Modifiers and combinations must work with letters, arrows, function keys,
  top-row number keycodes, keypad number keycodes, and other navigation keys.
- Preserve the distinction between number-row and keypad HID keycodes because
  some applications treat them differently.
- Keep a mouse layer. Use a WASD-shaped directional arrangement for both
  pointer movement and horizontal/vertical scrolling, rather than Vim's HJKL.
  **Chosen:** left hand moves the pointer; right hand scrolls.
- Support modified clicks, Ctrl+scroll zoom, and sustained modified mouse
  operations. Do not assume ZMK v0.3's one-shot keyboard modifiers automatically
  consume mouse events correctly; verify that path before relying on it.
- Integrate with the installed Omarchy shortcuts for focus, workspaces, window
  movement, resizing, grouping, and other common desktop actions.
- Accommodate Vim and tmux. Tmux's prefix is Ctrl+A; this must be easy and
  reliable. Escape is a priority.
- Modifier-only presses/chords must reach the host without a target key.
  Example: Ctrl+Alt releases keyboard capture in some VNC/VM applications.
  Preserve an explicit held-modifier path; one-shot/lazy implementations must
  not make a following ordinary key necessary to emit every modifier action.
  Include modifier press and release events in verification.

## Workflow and symbol priorities

Primary use is command-line work, tmux, and Vim. Optimize for those before
general programming. Bash is the main language; TypeScript is the secondary
programming reference, although much coding is now delegated to agents.

- Frequent command-line symbols: `/` for paths, `@` for Codex file references,
  `|` for pipes, `=` for assignments, and `_` for variable names.
- Vim priorities include `^`, `$`, `;`, and `,`.
- Organize all four bracket pairs consistently: `()`, `[]`, `{}`, and `<>`.
- Preserve practical access to other Bash and TypeScript punctuation when
  arranging the rest of the symbol layer; see the complete map for positions.

The user regularly writes both English and Spanish. Required Spanish characters
are **á é í ó ú ü ñ ¿ ¡**. **Chosen:** AltGr combinations with the current
`us(altgr-intl)` host layout. Provide comfortable access to Right Alt/AltGr and
preserve its combination with Shift for uppercase accented letters.

Compose is also required, although used less often. Allocate an explicit
Compose key; the complete map uses selector then C and a System duplicate. With the current host option
`compose:menu`, ZMK's `&kp K_APP` sends the Menu key that the host interprets as
Compose. This is a distinct action from the keyboard's layer-selection menu;
keep both concepts clearly named in diagrams and discussions.

## Organization goals

The original grew incrementally and feels inconsistent. Its symbol layer is
hard to remember: the user often falls back to shifted number-row symbols and
hunts for bracket pairs. Design by a small set of spatial rules, including a
consistent organization for `()`, `[]`, `{}`, and `<>`, and give frequent symbols
comfortable positions. Avoid adding isolated bindings without a place in the
overall system.

## Host configuration inspected

The actual Omarchy shortcut list was read with
`omarchy menu keybindings --print` on 2026-10-16. Relevant defaults include:

| Input | Action |
| --- | --- |
| Super + arrows | Focus window |
| Super + Shift + arrows | Swap window |
| Super + 0–9 | Select workspace |
| Super + Shift + 0–9 | Move window to workspace |
| Super + Shift + Alt + 0–9 | Move window silently to workspace |
| Super + Ctrl + Left/Right | Change grouped-window focus |
| Super + Alt + arrows | Move window into directional group |
| Super + Shift + Alt + arrows | Move workspace to another monitor |
| Super + Minus/Equal and variants | Expand/shrink window |
| Super + mouse buttons | Move/resize window |
| Super + mouse wheel | Scroll workspace |

Consult the live shortcut list before assigning the final window layer;
the user's overrides and Omarchy's scrolling layout matter.

The host keyboard configuration uses `us` with variant `altgr-intl`, plus
`compose:menu`. The user chose to keep AltGr combinations for Spanish and also
requires occasional Compose access. Preserve both paths in the new layout.

Tmux configuration is in `~/.config/tmux/tmux.conf`: prefix Ctrl+A, prefix then
Ctrl+A sends the prefix, Vim HJKL pane navigation, and Alt+digits selects windows.
Alt+Left/Right is defined twice: later previous/next-window bindings override
the earlier pane-navigation bindings. Do not change this host config as part of
the keymap redesign without a separate request.

## Design principles

- Preserve QWERTY letters; put frequent actions on `C6`, `E2`, and `E1`.
- Use a fixed single-tap return to base and deliberate persistent layer entry.
- Use the agreed `C6` assignments for Escape and layer entry; avoid essential actions on `E4`,
  `D0`, or the number row.
- Reuse modifier positions across functional layers, with direct modifier keys
  where there is no useful tap character. Treat held, one-shot, and sustained
  mouse modifiers as distinct requirements.
- Keep ordinary digits, keypad digits, and function keys spatially related but
  distinct. Apply the same ordering to Omarchy workspace selection.
- Group brackets spatially: one pair per adjacent pair of keys, with a fixed
  opener/closer direction and consistent ordering of pair types.
- Reuse one directional shape across navigation, mouse, scroll, and desktop
  operations where possible.
- Validate representative real tasks before expanding the design. Examples:
  Ctrl+A then a tmux command, Escape from an editor, Ctrl+Shift+Right,
  Alt+number-row digit, modified keypad input, Ctrl+F-key, Ctrl+scroll,
  modified click/drag, modifier-only Ctrl+Alt capture release, Spanish text,
  workspace selection/movement, and window resizing.

## Agreed anchors for the next design iteration

The user approved these assignments; they are implemented in the clean map.

| Position | Agreed role |
| --- | --- |
| `LE2` | Backspace |
| `LE1` | Space |
| `RE1` | Enter except in Menu, where it selects Windows |
| `RE2` | Return to base on every layer; no output when already on base |
| `LC6` | Escape on every layer |
| `RC6` | Open the layer selector on every layer |
| `LE3` | Tab |
| `RE3` | Delete |
| `E4`, `D0` | No essential action |

Agreed menu interaction: tap `RC6`, then tap a selector; the chosen layer stays
active until another selection or `RE2`. Approved selector positions use the
physical QWERTY letters S = Symbols, N = Numbers, V = Navigation, M = Mouse,
and RE1 = Windows. The complete map also assigns P = Keypad, F = Function,
B = System, and C = Compose then Base.

Mouse directions: left E/S/D/F physical positions for up/left/down/right,
and right I/J/K/L positions for scroll up/left/down/right. These are positional
diamonds, not linear HJKL navigation. Clicks occupy left Q/W/R/T and right Y;
sustained modifiers occupy row D on both hands. See the complete map for exact
bindings and examples.

## Windows layer revision after use (2026-11-13)

Approved and implemented: right A selects workspaces 1–5, B swaps in H/J/K/L
order plus fullscreen at RB5, C focuses in H/J/K/L order plus next monitor at
RC5, D sends silently to workspaces 1–5. Left B controls groups; LC1 is tiled
fullscreen, LC2/LC3 move the window/workspace to the next monitor. LC4/LC5 and
left D stay unused. Windows has no modifier strip, Restore, or workspace 6–10
bindings. Enter with RC6 then RE1, replacing the W selector. Join targets the
left group by default. See `windows-layer-proposal.md` for implementation details.
