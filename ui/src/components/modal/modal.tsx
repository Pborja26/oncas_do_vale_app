import * as modal from "./modal.styled";
import Divider from "../divider/divider";
import Button from "../button/button";
import { ModalProps } from "./modal.types";
import Container from "../container/container";

const Modal = ({
  children,
  width,
  height,
  padding,
  style,
  headder,
  subtilte,
  footer,
  onClose,
  onPrimaryClick,
  onSecondaryClick
}: ModalProps) => {
  return (
    <modal.BackDrop>
      <modal.Container width={"200px"} height={"200px"}>

      </modal.Container>
    </modal.BackDrop>
  )
};

export default Modal;
