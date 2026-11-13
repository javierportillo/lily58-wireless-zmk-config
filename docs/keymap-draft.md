# Clean keymap: first complete draft

[Open the visual reference](clean-keymap.html) for all ten layers, physical
positions, and modifier labels. Regenerate it after keymap changes with
`./scripts/render-keymap`.

On Javi's desktop, search **Lily58 Keymap** in the app menu. It opens a standalone
Omarchy app window and regenerates the reference on launch. The launcher invokes
`scripts/open-visualizer`; its desktop entry is
`~/.local/share/applications/lily58-keymap.desktop`.

**Status: implemented in `config/clean.keymap`. Latest Windows revision built
for both halves and flashed to the left on 2026-11-13; matching USB keyboard
return verified. Physical trial of the new Windows actions remains.**
The agreed anchors and user requirements come from [the design brief](keymap-design-brief.md).
The preserved original remains `config/lily58.keymap` and is still the default.
This document describes the first complete clean map, including the requested
swap of Symbols `RC4`–`RC5` with `RD4`–`RD5`.

## Reading the maps

Names use [physical positions](key-positions.md), counted from center outward.
The diagrams show the ten main letter columns in their physical order:

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
```

Each diagram has rows B, C, and D. Outer column 6, row A, extra inner keys D0,
and thumbs are specified separately below. `—` means no action, not transparent
fall-through to a different layer. An unsided position means both halves.

`Sh` = Shift, `Su` = Super/GUI, `Al` = left Alt, `Ct` = Ctrl,
`AG` = Right Alt/AltGr. Prefix `o` means a one-shot modifier. A slash in a
typing key such as `F/Ct` separates its tap letter from its held modifier.

## Shared anchors

These anchors are shared, with the explicit Menu exception for RE1 below:

| Position | Action |
| --- | --- |
| `LC6` | Escape |
| `RC6` | Enter the layer selector |
| `LE1` | Space |
| `LE2` | Backspace |
| `LE3` | Tab |
| `RE1` | Enter, except selects Windows in Menu |
| `RE2` | Select Base; produce no host key |
| `RE3` | Delete |
| `E4`, `D0` | No action |

The thumb row, viewed physically, is therefore:

```text
LE4   LE3   LE2    LE1  |  RE1    RE2   RE3   RE4
 —    Tab   Bspc Space |  Enter  Home  Del    —
```

Here `Home` means **keyboard Base layer**, not the Home navigation key.
Pressing `RE2` while already on Base does nothing. Escape stays Escape and does
not silently switch layers. Compose is distinct from the layer selector.

Except for Base, Symbols, and the maintenance exceptions described below,
`B6`, `D6`, and all of row A are unassigned. Base retains the familiar number
row for convenience; comfortable digit entry also exists on Numbers.

## Layer selection and one-shot modifiers

Tap `RC6`, release it, then tap a selector. The selected layer stays active.
There are no double taps, timed tap counts, held layer keys, or cycling through
layers. `RE2` cancels selection and returns to Base. Pressing `RC6` while already
in the selector simply stays there.

| Physical letter / position | Destination |
| --- | --- |
| S / `LC4` | Symbols |
| N / `RD1` | Numbers: ordinary number-row digit keycodes |
| P / `RB5` | Keypad: native keypad digit keycodes |
| F / `LC2` | Function keys |
| V / `LD2` | Navigation |
| M / `RD2` | Mouse |
| Enter thumb / `RE1` | Windows / Omarchy |
| B / `LD1` | System: Bluetooth, media, display, output selection |
| C / `LD3` | Send Compose, then return to Base |

The selector doubles as the one-shot modifier palette on the right home row:

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       —     —     —     —     —  |   —     —     —     —    Pad
C       —   Symbols —    Fn     —  |  oAG   oCt   oAl   oSu   oSh
D       —     —   Compose Nav  Sys |  Num  Mouse   —     —     —
```

For example: selector, `RC2` (one-shot Ctrl), `RC5` (one-shot Shift), V, Right
produces Ctrl+Shift+Right. Selector, `RC2`, F, F5 produces Ctrl+F5. Selector,
`RC1`, `RE2`, A produces AltGr+A. Selecting layers produces no ordinary keyboard
events, so it must not consume an armed one-shot modifier.

Use lazy, stackable one-shots for keyboard actions, initially with a five-second
expiry. They apply to the next ordinary keyboard key through its release, so
holding that target can repeat with the modifiers still active. `RE2` changes
the layer without clearing the one-shots: that is how they can apply to Base
letters. If the wrong modifier is armed, waiting for expiry discards it without
emitting it. This is an explicit usability tradeoff to evaluate in the trial.

