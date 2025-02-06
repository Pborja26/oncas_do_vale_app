import * as types from "../../utils/global.types";

export interface ContainerProps {
    display?: types.Display;
    direction?: types.FlexDirection;
    align?: types.AlignItems;
    justify?: types.JustifyContent;
    width?: types.Measurement;
    height?: types.Measurement;
    padding?: types.Measurement;
    gap?: types.Measurement;
    border?: types.BorderTypes;
    style?: React.CSSProperties;
    children?: React.ReactNode;
}
