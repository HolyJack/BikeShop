import { json } from "react-router-dom";
import { authToken } from "../utils/auth";

const Products = ({ products }) => {
  const productsList = products.map((product) => {
    const addToCartHandler = () => {};

    return (
      <li className="m-5 font-mono" key={product.id}>
        <div className="m-5 h-72 w-52 flex flex-col justify-end bg-yellow-500 rounded-xl items-center text-center">
          <div className="h-52 w-52">
            <img src="" alt="" />
          </div>
          <h1>{product.name}</h1>
          <button
            className="m-2 bg-white h-10 w-20 rounded-xl"
            onClick={addToCartHandler}
          >
            to Cart
          </button>
        </div>
      </li>
    );
  });

  return (
    <div className="h-full w-8/12 mx-auto">
      <ul className="grid grid-cols-4 justify-start">{productsList} </ul>
    </div>
  );
};

export default Products;

export const action = async (request) => {
  if (!authToken()) {
    throw json({ message: "User has to be logged in" }, { code: 500 });
  }
  const token = `Token ${authToken()}`;
  const data = request.data;

  const responce = await fetch("http://localhost:8000/api/cart/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`,
    },
    body: JSON.stringify(data),
  });

  if (!responce.ok) {
    throw json({ message: "error" }, { code: 500 });
  }
  return responce;
};