One-shots are supplementary. They are not the planned way to sustain a modified
mouse action or produce modifier-only capture-release chords.

## Base: typing

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       Q     W     E     R     T  |   Y     U     I     O     P
C     A/Sh  S/Su  D/Al  F/Ct  G/AG | H/AG  J/Ct  K/Al  L/Su  ;/Sh
D       Z     X     C     V     B  |   N     M     ,     .     /
```

Row A is the familiar `` ` 1 2 3 4 5 | 6 7 8 9 0 - ``. `LB6` is backslash
and `RB6` is apostrophe, as optional convenience duplicates of Symbols.
`D6` stays unassigned. No essential modifier is placed on an outer B/D pinky key.

Hold modifiers are mirrored on corresponding fingers. G and H add two
opposite-hand routes to AltGr without spending a thumb or requiring E4.
Examples: hold J and tap A for tmux Ctrl+A; hold J and semicolon, then tap A,
for Ctrl+Shift+A. No A/Control dual role is needed for the tmux prefix.

Start the hold-tap trial with balanced, opposite-hand triggering. Tune timing
from actual typing and shortcut tests rather than claiming the original values
are already ideal. Reliable held-modifier alternatives remain available below.

## Functional modifier strip

Navigation, Numbers, Keypad, Function, and System have this **plain
held-modifier** strip on the left home row:

```text
LC5 Shift   LC4 Super   LC3 Alt   LC2 Ctrl   LC1 AltGr
```

These are immediate key-down/key-up modifiers with no tap behavior or timeout.
They can be held together and released without pressing a target key. On pages
whose targets conflict with that hand, use the selector's one-shots or a mirrored
held modifier where provided. The selector supplies a route to arbitrary
keyboard chords independently of the home row hold-tap decisions.

## Symbols: shell first, paired brackets

These are plain symbol keys, with no home row modifier behavior on this page.

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       !     #     $     %     &  |   \     (     )     *     ?
C       /     @     |     =     _  |   `     [     ]     '     "
D       ^     ;     ,     -     +  |   ~     {     }     <     >
```

The full left home row serves `/ @ | = _`. Vim's `$` sits above comma, and
`^ ; ,` are adjacent on the lower left. Quotes share the right home row.

Parentheses, square brackets, and braces share the **same opening/closing
columns** (`R2`/`R3`) on successive rows. Angle brackets are the neighboring
pair on the lower row (`RD4`/`RD5`): open first, close second, always left to right.
There is no fourth comfortable letter row, so this deliberate angle-pair
placement is the one departure from the vertical three-pair stack.

Dot remains directly available on Base at `RD4`; colon is Shift+semicolon on
Base or Shift plus this page's semicolon. For convenience, Symbols also places
dot on `RB6` and colon on `RD6`; neither extension is the only route to its
character. The comfortable routes together cover all standard ASCII punctuation.
Row A is unassigned on this page to make the new spatial organization explicit.

For a modified symbol, arm modifiers in the selector before selecting S.
Shifted symbol output combined with other modifiers needs an implementation
test; do not copy the original symbol macros without identifying a real need.

## Numbers and Keypad: identical geometry, distinct keycodes

Both pages share the right-hand grid and left modifier strip:

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       —     —     —     —     —  |   -     7     8     9     +
C      Sh    Su    Al    Ct    AG  |   0     4     5     6     =
D       —     —     —     —     —  |   .     1     2     3     /
```

Numbers emits ordinary digits (`N0`–`N9`) and ordinary punctuation. Keypad
emits `KP_N0`–`KP_N9`, keypad operators, keypad decimal, and keypad equals.
On Keypad only, `LB1` is Num Lock and `LB2` is native keypad Enter. The fixed
Enter thumb keeps sending ordinary Enter, preserving both distinct inputs.
Thus Alt+3 and Alt+keypad-3 remain distinct, and both have a direct held-modifier
path. Additional Shift on Numbers gives familiar shifted digit symbols.

The number row convenience remains on Base; these grids require no reaching
up to row A. Zero occupies the inner home-row index position, not a weak thumb.

## Function keys

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       —     —     —     —     —  |  F10   F7    F8    F9   PrtSc
C      Sh    Su    Al    Ct    AG  |  F11   F4    F5    F6     —
D       —     —     —     —     —  |  F12   F1    F2    F3     —
```

F1–F9 use the same 3-by-3 positions as digits 1–9. F10–F12 are the neighboring
inner column, top to bottom. Modifiers are plain held keys on the other hand.
F9 can therefore remain held for Omarchy's push-to-talk dictation shortcut.

