import styled from "styled-components";
import { ModalProps } from "./modal.types";

export const BackDrop = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: rgba(99, 99, 99, 0.3);
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
  box-shadow: 0px 4px 8px 0px;
`

export const Headder = styled.div`
  
`