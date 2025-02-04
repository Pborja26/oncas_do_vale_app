import styled from "styled-components";
import { ModalProps } from "./modal.types";

export const BackDrop = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: #000;
  opacity: 0.2;
  display: flex;
  align-items: center;
  justify-content: center;
`

export const Container = styled.div<ModalProps>`
  width: ${props => props.width};
  height: ${props => props.height};
  padding: ${props => props.padding};
  border-radius: 8px;
  background-color: #fff;
`

export const Headder = styled.div`
  
`