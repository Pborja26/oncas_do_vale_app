import * as types from "../../utils/global.types";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

type ButtonTypes = 
  "primary"
| "secondary"
| "close"
| "delete"

export interface ButtonProps {
  height?: types.Measurement;
  width?: types.Measurement;
  border?: types.BorderTypes;
  padding?: types.Measurement;
  gap?: types.Measurement;
  type?: ButtonTypes;
  style?: React.CSSProperties;
  icon?: IconDefinition;
  iconPosition?: "left" | "right";
  children?: React.ReactNode;
  isLoading?: boolean;
  color?: string;
  backgroundColor?: string;
}
