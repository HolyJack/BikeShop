import { json, useLoaderData } from "react-router-dom";
import Cart from "../components/Cart";
import { authToken } from "../utils/auth";

const CartPage = () => {
  const cartData = useLoaderData();
  const cartItemsData = cartData["cart_items"];

  return <Cart cartData={cartItemsData} />;
};

export default CartPage;

export const loader = async () => {
  const token = `Token ${authToken()}`;

  const responce = await fetch("http://localhost:8000/api/cart/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
  });

  if (!responce.ok) {
    throw json({ message: "error" }, { status: 500 });
  }

  return responce;
};
