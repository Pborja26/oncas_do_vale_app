import * as modal from "./modal.styled";
import Divider from "../divider/divider";
import Button from "../button/button";
import Container from "../container/container";
import Label from "../label/label";
import { ModalProps } from "./modal.types";

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
      <modal.Container 
        width={width} 
        height={height}
        padding={padding}
        style={style}
      >
        {headder && (
          <Container display="flex" direction="row" align="center" justify="space-between" >
            <Container direction="column" >
              <Label label={headder} variant="h2" />
              <Label label={subtilte} variant="p" />
            </Container>
          </Container>
        )}
        {children}
      </modal.Container>
    </modal.BackDrop>
  )
};

export default Modal;
