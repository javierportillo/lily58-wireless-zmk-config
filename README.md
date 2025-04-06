# Gut's keymap for lily58

## Graphite Layout

```
~ ! @ # $ %  ^ & * ( ) { }
  B L D W Z  _ F O U J : + |
  N R T S G  Y H A E I ?
  Q X M C V  K P > " <

` 1 2 3 4 5  6 7 8 9 0 [ ]
  b l d w z  ' f o u j ; = \
  n r t s g  y h a e i ,
  q x m c v  k p . - /
```

Above is the base graphite layout in which my keymap is inspired. The changes are shown on the layers section.

## Special features

- This is my implementation for the Graphite Layout, it calls for some of the symbols to change their shifted output, this was achieved using mod-morph.
- Tap: Caps Word; 2x: CAPS LOCK
- Tap: BACKSPACE; 2x: CTRL + BACKSPACE
- Tap: SPACE; Hold: HYPER
- Home Row Mods
- Dedicated Shift Keys
- No momentary layers.
- Layer switching works like a standard transmission shift stick, you can always go from any layer to any other layer. On all layers:
  - Right thumb: tap to 1; double tap to 2.
  - Left  thumb: tap to 3; double tap to 4 (unused).

## Layers

```

All layers: HRM and Layer switching --------------------------------------------------------------------------
|       |     |     |     |      |      |       | |        |        |      |      |       |         |        |
|       |     |     |     |      |      |       | |        |        |      |      |       |         |        |
|       |     | GUI | ALT | CTRL |      |       | |        |        | CTL  | ALT  | GUI   |         |        |
| SHIFT |     |     |     |      |      |       | |        |        |      |      |       |         | SHIFT  |
|       |     |     |     |      | To 2 |       | |        | To 0/1 |      |      |       |         |        |
--------------------------------------------------------------------------------------------------------------

layer 0: Base ------------------------------------------------------------------------------------------------
| `     | 1   | 2   | 3   | 4    | 5    |       | |        | 6      | 7    | 8    | 9     | 0       | CAPS   |
| TAB   | B   | L   | D   | W    | Z    |       | |        | '      | F    | I    | O     | J       | ;      |
| ESC   | N   | R   | T   | S    | G    |       | |        | Y      | H    | A    | E     | I       | ,      |
| ▽     | Q   | X   | M   | C    | V    | PSCRN | | DEL    | K      | P    | .    | -     | /       | ▽      |
|       |     |     | INS | RALT | ▽    | SPACE | | ENTER  | ▽      | BSPC | ▤    |       |         |        |
--------------------------------------------------------------------------------------------------------------

layer 1: Symbol ----------------------------------------------------------------------------------------------
| F12   | F1  | F2  | F3  | F4   | F5   |       | |        | F6     | F7   | F8   | F9    | F10     | F11    |
| ▽     | !   | @   | [   | ]    | ¦    |       | |        | -      | 7    | 8    | 9     | *       | _      |
| ▽     | #   | $   | (   | )    | \    |       | |        | =      | 4    | 5    | 6     | +       | >      |
| ▽     | %   | ^   | {   | }    | &    | ▽     | | NUMLCK | /      | 1    | 2    | 3     | .       | <      |
|       |     |     | ▽   | ▽    | ▽    | ▽     | | ▽      | ▽      | ▽    | 0    |       |         |        |
--------------------------------------------------------------------------------------------------------------

layer 2: Navigation / Media ----------------------------------------------------------------------------------
| BTCLR | BT0 | BT1 | BT2 | BT3  | BT4  |       | |        | ▽      | ▽    | ▽    | MUTE  | Vol DWN | Vol UP |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽    |       | |        | HOME   | PGDN | PGUP | END   | ▽       | ▽      |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽    |       | |        | LEFT   | DOWN | UP   | RIGHT | ▽       | ▽      |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽    | ▽     | | ▽      | ⏮      | ⏯    | ⏭    | ▽     | ▽       | ▽      |
|       |     |     | ▽   | ▽    | ▽    | ▽     | | ▽      | ▽      | ▽    | ▽    |       |         |        |
--------------------------------------------------------------------------------------------------------------

```


