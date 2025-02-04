import React from "react";
import * as button from "./button.styled";
import { ButtonProps } from "./button.types";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpinner } from "@fortawesome/free-solid-svg-icons";

const Button = ({
  height,
  width,
  border,
  padding,
  type,
  style,
  icon,
  iconPosition,
  children,
  isLoading
}: ButtonProps) => {
  switch (type) {
    case "primary":
      return (
        <button.Container>
          {isLoading ? (
            <FontAwesomeIcon icon={faSpinner} spin />
          ) : (
            icon && iconPosition === "left" && (
              <FontAwesomeIcon icon={icon} />
            )
            
          )}
        </button.Container>
      )
    
    default:
      return <></>
  }
}

export default Button;
