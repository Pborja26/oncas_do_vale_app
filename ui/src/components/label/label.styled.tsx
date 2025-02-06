import styled from "styled-components";
import { LabelProps } from "./label.types";

export const LabelComponent = styled.div<LabelProps>`
  font-family: Inter;
  font-size: ${(props) => {
    switch (props.variant) {
      case "h1":
        return '2.5rem';
      case "h2":
        return '2rem';
      case "h3":
        return '1.75rem';
      case "p":
      default:
        return '1rem';
    }
  }};
  font-weight: ${props => props.weight};
  color: ${props => props.color || "#000"};
  display: flex;
  width: fit-content;
  height: fit-content;
`