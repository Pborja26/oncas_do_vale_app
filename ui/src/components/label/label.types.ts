type TextVariant = 
  "h1"
| "h2"
| "h3"
| "p"

export interface LabelProps {
  label?: string;
  style?: React.CSSProperties;
  variant?: TextVariant;
  weight?: number;
  color?: string;
}