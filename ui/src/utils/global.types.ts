export type BorderTypes = 
  "none"
| "dotted"
| "dashed"
| "solid"
| "double"
| "groove"
| "ridge"
| "inset"
| "outset"

export type JustifyContent = 
  "flex-start"
| "flex-end"
| "center"
| "space-between"
| "space-around"

export type AlignItems = 
  "start"
| "center"
| "end"
| "stretch"

export type FlexDirection = 
  "row"
| "column"

export type Display =
  "flex"
| "grid"
| "block"
| "none"

export type Measurement = 
  `${number}px`
| `${number}rem`
| `${number}%`
| `${number}vw`
| `${number}vh`
| Array< `${number}px` | `${number}rem` | `${number}%` | `${number}vw` | `${number}vh` >;
