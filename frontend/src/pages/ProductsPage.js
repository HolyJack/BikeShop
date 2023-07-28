import Products from "../components/Products";
import { useLoaderData, json } from "react-router-dom";

const ProductsPage = () => {
  const data = useLoaderData();

  if (data.isError) {
    return <p>{data.message}</p>;
  }

  return <Products products={data} />;
};

export default ProductsPage;

export const loader = async () => {
  const response = await fetch("http://localhost:8000/api/products/");

  if (!response.ok) {
    throw json(
      { message: "Could not fetch events." },
      {
        status: 500,
      },
    );
  } else {
    return response;
  }
};
