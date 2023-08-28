import { Outlet } from "react-router-dom";
import MainNavigation from "../components/MainNavigation";

const RootLayout = () => {
  return (
    <>
      <MainNavigation />
      <main className="h-full w-full">
        <Outlet></Outlet>
      </main>
    </>
  );
};

export default RootLayout;
