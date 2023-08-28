import { NavLink } from "react-router-dom";

const NAV_ITEMS = [
  {
    id: "n1",
    link: "/",
    name: "Home",
  },
  {
    id: "n2",
    link: "/products",
    name: "Products",
  },
  {
    id: "n3",
    link: "/cart",
    name: "Cart",
  },
];

const Navigation = () => {
  const navList = NAV_ITEMS.map((item) => {
    return (
      <li key={item.id}>
        <NavLink to={item.link}>
          <div className="p-1 m-2 h-8 w-24 rounded-lg text-center hover:bg-white">
            {item.name}
          </div>
        </NavLink>
      </li>
    );
  });

  return (
    <nav>
      <ul className="flex flex-row justify-between items-center">{navList}</ul>
    </nav>
  );
};

export default Navigation;
