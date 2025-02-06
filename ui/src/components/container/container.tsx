import * as styled from "./container.styled";
import { ContainerProps } from "./container.types";

const Container = ({
    display = "flex",
    direction,
    align,
    justify,
    width = "100%",
    height = "100%",
    padding,
    gap,
    border,
    style,
    children
}: ContainerProps) => {
    return (
        <styled.ContainerComponent
            display={display}
            direction={direction}
            align={align}
            justify={justify}
            width={width}
            height={height}
            padding={padding}
            gap={gap}
            border={border}
            style={style}
        >
            {children}
        </styled.ContainerComponent>
    )
}

export default Container;
