import { redirect } from "react-router-dom";

export const authToken = () => {
  return localStorage.getItem("token");
};

export const tokenLoader = () => {
  return authToken();
};

export function logout() {
  localStorage.removeItem("token");
  return redirect("/");
}
