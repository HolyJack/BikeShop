import { RouterProvider, createBrowserRouter } from "react-router-dom";

import RootLayout from "./pages/RootLayout";
import HomePage from "./pages/HomePage";
import ProductsPage, { loader as productsLoader } from "./pages/ProductsPage";
import AuthPage, { action as authAction } from "./pages/AuthPage";
import CartPage, { loader as cartLoader } from "./pages/CartPage";
import { tokenLoader } from "./utils/auth";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    id: "root",
    loader: tokenLoader,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "products/",
        element: <ProductsPage />,
        loader: productsLoader,
      },
      {
        path: "auth/",
        element: <AuthPage />,
        action: authAction,
      },
      {
        path: "cart/",
        element: <CartPage />,
        loader: cartLoader,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
