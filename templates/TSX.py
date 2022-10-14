def TSX(name):
    nameCapitalize = name.capitalize()
    return f"""
import React, {{ FC }} from "react";
import {{ view, ViewProps, ViewType }} from "@itcs/react-mvvm";
import {{ {nameCapitalize}ViewModel }} from "./{nameCapitalize}ViewModel";

interface {nameCapitalize}Props extends ViewProps<{nameCapitalize}ViewModel> {{
    viewModel: {nameCapitalize}ViewModel;
}}

export const {nameCapitalize}: FC<{nameCapitalize}Props> = () => {{
    return (
            <ExtPortal extComponentId={{"{name}React"}}>
                <{nameCapitalize}Component />
            </ExtPortal>
          )
}};

const {name}: FC<{nameCapitalize}Props> = ({{ viewModel }}) => {{
    return <></>
}};

const {nameCapitalize}Component: ViewType<{nameCapitalize}Props> = React.memo(view("{nameCapitalize}ViewModel")({name} as FC));
"""


# import React, { FC } from "react";
# import { view, ViewProps, ViewType } from "@itcs/react-mvvm";
# import { RootPanelViewModel } from "./RootPanelViewModel";

# interface RootPanelProps extends ViewProps<RootPanelViewModel> {
#     viewModel: RootPanelViewModel;
# }

# export const RootPanel: FC<RootPanelProps> = () => {
#     return (
#             <ExtPortal extComponentId={"dhcpServerReact"}>
#               <DHCPServerComponent />
#            </ExtPortal>
#           )
# };

# const rootPanel: FC<RootPanelProps> = ({ viewModel }) => {
#     return <>{}</>
# };

# const RootPanelComponent: ViewType<RootPanelProps> = React.memo(view("RootPanelViewModel")(rootPanel as FC));