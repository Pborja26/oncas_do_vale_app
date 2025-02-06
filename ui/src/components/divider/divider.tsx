import * as styled from "./divider.styled";
import { DividerProps } from "./divider.types";

const Divider = ({
    direction = "row",
    size = "90%",
    width = "1px",
    color = "#000",
    type = "solid",
    style,
    spacing = "10px"
}: DividerProps) => {
    return (
        <styled.DividerComponent
            direction={direction}
            size={size}
            width={width}
            color={color}
            type={type}
            style={style}
            spacing={spacing}
        />
    )
};

export default Divider;
