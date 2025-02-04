import styled from "styled-components";
import { ButtonProps } from "./button.types";

export const Container = styled.button<ButtonProps>`
  width: ${props => props.width};
  height: ${props => props.height};
  border: ${props => props.border};
  padding: ${props => props.padding};
`
