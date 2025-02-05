import * as types from "../../utils/global.types";

export interface DividerProps {
  direction: types.FlexDirection;
  size?: types.Measurement;
  width?: types.Measurement;
  color?: string;
  type?: types.BorderTypes;
  style?: React.CSSProperties;
  spacing?: types.Measurement;
}