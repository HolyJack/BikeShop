import { NavLink, useRouteLoaderData } from "react-router-dom";
import { logout } from "../utils/auth";

const AuthButtons = () => {
  const token = useRouteLoaderData("root");

  const logoutHandler = () => {
    logout();
  };

  return (
    <div className=" flex flex-row items-center justify-center">
      {!token && (
        <NavLink to="/auth">
          <div className="p-1 w-20 h-8 bg-yellow-500 text-center rounded-lg">
            Login
          </div>
        </NavLink>
      )}
      {token && (
        <NavLink onClick={logoutHandler} to="/">
          <div className="p-1 w-20 h-8 bg-yellow-500 text-center rounded-lg">
            Logout
          </div>
        </NavLink>
      )}
    </div>
  );
};

export default AuthButtons;
