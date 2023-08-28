import { useLoaderData } from "react-router-dom";
import CartItem from "./Cart/CartItem";

const Cart = () => {
  const cartData = useLoaderData()["cart_item"];
  let cartItems = [];

  if (cartData) {
    cartItems = cartData.map((data) => <CartItem />);
  }

  return (
    <div>
      <ul>{cartItems}</ul>
    </div>
  );
};

export default Cart;
