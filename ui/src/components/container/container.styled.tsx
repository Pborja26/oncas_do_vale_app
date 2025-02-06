import styled from "styled-components";
import { ContainerProps } from "./container.types";

export const ContainerComponent = styled.div<ContainerProps>`
    display: ${props => props.display};
    flex-direction: ${props => props.direction};
    align-items: ${props => props.align};
    justify-content: ${props => props.justify};
    width: ${props => props.width};
    height: ${props => props.height};
    padding: ${props => props.padding};
    gap: ${props => props.gap};
    border: ${props => props.border};
`
