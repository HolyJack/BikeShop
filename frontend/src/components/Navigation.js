import { NavLink } from "react-router-dom";

const Navigation = () => {
  return (
    <nav>
      <ul className="h-full w-40 flex flex-row justify-between items-center">
        <li>
          <NavLink to="/">
            <div className="m-2 h-8 w-24 bg-yellow-500 rounded-lg text-center items-center font-bold">
              HOME
            </div>
          </NavLink>
        </li>
        <li>
          <NavLink to="/products">
            <div className="m-2 h-8 w-24 bg-yellow-500 rounded-lg text-center items-center font-bold">
              PRODUCTS
            </div>
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
