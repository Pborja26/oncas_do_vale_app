import React from "react";
import * as types from "../../utils/global.types";

export interface ModalProps {
  children?: React.ReactNode;
  width?: types.Measurement;
  height?: types.Measurement;
  padding?: types.Measurement;
  style?: React.CSSProperties;
  headder?: string;
  subtilte?: string;
  footer?: boolean;
  onPrimaryClick?: () => void;
  onSecondaryClick?: () => void;
  onClose?: () => void;
}