## Navigation

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B       —     —     —     —     —  |   —   PgUp    Up   PgDn    —
C      Sh    Su    Al    Ct    AG  | Home  Left  Down  Right  End
D       —     —     —     —     —  |  Ins    —     —     —     —
```

The I/J/K/L positions form an up/left/down/right diamond. Home and End extend
the horizontal row; page movement is above. Backspace, Delete, Enter, Tab,
Escape, and Base return retain their global positions. No contextual editing
macros are needed here: Ctrl+arrows, Ctrl+Shift+arrows, Alt+arrows, and so forth
come from the modifier strip plus the target.

## Mouse

```text
       L5    L4    L3    L2    L1  |  R1    R2    R3    R4    R5
B      Back RClick  Up   LClick Middle | Forward —  ScrUp   —     —
C       —    Left  Down  Right   —  |   —  ScrLeft ScrDown ScrRight —
D      Sh    Su    Al    Ct    AG  |  AG    Ct    Al    Su    Sh
```

Left E/S/D/F moves the pointer: `LB3` up, `LC4` left, `LC3` down,
and `LC2` right. Right I/J/K/L scrolls. R (`LB2`) is left click,
W (`LB4`) is right click, and T (`LB1`) is middle click. Q/Y are back/forward.
Movement and left click share the index finger for rightward movement;
evaluate that reach during dragging. The agreed thumb anchors remain intact.

The plain held-modifier strip moves down to row D on **both** hands while
preserving its finger order. This is a deliberate Mouse-page exception:
the normal left home-row strip would collide with pointer movement.

- Ctrl+scroll: hold `LD2` (Ctrl), scroll with the right hand.
- Ctrl+click: hold `RD2` (Ctrl), press `LB2` (left click).
- Super+drag: hold `RD4` (Super), hold `LB2`, move with E/S/D/F.
- Super+resize: hold `RD4`, hold `LB4` (right click), move with E/S/D/F.
- Multi-modifier pointer actions: hold the right row-D modifiers.
- Multi-modifier scrolling: hold the left row-D modifiers.

No one-shot release-on-mouse assumption, modifier lock, or tap dance is needed.
Release the physical modifiers/buttons to end the operation. Pointer speed is
1200 and scroll speed is 20, twice ZMK v0.3's defaults of 600 and 10.
Acceleration timing remains unchanged.

## Windows / Omarchy

Redesigned on 2026-11-13 after physical use. Enter with **RC6 → RE1**;
RE1 selects Windows only in Menu and remains Enter elsewhere. The W selector
is removed. All actions below include their complete modifier chord.

Right columns 1–5, from center outward:

| Row | R1 | R2 | R3 | R4 | R5 |
| --- | --- | --- | --- | --- | --- |
| A | Workspace 1 | Workspace 2 | Workspace 3 | Workspace 4 | Workspace 5 |
| B | Swap left | Swap down | Swap up | Swap right | Fullscreen |
| C | Focus left | Focus down | Focus up | Focus right | Next monitor |
| D | Send silently WS1 | Send silently WS2 | Send silently WS3 | Send silently WS4 | Send silently WS5 |

Left columns 1–5, from center outward:

| Row | L1 | L2 | L3 | L4 | L5 |
| --- | --- | --- | --- | --- | --- |
| B | Toggle group | Join left group | Leave group | Next tab | Previous tab |
| C | Tiled fullscreen | Move window to next monitor | Move workspace to next monitor | — | — |
| D | — | — | — | — | — |

Left row A and the remaining unused positions have no action. Fixed anchors
remain, including Return to Base at RE2. There are no modifier strips on this
layer. **RA6 increases width; RB6 reduces width**, sending Super+Minus and
Super+Equal. These use the existing Scrolling presets (33.3%, 50%, 66.7%, 100%)
and retain 100px steps for floating windows and other layouts. Base shortcuts
also remain available.

`host/windows-layer.lua` supplies Scrolling-local horizontal focus and whole-column
swaps, with normal directional behavior on other layouts. It also binds the
LC2/LC3 monitor-transfer chords. Workspace selection and silent sends use
Omarchy's current monitor-local workspace slots. See
[implementation notes](windows-layer-proposal.md) for host installation, exact
transfer chords, assumptions, and verification.

## Modifier-only actions

Use the plain modifier strip already present on the utility pages. For example,
select Navigation, hold `LC2` (Ctrl) and `LC3` (Alt), then release them for an
application where that chord itself releases input capture. These produce
immediate modifier press and release events without a target key or lazy
activation. Return to Base with `RE2` afterward.

The same strip can modify a physical mouse without sending a navigation key.
Mouse also provides a mirrored right-hand strip where its left-hand targets
need opposite-hand modifiers. Windows uses complete action chords instead. One-shot keyboard modifiers
are available on the selector. A separate modifiers-only layer is unnecessary
in this draft.

## System: media, display, Bluetooth, and Compose

```text
       L5    L4    L3    L2    L1  |  R1      R2      R3      R4      R5
