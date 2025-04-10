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
- Tap: BACKSPACE; 2x: CTRL + BACKSPACE
- Tap: SPACE; Hold: HYPER
- Home Row Mods
- Dedicated Shift Keys
- No momentary layers.
- Layer switching works like a standard transmission shift stick, you can always go from any layer to any other layer. On all layers:
  - Right thumb: tap to 0; double tap to 1.
  - Left  thumb: tap to 2; double tap to 4.
- Mouse Emulation layer
- Combo: inner keys to clear current bluetooth profile

## Layers

```

All layers: HRM and Layer switching -----------------------------------------------------------------------------
|       |     |     |     |      |        |       | |        |        |       |      |       |         |        |
|       |     |     |     |      |        |       | |        |        |       |      |       |         |        |
|       |     | GUI | ALT | CTRL |        |       | |        |        | CTL   | ALT  | GUI   |         |        |
| SHIFT |     |     |     |      |        |       | |        |        |       |      |       |         | SHIFT  |
|       |     |     |     |      | To 2/3 |       | |        | To 0/1 |       |      |       |         |        |
-----------------------------------------------------------------------------------------------------------------

layer 0: Base ---------------------------------------------------------------------------------------------------
| `     | 1   | 2   | 3   | 4    | 5      |       | |        | 6      | 7     | 8    | 9     | 0       | CAPS   |
| TAB   | B   | L   | D   | W    | Z      |       | |        | '      | F     | I    | O     | J       | ;      |
| ESC   | N   | R   | T   | S    | G      |       | |        | Y      | H     | A    | E     | I       | ,      |
| ▽     | Q   | X   | M   | C    | V      | PSCRN | | DEL    | K      | P     | .    | -     | /       | ▽      |
|       |     |     | INS | RALT | ▽      | SPACE | | ENTER  | ▽      | BSPC  | ▤    |       |         |        |
-----------------------------------------------------------------------------------------------------------------

layer 1: Symbol -------------------------------------------------------------------------------------------------
| F12   | F1  | F2  | F3  | F4   | F5     |       | |        | F6     | F7    | F8   | F9    | F10     | F11    |
| ▽     | !   | @   | [   | ]    | ¦      |       | |        | -      | 7     | 8    | 9     | *       | _      |
| ▽     | #   | $   | (   | )    | \      |       | |        | = +    | 4     | 5    | 6     | 0       | >      |
| ▽     | %   | ^   | {   | }    | &      | ▽     | | NUMLCK | /      | 1     | 2    | 3     | .       | <      |
|       |     |     | ▽   | ▽    | ▽      | ▽     | | ▽      | ▽      | ▽     | ▽    |       |         |        |
-----------------------------------------------------------------------------------------------------------------

layer 2: Navigation / Media -------------------------------------------------------------------------------------
| ▽     | BT0 | BT1 | BT2 | BT3  | BT4    |       | |        | ▽      | ▽     | ▽    | MUTE  | Vol DWN | Vol UP |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽      |       | |        | HOME   | PGDN  | PGUP | END   | ▽       | ▽      |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽      |       | |        | LEFT   | DOWN  | UP   | RIGHT | ▽       | ▽      |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽      | ▽     | | ▽      | ⏮      | ⏯     | ⏭    | ▽     | ▽       | ▽      |
|       |     |     | ▽   | ▽    | ▽      | ▽     | | ▽      | ▽      | ▽     | ▽    |       |         |        |
-----------------------------------------------------------------------------------------------------------------

layer 3: Mouse Emulation ----------------------------------------------------------------------------------------
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽      |       | |        | ▽      | ▽     | ▽    | ▽     | ▽       | ▽      |
| ▽     | ▽   | GUI | MB4 | MB5  | ▽      |       | |        | S_LEFT | S_DWN | S_UP | S_RGT | ▽       | ▽      |
| ▽     | ▽   | MB3 | MB2 | MB1  | ▽      |       | |        | M_LEFT | M_DWN | M_UP | M_RGT | ▽       | ▽      |
| ▽     | ▽   | ▽   | ▽   | ▽    | ▽      | ▽     | | ▽      | ▽      | ▽     | ▽    | ▽     | ▽       | ▽      |
|       |     |     | ▽   | ▽    | ▽      | ALT   | | CTRL   | ▽      | ▽     | ▽    |       |         |        |
-----------------------------------------------------------------------------------------------------------------

```

## TODO:
- Right now I just need to use it for a while and search for improvement oportunities.
