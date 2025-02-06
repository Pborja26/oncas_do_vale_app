import * as types from "../../utils/global.types";

type InputTypes = 
  "text" 
| "radio"
| "checkbox"
| "range" 

export interface InputProps {
  type?: InputTypes;
  height?: types.Measurement;
  width?: types.Measurement;
  borderWidth?: types.Measurement;
  padding?: types.Measurement;
  isChecked?: boolean;
}