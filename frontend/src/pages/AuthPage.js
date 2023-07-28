import { Form, json, redirect } from "react-router-dom";

const AuthPage = () => {
  return (
    <div className="h-full w-96 mx-auto">
      <Form method="post">
        <div>
          <label htmlFor="email">E-mail</label>
          <input
            id="email"
            type="email"
            name="email"
            placeholder="example@example.com"
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input id="password" type="password" name="password" />
        </div>
        <div>
          <button type="submit" className="bg-yellow-500">
            Login
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

  if (responce.ok) {
    return redirect("/");
    return responce;
  }
};