B      BT0   BT1   BT2   BT3   BT4 | Prev    Play    Next    Mute   Compose
C      Sh    Su    Al    Ct    AG  | Vol-    Vol+    Brite-  Brite+ CapsLock
D       —     —     —     —     —  | USB     BLE     BTprev  BTnext NumLock
```

Compose sends `K_APP`, then returns to Base for the compose sequence; the host
already maps Menu to Compose. The same action is available as selector then C.
Bluetooth profiles are numbered 0–4 as in ZMK; they are separate from desktop
workspaces 1–10. Output USB/BLE selects the keyboard output, not a profile erase.

Rare maintenance actions use row A only on this page:

- `LA1`: left-half bootloader.
- `RA1`: right-half bootloader.
- `LA6`: clear the current Bluetooth profile.

They have no automatic trigger during ordinary layer selection. All other row-A
positions remain unassigned. Bootloader reset remains source-specific.

## Spanish input

Keep the existing host `us(altgr-intl)` layout and `compose:menu` option. The
keyboard emits Right Alt, not character-specific Unicode macros.

On Base, hold the opposite-hand G/H AltGr key and type the host combination.
For a sequential alternative, open the selector, tap `RC1` for one-shot AltGr,
return to Base, then type the target. Add one-shot Shift when required.

The host symbols checked for this design give:

| Character | Host input |
| --- | --- |
| á é í ó ú | AltGr+A/E/I/O/U |
| ü | AltGr+Y |
| ñ | AltGr+N |
| ¿ | AltGr+Slash |
| ¡ | AltGr+Shift+1 |

Uppercase accented letters add Shift. The 1 for inverted exclamation can come
from the comfortable Numbers grid with held AltGr+Shift on the other hand.
The exact generated XKB map and physical text output must be checked during
implementation and the trial.

## Verification and physical trial

The ten-layer map is implemented only in `config/clean.keymap`. Both halves
compile with `./scripts/build-local --keymap clean`; generated artifacts are in
`firmware/clean/`. The original keymap and default build selection are preserved.
USB bootloader touch remains enabled only on the left build.

Review the file in the keymap viewer, especially the selector one-shot flow,
the Mouse row-D modifier exception, and the redesigned Windows actions. Flash the
clean artifact only when requested, then test real tasks. On 2026-10-21,
`./scripts/flash-left --keymap clean` rebuilt and installed the left artifact,
saved the previous firmware, and verified serial `23E5F50B0A98298E` returned as
a USB HID keyboard. The right half was not flashed. Typing and shortcut trials
have not yet been verified.

The physical trial should cover typing rolls and repeated letters; tmux Ctrl+A
then H/J/K/L and Ctrl+A twice; Escape; Alt+ordinary digit versus Alt+keypad digit;
Ctrl+Shift+arrows; Ctrl+F-key; the full Spanish character set; bracket/symbol
strings such as `${var}`, `$(cmd)`, `a_b=/path`, and `cmd | next`; modifier-only
Ctrl+Alt; modified click, scroll, and drag; workspace selection/movement; and
window resizing. A successful compile alone does not validate those interactions.

Latest install (2026-11-13): the redesigned Windows/Menu map built for both halves.
The original `config/lily58.keymap` and the other eight clean layers were unchanged.
Lua routing tests passed and Hyprland reloaded without configuration errors.
`./scripts/flash-left --keymap clean --no-build` backed up the previous firmware
and verified serial `23E5F50B0A98298E` returned as a USB keyboard. The right half
was built, not flashed. Firmware SHA256:
`db13b53570c6a5c4f2a0753034ee4005ca5268da1659c0f13d7da3ffc76435a2`.
The physical flash check verifies USB return, not every window/group action.

Follow-up on 2026-11-13: added RA6 width increase and RB6 width decrease.
Both halves built and compiled shortcuts were checked; left flashed with backup
and matching USB keyboard return verified. Latest left firmware SHA256:
`0a5f5f8f9cc97a8d5ec28a6df74ddb0cc37274ec26888f39a1e5174c8bff20d5`.
