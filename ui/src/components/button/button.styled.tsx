import styled from "styled-components";
import { ButtonProps } from "./button.types";

export const Container = styled.button<ButtonProps>`
  width: ${props => props.width};
  height: ${props => props.height};
  border: ${props => props.border};
  padding: ${props => props.padding};
  background-color: ${props => props.backgroundColor};
  color: ${props => props.color};
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 8px;
`
