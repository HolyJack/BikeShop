import AuthButtons from "./AuthButtons";
import Navigation from "./Navigation";

const MainNavigation = () => {
  return (
    <header className="p-1 w-full h-16 bg-gray-500 font-mono flex flex-row justify-between">
      <Navigation />
      <AuthButtons />
    </header>
  );
};

export default MainNavigation;
