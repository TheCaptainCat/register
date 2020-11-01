import ApiRequest from "@/core/api";
import { HttpMethod } from "@/core/requests";
import User from "@/composition/user/model";
import userStore from "@/composition/user/store";

async function getUserInfo(): Promise<User> {
  const request = new ApiRequest(HttpMethod.get, "/user/info");
  const response = await request.fetch<User>();
  return response.data;
}

async function login(username: string, password: string) {
  const request = new ApiRequest(HttpMethod.post, "/user/login", {
    username: username,
    password: password
  });
  const response = await request.fetch<User>();
  userStore.setState({ user: response.data });
}

async function logout() {
  const request = new ApiRequest(HttpMethod.post, "/user/logout");
  await request.fetch();
  userStore.setState({ user: undefined });
}

export default function useUserFunctions() {
  return {
    getUserInfo,
    login,
    logout
  };
}
