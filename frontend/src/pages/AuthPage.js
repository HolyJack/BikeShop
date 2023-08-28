import { Form, json, redirect } from "react-router-dom";

const AuthPage = () => {
  return (
    <div className="h-full w-96 mx-auto font-mono">
      <Form
        className="py-6 px-10 m-5 h-full w-fit bg-gray-600 flex flex-col justify-center items-center shadow shadow-gray-900 rounded-xl"
        method="post"
      >
        <h1 className="w-full mb-5 text-center font-bold text-4xl">Login</h1>
        <div className="  py-1 w-full flex flex-row justify-between items-center">
          <label className=" w-24 " htmlFor="email">
            E-mail:
          </label>
          <input
            className="px-2 rounded-lg"
            id="email"
            type="email"
            name="email"
            placeholder="example@example.com"
            required
          />
        </div>
        <div className=" py-1 w-full flex flex-row justify-between items-center">
          <label className="w-24 " htmlFor="password">
            Password:
          </label>
          <input
            className="px-2 rounded-lg"
            id="password"
            type="password"
            name="password"
            required
          />
        </div>
        <div className=" mt-3 py-2 w-full flex flex-row justify-end items-center">
          <button className=" m-1 w-20 h-8 bg-transparent rounded-lg">
            Sign up
          </button>
          <button
            className=" m-1 w-20 h-8 bg-yellow-500 rounded-lg"
            type="submit"
          >
            Sign in
          </button>
        </div>
      </Form>
    </div>
  );
};

export default AuthPage;

export const action = async ({ request }) => {
  const data = await request.formData();
  const authData = {
    username: data.get("email"),
    password: data.get("password"),
  };

  const responce = await fetch("http://localhost:8000/api-token-auth/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(authData),
  });

  if (responce.satus === 422 || responce.status === 401) {
    return responce;
  }

  if (!responce.ok) {
    throw json({ message: "Could not authenticate user" }, { status: 500 });
  }
  const resData = await responce.json();
  const token = resData.token;

  localStorage.setItem("token", token);
  console.log(token);

  return redirect("/");
};
