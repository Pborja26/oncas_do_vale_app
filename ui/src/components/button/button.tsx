import * as button from "./button.styled";
import { ButtonProps } from "./button.types";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpinner, faXmark } from "@fortawesome/free-solid-svg-icons";


const Button = ({
  height = "60px",
  width = "150px",
  border = "solid",
  padding = "10px",
  gap = "10px",
  type,
  style,
  icon,
  iconPosition,
  children,
  isLoading,
  color,
  backgroundColor
}: ButtonProps) => {
  switch (type) {
    case "primary":
      return (
        <button.Container
          height={height}
          width={width}
          border={border}
          padding={padding}
          gap={gap}
          style={style}
          color={color}
          backgroundColor={backgroundColor}
        >
          {isLoading ? (
            <FontAwesomeIcon icon={faSpinner} color={color} spin />
          ) : (
            <>
              {icon && iconPosition === "left" && 
                <FontAwesomeIcon icon={icon} color={color} />
              }
              {children}
              {icon && iconPosition === "right" && 
                <FontAwesomeIcon icon={icon} color={color} />
              }
            </>
          )}
        </button.Container>
      )

    case "secondary":
      return <></>

    case "close":
      return (
        <button.Container
          height={"18px"}
          width={"18px"}
          backgroundColor={backgroundColor}
        >
          <FontAwesomeIcon icon={faXmark} color={color} />
        </button.Container>
      )
    
    default:
      return <></>
  }
}

export default Button;
