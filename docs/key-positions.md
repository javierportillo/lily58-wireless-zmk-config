# Physical key position names

Use **`<side><row><column>`**, for example `LB3`. These names identify physical
positions and stay the same when their bindings change. They are independent of
ZMK's numeric key-position indices.

When the side is omitted, the position applies to **both halves**: `D0` means
`LD0` and `RD0`. Likewise, `C6` means both outer home-row keys, and `E2` means
both second thumb positions. An unsided range applies to the same range on
each half.

## Sides and rows

| Component | Meaning |
| --- | --- |
| `L` | Left half |
| `R` | Right half |
| `A` | Top / number row |
| `B` | Upper letter row |
| `C` | Home row |
| `D` | Lower letter row, including the extra inner key on each half |
| `E` | Thumb row |

## Columns

Number columns **from the center outward** on both halves:

- Rows A–D use `1` for the innermost main column through `6` for the outermost.
- The extra inner keys on row D are `LD0` and `RD0`.
- Thumbs use `E1` through `E4`, beginning with the main inner thumb and moving
  outward.

Viewed from above, in normal typing orientation:

```text
           LEFT                  RIGHT
outer →             center             → outer

A    6 5 4 3 2 1       |       1 2 3 4 5 6
B    6 5 4 3 2 1       |       1 2 3 4 5 6
C    6 5 4 3 2 1       |       1 2 3 4 5 6
D    6 5 4 3 2 1 0     |     0 1 2 3 4 5 6
E        4 3 2 1       |       1 2 3 4
```

## Ranges and simultaneous presses

- `LB3`: one physical position.
- `LB1–LB5`: an inclusive range on one side and row, from center outward.
- `LD0 + RD0`: both positions pressed together.
- `LE1 / RE1`: a pair of corresponding positions; does not imply a combo.

Describe positions with these names in discussions and design notes. Read the
selected `.keymap` file to determine the keys currently assigned to them.
