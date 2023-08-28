import { useRouteLoaderData } from "react-router-dom";
import AuthButtons from "./AuthButtons";
import Navigation from "./Navigation";

const MainNavigation = () => {
  return (
    <header className="p-1 w-full h-16 bg-gray-500 font-mono flex flex-row justify-between">
      <div className="m-auto w-8/12 flex justify-between">
        <Navigation />
        <AuthButtons />
      </div>
    </header>
  );
};

export default MainNavigation;
