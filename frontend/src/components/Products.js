const Products = ({ products }) => {
  const productsList = products.map((product) => {
    return (
      <li key={product.id}>
        <div className="m-5 bg-yellow-500 w-50 h-30 rounded-lg">
          <h1>{product.name}</h1>
          <p>{product.product_description}</p>
        </div>
      </li>
    );
  });

  return (
    <div className="h-full w-96 mx-auto">
      <ul className="flex flex-row flex-wrap justify-start">{productsList} </ul>
    </div>
  );
};

export default Products;
