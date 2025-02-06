import * as styled from "./label.styled";
import { LabelProps } from "./label.types";

const Label = ({
  label,
  style,
  variant,
  weight,
  color
}: LabelProps) => {
  return (
    <styled.LabelComponent
      style={style}
      variant={variant}
      weight={weight}
      color={color}
    >
      {label}
    </styled.LabelComponent>
  )
};

export default Label;
