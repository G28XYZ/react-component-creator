import React, { FC } from "react";
import { view, ViewProps, ViewType } from "@itcs/react-mvvm";
import { TestViewModel } from "./TestViewModel";

interface TestProps extends ViewProps<TestViewModel> {
    viewModel: TestViewModel;
}

export const Test: FC<TestProps> = () => {
    return (
            <ExtPortal extComponentId={"testReact"}>
                <TestComponent />
            </ExtPortal>
          )
};

const test: FC<TestProps> = ({ viewModel }) => {
    return <></>
};

const TestComponent: ViewType<TestProps> = React.memo(view("TestViewModel")(test as FC));