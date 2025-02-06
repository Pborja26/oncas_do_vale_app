import styled from "styled-components";
import { DividerProps } from "./divider.types";

export const DividerComponent = styled.div<DividerProps>`
  ${(props) => props.direction === "row" ? `
    height: 0px;
    width: ${props.size};
    margin-top: ${props.spacing};
    margin-bottom: ${props.spacing};
  ` : `
    height: ${props.size};
    width: 0px;
    margin-left: ${props.spacing};
    margin-right: ${props.spacing};
  `};
  color: ${props => props.color};
  border-width: ${props => props.width};
  border-style: ${props => props.type};
  border-radius: 8px
`;
